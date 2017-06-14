import os
import logging
from script_utils import runProgram, log


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
