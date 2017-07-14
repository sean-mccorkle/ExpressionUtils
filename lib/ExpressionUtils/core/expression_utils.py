import math

import logging

import time

import sys


def get_logger():
    logger = logging.getLogger('ExpressionUtils.core.expression_utils')
    logger.setLevel(logging.INFO)
    streamHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s")
    formatter.converter = time.gmtime
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    logger.info("Logger was set")
    return logger


class ExpressionUtils:
    """
     Constains a set of functions for expression levels calculations.
    """

    def __init__(self, config, logger=None):
        self.config = config
        if logger is not None:
            self.logger = logger
        else:
            self.logger = get_logger()

    def get_expression_levels(self, filepath):
        """
         Returns FPKM and TPM expression levels.
         # (see discussion @ https://www.biostars.org/p/160989/)

        :param filename: An FPKM tracking file
        :return: fpkm and tpm expression levels as dictionaries
        """
        fpkm_dict = {}
        tpm_dict = {}
        gene_col = 0

        # get FPKM col index
        try:
            with open(filepath, 'r') as file:
                header = file.readline()
                fpkm_col = header.split('\t').index('FPKM')
                self.logger.info('Using FPKM at col '+str(fpkm_col)+' in '+str(filepath))
        except:
            self.logger.error('Unable to find an FPKM column in the specified file: '+str(filepath))

        sum_fpkm = 0.0
        with open(filepath) as f:
            next(f)
            for line in f:
                larr = line.split("\t")
                gene_id = larr[gene_col]
                if gene_id != "":
                    fpkm = float(larr[fpkm_col])
                    sum_fpkm = sum_fpkm + fpkm
                    fpkm_dict[gene_id] = math.log(fpkm + 1, 2)
                    tpm_dict[gene_id] = fpkm

        for g in tpm_dict:
            tpm_dict[g] = math.log((tpm_dict[g] / sum_fpkm) * 1e6 + 1, 2)

        return fpkm_dict, tpm_dict
