# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import time
import inspect
import shutil
import json

from os import environ

try:
    from ConfigParser import ConfigParser  # py2
except BaseException:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from DataFileUtil.DataFileUtilClient import DataFileUtil
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
from ExpressionUtils.ExpressionUtilsImpl import ExpressionUtils
from ExpressionUtils.ExpressionUtilsServer import MethodContext
from ExpressionUtils.authclient import KBaseAuth as _KBaseAuth
from GenomeAnnotationAPI.GenomeAnnotationAPIClient import GenomeAnnotationAPI

class ExprMatrixUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('ExpressionUtils'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        # authServiceUrlAllowInsecure = cls.cfg['auth_service_url_allow_insecure']
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
        suffix = int(time.time() * 1000)
        cls.wsName = "test_exprMatrixUtils_" + str(suffix)
        cls.wsClient.create_workspace({'workspace': cls.wsName})
        cls.serviceImpl = ExpressionUtils(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        #cls.dfu = DataFileUtil(cls.callback_url, service_ver='dev')
        cls.dfu = DataFileUtil( cls.callback_url )
        cls.ws_id = cls.dfu.ws_name_to_id(cls.wsName)
        cls.gaa = GenomeAnnotationAPI( cls.callback_url )
        cls.gfu = GenomeFileUtil(cls.callback_url)
        cls.setupdata()

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        return self.__class__.wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    @classmethod
    def setupdata(cls):

        # 
        # load genome first
        #
        genome_file_name = 'eFEM_test_genome.json'
        genome_file_path = os.path.join('data', genome_file_name)
        print "### genome file path is {0}".format( genome_file_path )

        with open( genome_file_path ) as genome_file:  
            genome = json.load( genome_file )

            gen_info = cls.gaa.save_one_genome_v1( { 'workspace': cls.wsName,
                                                     'data': genome,
                                                     'name': 'at'
                                                 } ).get('info')
            cls.genome_ref = "{0}/{1}/{2}".format( gen_info[6], gen_info[0], gen_info[4] )
            print "### genome_ref is {0}".format( cls.genome_ref )

            #gen_ref = cls.wsClient.save_objects( {
            #  objdata = cls.wsClient.save_objects({                                                                                  
            #'workspace': cls.getWsName(),                                                                                      
            #'objects': [{'type': 'Empty.AType',                                                                                
            #             'data': {},                                                                                           
            #             'name': 'empty'                                                                                       
            #             }]                                                                                                    
            #  })[0]                                                                                                                  
        print "### genome_ref is again {0}".format( cls.genome_ref )

        # Read DEM test object and save

        dem_file_name = "eFEM_test_dem.json"
        dem_file_path = os.path.join('data', dem_file_name)
        print "### dem file path is {0}".format( dem_file_path )
        with open( dem_file_path ) as dem_file:  
            dem = json.load( dem_file )
            dem["genome_ref"] = cls.genome_ref
            print "### dem is "
            pprint( dem )

            dem_info = cls.dfu.save_objects( { 'id': cls.ws_id, 
                                               'objects': [ {'type': 'KBaseFeatureValues.DifferentialExpressionMatrix', 
                                                             'data': dem, 
                                                             'name': 'dem'} ]
                                           } )[0]
            print "### dem_info is {0}".format( dem_info )
            cls.dem_ref = "{0}/{1}/{2}".format( dem_info[6], dem_info[0], dem_info[4] )
            print "### dem_ref is {0}".format( cls.dem_ref )

        # Read FEM test object and save

        fem_file_name = "eFEM_test_fem.json"
        fem_file_path = os.path.join('data', fem_file_name)
        print "### fem file path is {0}".format( fem_file_path )
        with open( fem_file_path ) as fem_file:
            fem = json.load( fem_file )
            fem["genome_ref"] = cls.genome_ref
            print "### fem is "
            pprint( fem )

            # Save without DEM provenance

            fem_info = cls.dfu.save_objects( { 'id': cls.ws_id, 
                                               'objects': [ {'type': 'KBaseFeatureValues.ExpressionMatrix', 
                                                             'data': fem, 
                                                             'name': 'fem_no_dem_prov'} ]
                                           } )[0]
            print "### fem_info is {0}".format( fem_info )
            cls.fem_no_prov_ref = "{0}/{1}/{2}".format( fem_info[6], fem_info[0], fem_info[4] )
            print "### fem_no_prov_ref is {0}".format( cls.fem_no_prov_ref )

            # Save with DEM provenance

            fem_info = cls.dfu.save_objects( { 'id': cls.ws_id, 
                                               'objects': [ {'type': 'KBaseFeatureValues.ExpressionMatrix', 
                                                             'data': fem, 
                                                             'name': 'fem',
                                                             'extra_provenance_input_refs': [cls.dem_ref]
                                                          } ]
                                           } )[0]
            cls.fem_prov_ref = "{0}/{1}/{2}".format( fem_info[6], fem_info[0], fem_info[4] )
            print "### fem_prov_ref is {0}".format( cls.fem_prov_ref )
                                                       
        #shutil.copy(os.path.join('data', genbank_file_name), genbank_file_path)
        pass

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa

    def get_enhancedFEM_test( self ):
        print "### enhancedFEM_Test - yay" 
        print "### self.genome_ref {0}".format( self.genome_ref )
        print "### self.dem_ref {0}".format( self.dem_ref )
        print "### self.fem_no_prov_ref {0}".format( self.fem_no_prov_ref )
        print "### self.fem_prov_ref {0}".format( self.fem_prov_ref )

        ret = self.getImpl().get_enhancedFilteredExpressionMatrix( self.ctx, 
                                                            {'fem_object_ref': self.fem_prov_ref} )
        pprint( ret )
        pass


#    def get_expr_matrix_success(self, input_exprset_ref, output_obj_name):
#
#        test_name = inspect.stack()[1][3]
#        print('\n*** starting expected get expr matrix success test: ' + test_name + ' *****************')
#
#        params = {'expressionset_ref': input_exprset_ref,
#                  'workspace_name': self.getWsName(),
#                  'output_obj_name': output_obj_name,
#                  }
#
#        getExprMat_retVal = self.getImpl().get_expressionMatrix(self.ctx, params)[0]
#
#        inputObj = self.dfu.get_objects(
#                                    {'object_refs': [input_exprset_ref]})['data'][0]
#
#        print("============ INPUT EXPRESSION SET OBJECT ==============")
#        pprint(inputObj)
#        print("==========================================================")
#
#        fpkm_ref = getExprMat_retVal.get('exprMatrix_FPKM_ref')
#        tpm_ref = getExprMat_retVal.get('exprMatrix_TPM_ref')
#
#        '''
#        outputFPKM_Obj = self.dfu.get_objects(
#            {'object_refs': [fpkm_ref]})['data'][0]
#
#        print("============  EXPRESSION MATRIX FPKM OUTPUT  ==============")
#        pprint(outputFPKM_Obj)
#        print("==========================================================")
#        
#        outputTPM_Obj = self.dfu.get_objects(
#            {'object_refs': [tpm_ref]})['data'][0]
#
#        print("============  EXPRESSION MATRIX TPM OUTPUT  ==============")
#        pprint(outputTPM_Obj)
#        print("==========================================================")
#        '''
#
#        print("============   FPKM REF  ==============  " + fpkm_ref)
#        print("============   TPM REF  ==============" + tpm_ref)
#
#    # Following test uses object refs from a narrative. Comment the next line to run the test
#    @unittest.skip("skipped test_get_expr_matrix_rnaseq_exprset_success")
#    def test_get_expr_matrix_rnaseq_exprset_success(self):
#        """
#        Input object 1: downsized_AT_reads_hisat2_AlignmentSet_stringtie_ExpressionSet (4389/18/2)
#        Input object 2: downsized_AT_reads_tophat_AlignmentSet_cufflinks_ExpressionSet (4389/45/1)
#        """
#        appdev_rnaseq_exprset_obj_ref = '4389/18/2'
#        appdev_rnaseq_exprset_obj_name = 'downsized_AT_reads_hisat2_AlignmentSet_stringtie_ExpressionSet'
#
#        ci_rnaseq_exprset_obj_ref = '23165/2/1'
#        ci_rnaseq_exprset_obj_name = 'downsized_AT_reads_hisat2_AlignmentSet_stringtie_ExpressionSet'
#
#        self.get_expr_matrix_success(appdev_rnaseq_exprset_obj_ref, 'ci_rnaseq_exprset_exprmat_output')
#
#    @unittest.skip("skipped test_get_expr_matrix_setapi_exprset_success")
#    def test_get_expr_matrix_setapi_exprset_success(self):
#
#        appdev_kbasesets_exprset_ref = '2409/391/13'
#
#        ci_kbasesets_exprset_obj_ref = '23165/19/1'
#        ci_kbasesets_exprset_obj_name = 'extracted_sampleset_tophat_alignment_set_expression_set'
#
#        self.get_expr_matrix_success(appdev_kbasesets_exprset_ref, 'setapi_exprset_exprmat_output')
#
#
#    def fail_getExprMat(self, params, error, exception=ValueError, do_startswith=False):

#        test_name = inspect.stack()[1][3]
#        print('\n*** starting expected get Expression Matrix fail test: ' + test_name + ' **********************')
#
#        with self.assertRaises(exception) as context:
#            self.getImpl().get_expressionMatrix(self.ctx, params)
#        if do_startswith:
#            self.assertTrue(str(context.exception.message).startswith(error),
#                            "Error message {} does not start with {}".format(
#                                str(context.exception.message),
#                                error))
#        else:
#            self.assertEqual(error, str(context.exception.message))
#
#    def test_getExprMat_fail_no_ws_name(self):
#        self.fail_getExprMat(
#            {
#                'expressionset_ref': '1/1/1',
#                'output_obj_name': 'test_exprMatrix'
#            },
#            '"workspace_name" parameter is required, but missing')
#
#    def test_getExprMat_fail_no_obj_name(self):
#        self.fail_getExprMat(
#            {
#                'workspace_name': self.getWsName(),
#                'expressionset_ref': '1/1/1'
#            },
#            '"output_obj_name" parameter is required, but missing')
#
#    def test_getExprMat_fail_no_exprset_ref(self):
#        self.fail_getExprMat(
#            {
#                'workspace_name': self.getWsName(),
#                'output_obj_name': 'test_exprMatrix'
#            },
#            '"expressionset_ref" parameter is required, but missing')
#
#    def test_getExprMat_fail_bad_wsname(self):
#        self.fail_getExprMat(
#            {
#                'workspace_name': '&bad',
#                'expressionset_ref': '1/1/1',
#                'output_obj_name': 'test_exprMatrix'
#            },
#            'Illegal character in workspace name &bad: &')
#
#    def test_getExprMat_fail_non_existant_wsname(self):
#        self.fail_getExprMat(
#            {
#                'workspace_name': '1s',
#                'expressionset_ref': '1/1/1',
#                'output_obj_name': 'test_exprMatrix'
#            },
#            'No workspace with name 1s exists')
#
#    def test_getExprMat_fail_non_expset_ref(self):
#        self.fail_getExprMat(
#            {
#                'workspace_name': self.getWsName(),
#                'expressionset_ref': self.genome_ref,
#                'output_obj_name': 'test_exprMatrix'
#            },
#            'expressionset_ref should be of type KBaseRNASeq.RNASeqExpressionSet ' +
#            'or KBaseSets.ExpressionSet', exception=TypeError)


