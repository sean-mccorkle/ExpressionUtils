# -*- coding: utf-8 -*-
import unittest
import logging
import sys
import os  # noqa: F401
import time
import hashlib
from ExpressionUtils.core import script_utils

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except BaseException:
    from configparser import ConfigParser  # py3

from biokbase.workspace.client import Workspace as workspaceService
from ExpressionUtils.ExpressionUtilsImpl import ExpressionUtils
from ExpressionUtils.ExpressionUtilsServer import MethodContext
from ExpressionUtils.authclient import KBaseAuth as _KBaseAuth

from ExpressionUtils.core.gff_utils import GFFUtils


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
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
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
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = ExpressionUtils(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    def test_convert_gff_to_gtf(self):
        opath = '/kb/module/work/'
        ofile = 'at_chrom1_section.gtf'

        if os.path.exists(opath + ofile):
            os.remove(opath + ofile)

        gff_utils = GFFUtils(self.__class__.cfg, self.__class__.__LOGGER)

        result = gff_utils.convert_gff_to_gtf(ifile='at_chrom1_section.gff3',
                                              ipath='data/gff_utils',
                                              ofile=ofile,
                                              opath=opath)

        self.assertEquals(result, 0)
        self.assertTrue(os.path.exists(opath + ofile))
        self.assertEquals(hashlib.md5(open(opath + ofile, 'rb').read()).hexdigest(),
                          '7fd7ba7896c9819bcabed53aa72a6de7')
