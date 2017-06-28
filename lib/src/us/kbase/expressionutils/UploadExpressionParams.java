
package us.kbase.expressionutils;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: UploadExpressionParams</p>
 * <pre>
 * *    Required input parameters for uploading a reads expression data
 *         string   destination_ref        -   object reference of expression data.
 *                                             The object ref is 'ws_name_or_id/obj_name_or_id'
 *                                             where ws_name_or_id is the workspace name or id
 *                                             and obj_name_or_id is the object name or id
 *                                             
 *         string   source_dir             -   directory with the files to be uploaded
 *         string   alignment_ref          -   alignment workspace object reference
 *         string   tool_used              -   stringtie or cufflinks
 *         string   tool_version           -   version of the tool used
 *     *
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "destination_ref",
    "source_dir",
    "alignment_ref",
    "tool_used",
    "tool_version",
    "annotation_ref",
    "bam_file_path",
    "data_quality_level",
    "original_median",
    "description",
    "platform",
    "source",
    "external_source_date",
    "processing_comments",
    "tool_opts"
})
public class UploadExpressionParams {

    @JsonProperty("destination_ref")
    private java.lang.String destinationRef;
    @JsonProperty("source_dir")
    private java.lang.String sourceDir;
    @JsonProperty("alignment_ref")
    private java.lang.String alignmentRef;
    @JsonProperty("tool_used")
    private java.lang.String toolUsed;
    @JsonProperty("tool_version")
    private java.lang.String toolVersion;
    @JsonProperty("annotation_ref")
    private java.lang.String annotationRef;
    @JsonProperty("bam_file_path")
    private java.lang.String bamFilePath;
    @JsonProperty("data_quality_level")
    private Long dataQualityLevel;
    @JsonProperty("original_median")
    private Double originalMedian;
    @JsonProperty("description")
    private java.lang.String description;
    @JsonProperty("platform")
    private java.lang.String platform;
    @JsonProperty("source")
    private java.lang.String source;
    @JsonProperty("external_source_date")
    private java.lang.String externalSourceDate;
    @JsonProperty("processing_comments")
    private java.lang.String processingComments;
    @JsonProperty("tool_opts")
    private Map<String, String> toolOpts;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("destination_ref")
    public java.lang.String getDestinationRef() {
        return destinationRef;
    }

    @JsonProperty("destination_ref")
    public void setDestinationRef(java.lang.String destinationRef) {
        this.destinationRef = destinationRef;
    }

    public UploadExpressionParams withDestinationRef(java.lang.String destinationRef) {
        this.destinationRef = destinationRef;
        return this;
    }

    @JsonProperty("source_dir")
    public java.lang.String getSourceDir() {
        return sourceDir;
    }

    @JsonProperty("source_dir")
    public void setSourceDir(java.lang.String sourceDir) {
        this.sourceDir = sourceDir;
    }

    public UploadExpressionParams withSourceDir(java.lang.String sourceDir) {
        this.sourceDir = sourceDir;
        return this;
    }

    @JsonProperty("alignment_ref")
    public java.lang.String getAlignmentRef() {
        return alignmentRef;
    }

    @JsonProperty("alignment_ref")
    public void setAlignmentRef(java.lang.String alignmentRef) {
        this.alignmentRef = alignmentRef;
    }

    public UploadExpressionParams withAlignmentRef(java.lang.String alignmentRef) {
        this.alignmentRef = alignmentRef;
        return this;
    }

    @JsonProperty("tool_used")
    public java.lang.String getToolUsed() {
        return toolUsed;
    }

    @JsonProperty("tool_used")
    public void setToolUsed(java.lang.String toolUsed) {
        this.toolUsed = toolUsed;
    }

    public UploadExpressionParams withToolUsed(java.lang.String toolUsed) {
        this.toolUsed = toolUsed;
        return this;
    }

    @JsonProperty("tool_version")
    public java.lang.String getToolVersion() {
        return toolVersion;
    }

    @JsonProperty("tool_version")
    public void setToolVersion(java.lang.String toolVersion) {
        this.toolVersion = toolVersion;
    }

    public UploadExpressionParams withToolVersion(java.lang.String toolVersion) {
        this.toolVersion = toolVersion;
        return this;
    }

    @JsonProperty("annotation_ref")
    public java.lang.String getAnnotationRef() {
        return annotationRef;
    }

    @JsonProperty("annotation_ref")
    public void setAnnotationRef(java.lang.String annotationRef) {
        this.annotationRef = annotationRef;
    }

    public UploadExpressionParams withAnnotationRef(java.lang.String annotationRef) {
        this.annotationRef = annotationRef;
        return this;
    }

    @JsonProperty("bam_file_path")
    public java.lang.String getBamFilePath() {
        return bamFilePath;
    }

    @JsonProperty("bam_file_path")
    public void setBamFilePath(java.lang.String bamFilePath) {
        this.bamFilePath = bamFilePath;
    }

    public UploadExpressionParams withBamFilePath(java.lang.String bamFilePath) {
        this.bamFilePath = bamFilePath;
        return this;
    }

    @JsonProperty("data_quality_level")
    public Long getDataQualityLevel() {
        return dataQualityLevel;
    }

    @JsonProperty("data_quality_level")
    public void setDataQualityLevel(Long dataQualityLevel) {
        this.dataQualityLevel = dataQualityLevel;
    }

    public UploadExpressionParams withDataQualityLevel(Long dataQualityLevel) {
        this.dataQualityLevel = dataQualityLevel;
        return this;
    }

    @JsonProperty("original_median")
    public Double getOriginalMedian() {
        return originalMedian;
    }

    @JsonProperty("original_median")
    public void setOriginalMedian(Double originalMedian) {
        this.originalMedian = originalMedian;
    }

    public UploadExpressionParams withOriginalMedian(Double originalMedian) {
        this.originalMedian = originalMedian;
        return this;
    }

    @JsonProperty("description")
    public java.lang.String getDescription() {
        return description;
    }

    @JsonProperty("description")
    public void setDescription(java.lang.String description) {
        this.description = description;
    }

    public UploadExpressionParams withDescription(java.lang.String description) {
        this.description = description;
        return this;
    }

    @JsonProperty("platform")
    public java.lang.String getPlatform() {
        return platform;
    }

    @JsonProperty("platform")
    public void setPlatform(java.lang.String platform) {
        this.platform = platform;
    }

    public UploadExpressionParams withPlatform(java.lang.String platform) {
        this.platform = platform;
        return this;
    }

    @JsonProperty("source")
    public java.lang.String getSource() {
        return source;
    }

    @JsonProperty("source")
    public void setSource(java.lang.String source) {
        this.source = source;
    }

    public UploadExpressionParams withSource(java.lang.String source) {
        this.source = source;
        return this;
    }

    @JsonProperty("external_source_date")
    public java.lang.String getExternalSourceDate() {
        return externalSourceDate;
    }

    @JsonProperty("external_source_date")
    public void setExternalSourceDate(java.lang.String externalSourceDate) {
        this.externalSourceDate = externalSourceDate;
    }

    public UploadExpressionParams withExternalSourceDate(java.lang.String externalSourceDate) {
        this.externalSourceDate = externalSourceDate;
        return this;
    }

    @JsonProperty("processing_comments")
    public java.lang.String getProcessingComments() {
        return processingComments;
    }

    @JsonProperty("processing_comments")
    public void setProcessingComments(java.lang.String processingComments) {
        this.processingComments = processingComments;
    }

    public UploadExpressionParams withProcessingComments(java.lang.String processingComments) {
        this.processingComments = processingComments;
        return this;
    }

    @JsonProperty("tool_opts")
    public Map<String, String> getToolOpts() {
        return toolOpts;
    }

    @JsonProperty("tool_opts")
    public void setToolOpts(Map<String, String> toolOpts) {
        this.toolOpts = toolOpts;
    }

    public UploadExpressionParams withToolOpts(Map<String, String> toolOpts) {
        this.toolOpts = toolOpts;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((((((((((((((((((((((((((((("UploadExpressionParams"+" [destinationRef=")+ destinationRef)+", sourceDir=")+ sourceDir)+", alignmentRef=")+ alignmentRef)+", toolUsed=")+ toolUsed)+", toolVersion=")+ toolVersion)+", annotationRef=")+ annotationRef)+", bamFilePath=")+ bamFilePath)+", dataQualityLevel=")+ dataQualityLevel)+", originalMedian=")+ originalMedian)+", description=")+ description)+", platform=")+ platform)+", source=")+ source)+", externalSourceDate=")+ externalSourceDate)+", processingComments=")+ processingComments)+", toolOpts=")+ toolOpts)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
