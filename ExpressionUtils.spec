/*
A KBase module: ExpressionUtils
*/

/**
    A KBase module: ExpressionUtils

    This module is intended for use by Assemblers to upload RNASeq Expression files
    (gtf, fpkm and ctab). The expression files are uploaded as a single compressed file.
    This module also generates expression levels and tpm expression levels from the uploaded
    files and saves them in the workspace object. Once uploaded, the expression files can be
    downloaded in the specified directory.
    **/

module ExpressionUtils {

   /* A boolean - 0 for false, 1 for true.
       @range (0, 1)
   */

    typedef int boolean;

   /**    Required input parameters for uploading a reads expression data

        string   destination_ref        -   object reference of expression data.
                                            The object ref is 'ws_name_or_id/obj_name_or_id'
                                            where ws_name_or_id is the workspace name or id
                                            and obj_name_or_id is the object name or id

        string   source_dir             -   directory with the files to be uploaded
        string   assembly_or_genome_ref -   workspace object ref of assembly or genome
                                            annotation that was used to build the alignment
        string   annotation_ref         -   annotation ref
        mapping  mapped_alignment       -   mapping of read_lib_ref and alignment_ref
        string   condition            	-
        string   tool_used              -   stringtie or  cufflinks
        string   tool_version           -
    **/

    typedef structure {

        string   destination_ref;
        string   source_dir;
        string   assembly_or_genome_ref;
        string   annotation_ref;
        mapping<string read_lib_ref, string alignment_ref>  mapped_alignment;
        string   condition;
        string   tool_used;
        string   tool_version;

        mapping<string opt_name, string opt_value> tool_opts;  /* Optional */

        int      data_quality_level;    /*  Optional */
        float    original_median;       /*  Optional */

        string   description;           /*  Optional */
        string   platform;              /*  Optional */
        string   source;                /*  Optional */
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
        string source_ref 	-       object reference of expression source. The
                                    object ref is 'ws_name_or_id/obj_name_or_id'
                                    where ws_name_or_id is the workspace name or id
                                    and obj_name_or_id is the object name or id
    **/


    typedef structure {
        string      source_ref;
    } DownloadExpressionParams;

    /**  The output of the download method.  **/

    typedef structure {
        string    ws_id;                /* source */
        string    destination_dir;      /* directory containing all the downloaded files  */
    } DownloadExpressionOutput;

    /** Downloads expression **/

    funcdef download_expression(DownloadExpressionParams params)
                       returns (DownloadExpressionOutput)
                       authentication required;

    /**
        Required input parameters for exporting expression

        string   source_ref 	-   object reference of alignment source. The
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
