/*
A KBase module: ExpressionUtils
*/

/**
    A KBase module: ExpressionUtils

    This module is intended for use by Assemblers to upload RNASeq Expression files
    (gtf, fpkm and ctab). The expression files are uploaded as a single compressed file.
    Once uploaded, the expression can be downloaded in TODO file formats. This utility
    also generates expression levels and tpm expression levels **/

module ExpressionUtils {

   /* A boolean - 0 for false, 1 for true.
       @range (0, 1)
   */

    typedef int boolean;

   /**    Required input parameters for uploading a reads expression data

        string   destination_ref		-  	object reference of expression data.
                                            The object ref is 'ws_name_or_id/obj_name_or_id'
                                            where ws_name_or_id is the workspace name or id
                                            and obj_name_or_id is the object name or id

        string   source_dir		        -       Source: directory with the files to be uploaded
        string   condition            	-
        string   assembly_or_genome_ref -  	?? workspace object ref of assembly or genome
        annotation that was used to build the alignment
	    string annotation_id		    -	?? is this the same as assembly ref ??
	    mapping mapped_alignment	    -	?? is this alignment_ref?
    **/

    typedef structure {

        string  destination_ref;
        string  source_dir;
        string  condition;
        string  assembly_or_genome_ref;
        string  annotation_ref;
        mapping<string read_lib_ref, string alignment_ref> mapped_rnaseq_alignment;

        int     data_quality_level;		/*  Optional */
        float   original_median;		/*  Optional */

        string  tool_used;		        /*  Optional - stringtie or  cufflinks   */
        string  tool_version;		    /*  Optional */
        mapping<string opt_name, string opt_value> tool_opts;  /* Optional */

        string   description;		    /*  Optional */
        string   platform;		        /*  Optional */
        string   source;			    /*  Optional */
        string   external_source_date;	/*  Optional */
        string   processing_comments;	/*  Optional */

    }  UploadExpressionParams;


    /**     Output from upload expression    **/

    typedef structure {
        string   obj_ref;
     }  UploadExpressionOutput;

    /**  Uploads the expression  **/


    funcdef  upload_expression(UploadExpressionParams params)
                                   returns (UploadExpressionOutput)
                                   authentication required;
    /**
        Required input parameters for downloading expression
        string source_ref 	- 	    object reference of expression source. The
                                    object ref is 'ws_name_or_id/obj_name_or_id'
                                    where ws_name_or_id is the workspace name or id
                                    and obj_name_or_id is the object name or id
    **/


    typedef structure {
        string		source_ref;
        boolean	    downloadCTAB;	/* Optional - default is false */
        boolean	    downloadTPM;	/* Optional - default is false */
    } DownloadExpressionParams;

    /**  The output of the download method.  **/

    typedef structure {
        string    ws_id;    		    /* source */
        string    destination_dir;      /* directory containing all the downloaded files  */
    } DownloadExpressionOutput;

    /** Downloadsexpression files TODO …  **/

    funcdef download_expression(DownloadExpressionParams params)
                             returns (DownloadExpressionOutput)
                             authentication required;

    /**
        Required input parameters for exporting expression

        string   source_ref 	-  	object reference of alignment source. The
                                    object ref is 'ws_name_or_id/obj_name_or_id'
                                    where ws_name_or_id is the workspace name or id
                                    and obj_name_or_id is the object name or id
     **/

    typedef structure {
        string source_ref;   /* workspace object reference */
    } ExportParams;

    typedef structure {
        string shock_id;     /* shock id of file to export */
     } ExportOutput;
    /** Wrapper function for use by in-narrative downloaders to download expressions from shock **/


    funcdef export_expression(ExportParams params)
                     returns (ExportOutput output)
                     authentication required;
    };
