import os
import logging
import uuid
from script_utils import runProgram, log
import errno
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil
from DataFileUtil.DataFileUtilClient import DataFileUtil
from Workspace.WorkspaceClient import Workspace as Workspace

class GFFUtils:
    """
    A wrapper to the jhu.edu's gff utilities. See
    http://ccb.jhu.edu/software/stringtie/gff.shtml
    """

    def __init__(self, config, logger=None):
        self.config = config
        self.logger = logger
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.scratch = os.path.join(config['scratch'], str(uuid.uuid4()))
        self.token = os.environ['KB_AUTH_TOKEN']
        self.ws_url = config['workspace-url']
        self._mkdir_p(self.scratch)
        pass

    def _mkdir_p(self, path):
        """
        _mkdir_p: make directory for given path
        """
        if not path:
            return
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def convert_genome_to_gtf(self, genome_ref, target_dir):
        """
        Converts the specified kbase genome object to gff file format

        :param genome_ref: workspace reference to kbase genome object
        :param target_dir: directory to which to write the output gff file.
        :return: path to the gff file. The gff file has the same name as the specified genome object
        """
        gfu = GenomeFileUtil(self.callback_url)
        gtf_file_path = gfu.genome_to_gff({'genome_ref': genome_ref,
                                           'is_gtf': 1,
                                           'target_dir': target_dir})['file_path']

        return gtf_file_path

    def create_gtf_annotation_from_genome(self, genome_ref, workspace_name):
        """
        Create a workspace reference of a kbase genome annotation object from the specified
        kbase genome object.

        See https://ci.kbase.us/#spec/type/KBaseRNASeq.GFFAnnotation

        :param genome_ref: workspace reference to kbase genome object
        :return: Kbase genome annotation reference.
        """
        log('start saving GffAnnotation object')

        dfu = DataFileUtil(self.callback_url)

        if isinstance(workspace_name, int) or workspace_name.isdigit():
            workspace_id = workspace_name
        else:
            workspace_id = dfu.ws_name_to_id(workspace_name)

        ws = Workspace(self.ws_url, token=self.token)
        genome_data = ws.get_objects2({'objects':
                                       [{'ref': genome_ref}]})['data'][0]['data']
        genome_name = genome_data.get('id')
        genome_scientific_name = genome_data.get('scientific_name')
        gtf_annotation_name = genome_name + "_GTF_Annotation"

        gtf_file_path = self.convert_genome_to_gtf(genome_ref, self.scratch)

        file_to_shock_result = dfu.file_to_shock({'file_path': gtf_file_path,
                                                  'make_handle': True})
        gtf_annotation_data = {'handle': file_to_shock_result['handle'],
                               'size': file_to_shock_result['size'],
                               'genome_id': genome_ref,
                               'genome_scientific_name': genome_scientific_name}

        object_type = 'KBaseRNASeq.GFFAnnotation'

        save_object_params = {
            'id': workspace_id,
            'objects': [{
                'type': object_type,
                'data': gtf_annotation_data,
                'name': gtf_annotation_name
            }]
        }
        dfu_obj = dfu.save_objects(save_object_params)

        dfu_oi = dfu_obj[0]
        gtf_annotation_obj_ref = str(dfu_oi[6]) + '/' + str(dfu_oi[0]) + '/' + str(dfu_oi[4])

        return gtf_annotation_obj_ref
