
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
 *         string   destination_ref                -          object reference of expression data.
 *                                             The object ref is 'ws_name_or_id/obj_name_or_id'
 *                                             where ws_name_or_id is the workspace name or id
 *                                             and obj_name_or_id is the object name or id
 *         string   source_dir                        -       Source: directory with the files to be uploaded
 *         string   condition                    -
 *         string   assembly_or_genome_ref -          ?? workspace object ref of assembly or genome
 *         annotation that was used to build the alignment
 *             string annotation_id                    -        ?? is this the same as assembly ref ??
 *             mapping mapped_alignment            -        ?? is this alignment_ref?
 *     *
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "destination_ref",
    "source_dir",
    "condition",
    "assembly_or_genome_ref",
    "annotation_ref",
    "mapped_rnaseq_alignment",
    "data_quality_level",
    "original_median",
    "tool_used",
    "tool_version",
    "tool_opts",
    "description",
    "platform",
    "source",
    "external_source_date",
    "processing_comments"
})
public class UploadExpressionParams {

    @JsonProperty("destination_ref")
    private java.lang.String destinationRef;
    @JsonProperty("source_dir")
    private java.lang.String sourceDir;
    @JsonProperty("condition")
    private java.lang.String condition;
    @JsonProperty("assembly_or_genome_ref")
    private java.lang.String assemblyOrGenomeRef;
    @JsonProperty("annotation_ref")
    private java.lang.String annotationRef;
    @JsonProperty("mapped_rnaseq_alignment")
    private Map<String, String> mappedRnaseqAlignment;
    @JsonProperty("data_quality_level")
    private Long dataQualityLevel;
    @JsonProperty("original_median")
    private Double originalMedian;
    @JsonProperty("tool_used")
    private java.lang.String toolUsed;
    @JsonProperty("tool_version")
    private java.lang.String toolVersion;
    @JsonProperty("tool_opts")
    private Map<String, String> toolOpts;
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

    @JsonProperty("condition")
    public java.lang.String getCondition() {
        return condition;
    }

    @JsonProperty("condition")
    public void setCondition(java.lang.String condition) {
        this.condition = condition;
    }

    public UploadExpressionParams withCondition(java.lang.String condition) {
        this.condition = condition;
        return this;
    }

    @JsonProperty("assembly_or_genome_ref")
    public java.lang.String getAssemblyOrGenomeRef() {
        return assemblyOrGenomeRef;
    }

    @JsonProperty("assembly_or_genome_ref")
    public void setAssemblyOrGenomeRef(java.lang.String assemblyOrGenomeRef) {
        this.assemblyOrGenomeRef = assemblyOrGenomeRef;
    }

    public UploadExpressionParams withAssemblyOrGenomeRef(java.lang.String assemblyOrGenomeRef) {
        this.assemblyOrGenomeRef = assemblyOrGenomeRef;
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

    @JsonProperty("mapped_rnaseq_alignment")
    public Map<String, String> getMappedRnaseqAlignment() {
        return mappedRnaseqAlignment;
    }

    @JsonProperty("mapped_rnaseq_alignment")
    public void setMappedRnaseqAlignment(Map<String, String> mappedRnaseqAlignment) {
        this.mappedRnaseqAlignment = mappedRnaseqAlignment;
    }

    public UploadExpressionParams withMappedRnaseqAlignment(Map<String, String> mappedRnaseqAlignment) {
        this.mappedRnaseqAlignment = mappedRnaseqAlignment;
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
        return ((((((((((((((((((((((((((((((((((("UploadExpressionParams"+" [destinationRef=")+ destinationRef)+", sourceDir=")+ sourceDir)+", condition=")+ condition)+", assemblyOrGenomeRef=")+ assemblyOrGenomeRef)+", annotationRef=")+ annotationRef)+", mappedRnaseqAlignment=")+ mappedRnaseqAlignment)+", dataQualityLevel=")+ dataQualityLevel)+", originalMedian=")+ originalMedian)+", toolUsed=")+ toolUsed)+", toolVersion=")+ toolVersion)+", toolOpts=")+ toolOpts)+", description=")+ description)+", platform=")+ platform)+", source=")+ source)+", externalSourceDate=")+ externalSourceDate)+", processingComments=")+ processingComments)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
