# -*- coding: utf-8 -*-
import unittest
import logging
import sys
import os  # noqa: F401
import time

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except BaseException:
    from configparser import ConfigParser  # py3

from biokbase.workspace.client import Workspace as workspaceService
from ExpressionUtils.ExpressionUtilsServer import MethodContext
from ExpressionUtils.authclient import KBaseAuth as _KBaseAuth

from ExpressionUtils.core.expression_utils import ExpressionUtils


class GFFUtilsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__LOGGER = logging.getLogger('ExpressionUtils_test')
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

    def test_get_expression_levels_cufflinks(self):

        exp_utils = ExpressionUtils(self.__class__.cfg, self.__class__.__LOGGER)

        fpkm_dict, tpm_dict = exp_utils.get_expression_levels(
            filepath='data/expression_utils/cufflinks.genes.fpkm_tracking')

        self.assertEquals(45, len(fpkm_dict))
        self.assertEquals(45, len(tpm_dict))

    def test_get_expression_levels_stringtie(self):
        exp_utils = ExpressionUtils(self.__class__.cfg) # no logger specified

        fpkm_dict, tpm_dict = exp_utils.get_expression_levels(
            filepath='data/expression_utils/stringtie.genes.fpkm_tracking')

        self.assertEquals(49, len(fpkm_dict))
        self.assertEquals(49, len(tpm_dict))

    def test_get_expression_levels_zero_sum_fpkm(self):
        exp_utils = ExpressionUtils(self.__class__.cfg) # no logger specified

        fpkm_dict, tpm_dict = exp_utils.get_expression_levels(
            filepath='data/expression_utils/zero_sum_fpkm.genes.fpkm_tracking')

        self.assertEquals(49, len(fpkm_dict))
        self.assertEquals(49, len(tpm_dict))

        sum_tpm = 0.0
        for tpm in tpm_dict.values():
            sum_tpm += tpm
        self.assertEquals(0.0, sum_tpm)
