# -*- coding: utf-8 -*-
import unittest
import logging
import sys
import os  # noqa: F401
import time
import hashlib

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except BaseException:
    from configparser import ConfigParser  # py3

from biokbase.workspace.client import Workspace as Workspace
from ExpressionUtils.ExpressionUtilsImpl import ExpressionUtils
from ExpressionUtils.ExpressionUtilsServer import MethodContext
from ExpressionUtils.authclient import KBaseAuth as _KBaseAuth

from ExpressionUtils.core.gff_utils import GFFUtils
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
import shutil


class GFFUtilsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__LOGGER = logging.getLogger('GFFUtils_test')
        cls.__LOGGER.setLevel(logging.INFO)
        streamHandler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s")
        formatter.converter = time.gmtime
        streamHandler.setFormatter(formatter)
        cls.__LOGGER.addHandler(streamHandler)
        cls.__LOGGER.info("Logger was set")

        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('ExpressionUtils'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        auth_service_url = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(auth_service_url)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'ExpressionUtils',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.serviceImpl = ExpressionUtils(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

        # create workspace that is local to the user if it does not exist
        cls.ws = Workspace(url=cls.wsURL)
        cls.ws_id = 'ExpressionUtils_test_' + user_id

        try:
            ws_info = cls.ws.get_workspace_info({'workspace': cls.ws_id})
            print("workspace already exists: " + str(ws_info))
        except BaseException:
            ws_info = cls.ws.create_workspace(
                {'workspace': cls.ws_id, 'description': 'Workspace for ExpressionUtils_test'})
            print("Created new workspace: " + str(ws_info))

        print('using workspace_name: ' + cls.ws_id)

        # data has to be copied to tmp dir so it can be seen by
        # GenomeFileUtil subjob running in a separate docker container
        INPUT_DATA_DIR = "/kb/module/test/data/gff_utils"
        TMP_INPUT_DATA_DIR = "/kb/module/work/tmp"
        input_file_name = 'at_chrom1_section.gbk'
        input_data_path = os.path.join(INPUT_DATA_DIR, input_file_name)

        tmp_input_data_path = os.path.join(TMP_INPUT_DATA_DIR, input_file_name)
        shutil.copy(input_data_path, tmp_input_data_path)

        genbankToGenomeParams = {"file": {"path": tmp_input_data_path},
                                 "genome_name": "at_chrom1_section",
                                 "workspace_name": cls.ws_id,
                                 "source": "thale-cress",
                                 "release": "1TAIR10",
                                 "generate_ids_if_needed": True,
                                 "type": "User upload"
                                 }
        gfu = GenomeFileUtil(os.environ['SDK_CALLBACK_URL'], token=token,
                             auth_svc=auth_service_url)
        cls.genome_upload_result = gfu.genbank_to_genome(genbankToGenomeParams)
        print('genbank_to_genome save result: ' + str(cls.genome_upload_result))

    def test_convert_gff_to_gtf(self):
        gtf_file_path = '/kb/module/work/at_chrom1_section.gtf'

        if os.path.exists(gtf_file_path):
            os.remove(gtf_file_path)

        gff_utils = GFFUtils(self.__class__.cfg, self.__class__.__LOGGER)

        result = gff_utils.convert_gff_to_gtf(gff_file_path='data/gff_utils/at_chrom1_section.gff',
                                              gtf_file_path=gtf_file_path)

        self.assertEquals(result, 0)
        self.assertTrue(gtf_file_path)
        self.assertEquals(hashlib.md5(open(gtf_file_path, 'rb').read()).hexdigest(),
                          '73288223c46c11ec23bf9602ac1ef72f')

    def test_convert_genome_to_gff(self):
        gff_utils = GFFUtils(self.__class__.cfg, self.__class__.__LOGGER)

        gff_file_path = gff_utils.convert_genome_to_gff(
            self.__class__.genome_upload_result['genome_ref'],
            '/kb/module/work/tmp')

        self.assertEquals("/kb/module/work/tmp/at_chrom1_section.gff", str(gff_file_path))
        self.assertEquals(hashlib.md5(open(gff_file_path, 'rb').read()).hexdigest(),
                          'b21026788423648b2a1e200af702ff44')

    def test_convert_genome_to_gtf(self):
        target_path = '/kb/module/work/tmp/at_chrom1_section_test.gtf'
        gff_utils = GFFUtils(self.__class__.cfg, self.__class__.__LOGGER)
        result = gff_utils.convert_genome_to_gtf(self.__class__.genome_upload_result['genome_ref'],
                                                 target_path)
        self.assertEquals(result, 0)
        self.assertTrue(os.path.exists(target_path))
        self.assertEquals(hashlib.md5(open(target_path, 'rb').read()).hexdigest(),
                          '73288223c46c11ec23bf9602ac1ef72f')

    def test_get_gff_annotation_ref(self):
        gff_utils = GFFUtils(self.__class__.cfg, self.__class__.__LOGGER)
        result = gff_utils.create_gff_annotation_from_genome(
            self.__class__.genome_upload_result['genome_ref'], self.__class__.ws_id)

        obj = self.__class__.ws.get_objects([{'ref': result}])
        self.assertEquals('KBaseRNASeq.GFFAnnotation-3.0', obj[0]['info'][2])
