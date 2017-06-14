import os
import logging
import contig_id_mapping as c_mapping
from script_utils import runProgram, log
import traceback
from AssemblyUtil.AssemblyUtilClient import AssemblyUtil
from GenomeFileUtil.GenomeFileUtilClient import GenomeFileUtil

class GFFUtils:
    """
    A wrapper to the jhu.edu's gff utilities. See
    http://ccb.jhu.edu/software/stringtie/gff.shtml
    """

    def __init__(self, config, logger=None):
        self.config = config
        self.logger = logger
        pass

    def _prepare_paths(self, ifile, ipath, ofile, opath, iext, oext):
        """
        setup input and output file paths and extensions
        """
        if ipath is None:
            ipath = ''
        if opath is None:
            opath = ipath
        if ofile is None:
            if ifile[-4:] == iext:
                ofile = ifile[:-4] + oext
            else:
                ofile = ifile + oext
        ifile = os.path.join(ipath, ifile)
        ofile = os.path.join(opath, ofile)

        return ifile, ofile

    def convert_gff_to_gtf(self, ifile, ipath=None, ofile=None, opath=None):
        """
        Runs gffread converts the specified GFF3 file to a GTF2 format

        :param ifile: File path to a reference genome in GFF3 format
        :param ipath: path to reference genome. If None, ipath is set to current path
        :param ofile: GTF2 output filename. If None, ifile name is used with the
        extension '.gff3' (if any) replaced with '.gtf'
        :param opath: path to GTF2 output file. If None, ipath will be used

        :returns 0 if successful, else 1
        """
        log('Running gffread...', level=logging.INFO, logger=self.logger)

        # prepare input and output file paths
        ifile, ofile = self._prepare_paths(ifile, ipath, ofile, opath, '.gff3', '.gtf')

        # check if input file exists
        if not os.path.exists(ifile):
            raise RuntimeError(None, 'Input gff file does not exist: ' + str(ifile))

        try:
            gtf_args = " {0} -T -o {1}".format(ifile, ofile)
            log("Executing: gffread {0}".format(gtf_args), level=logging.INFO, logger=self.logger)
            rval = runProgram(logger=self.logger, progName="gffread", argStr=gtf_args)

            if rval['stderr'] != '':
                return 1

        except Exception as ex:
            log("Error executing gffread {0}. {1}".format(gtf_args, ex.message),
                logging.ERROR, self.logger)
            return 1

        return 0

    def create_gtf_annotation_from_genome(logger, ws_client, hs_client, urls, ws_id, genome_ref,
                                          genome_name, directory, token):
        ref = ws_client.get_object_subset(
            [{'ref': genome_ref, 'included': ['contigset_ref', 'assembly_ref']}])
        if 'contigset_ref' in ref[0]['data']:
            contig_id = ref[0]['data']['contigset_ref']
        elif 'assembly_ref' in ref[0]['data']:
            contig_id = ref[0]['data']['assembly_ref']
        if contig_id is None:
            raise ValueError(
                "Genome {0} object does not have reference to the assembly object".format(
                    genome_name))
        print contig_id
        logger.info("Generating GFF file from Genome")
        try:
            assembly = AssemblyUtil(urls['callback_url'])
            ret = assembly.get_assembly_as_fasta({'ref': contig_id})
            output_file = ret['path']
            mapping_filename = c_mapping.create_sanitized_contig_ids(output_file)
            os.remove(output_file)
            ## get the GFF
            genome = GenomeFileUtil(urls['callback_url'])
            ret = genome.genome_to_gff({'genome_ref': genome_ref})
            file_path = ret['file_path']
            c_mapping.replace_gff_contig_ids(file_path, mapping_filename, to_modified=True)
            gtf_ext = ".gtf"
            if not file_path.endswith(gtf_ext):
                gtf_path = os.path.join(directory, genome_name + ".gtf")
                gtf_cmd = " -E {0} -T -o {1}".format(file_path, gtf_path)
                try:
                    logger.info("Executing: gffread {0}".format(gtf_cmd))
                    cmdline_output = runProgram(None, "gffread", gtf_cmd, None,
                                                            directory)
                except Exception as e:
                    raise Exception(
                        "Error Converting the GFF file to GTF using gffread {0},{1}".format(gtf_cmd,
                                                                                            "".join(
                                                                                                traceback.format_exc())))
            else:
                logger.info("GTF handled by GAU")
                gtf_path = file_path
            logger.info("gtf file : " + gtf_path)
            if os.path.exists(gtf_path):
                annotation_handle = hs_client.upload(gtf_path)
                a_handle = {"handle": annotation_handle, "size": os.path.getsize(gtf_path),
                            'genome_id': genome_ref}
            ##Saving GFF/GTF annotation to the workspace
            res = ws_client.save_objects(
                {"workspace": ws_id,
                 "objects": [{
                     "type": "KBaseRNASeq.GFFAnnotation",
                     "data": a_handle,
                     "name": genome_name + "_GTF_Annotation",
                     "hidden": 1}
                 ]})
        except Exception as e:
            raise ValueError(
                "Generating GTF file from Genome Annotation object Failed :  {}".format(
                    "".join(traceback.format_exc())))
        return gtf_path

