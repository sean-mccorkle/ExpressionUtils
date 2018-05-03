
package us.kbase.expressionutils;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import us.kbase.kbasefeaturevalues.ExpressionMatrix;


/**
 * <p>Original spec-file type: getEnhancedFEMOutput</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "enhanced_FEM"
})
public class GetEnhancedFEMOutput {

    /**
     * <p>Original spec-file type: ExpressionMatrix</p>
     * <pre>
     * A wrapper around a FloatMatrix2D designed for simple matricies of Expression
     * data.  Rows map to features, and columns map to conditions.  The data type 
     * includes some information about normalization factors and contains
     * mappings from row ids to features and col ids to conditions.
     * description - short optional description of the dataset
     * type - ? level, ratio, log-ratio
     * scale - ? probably: raw, ln, log2, log10
     * col_normalization - mean_center, median_center, mode_center, zscore
     * row_normalization - mean_center, median_center, mode_center, zscore
     * feature_mapping - map from row_id to feature id in the genome
     * data - contains values for (feature,condition) pairs, where 
     *     features correspond to rows and conditions are columns
     *     (ie data.values[feature][condition])
     * @optional description row_normalization col_normalization
     * @optional genome_ref feature_mapping conditionset_ref condition_mapping report
     * @metadata ws type
     * @metadata ws scale
     * @metadata ws row_normalization
     * @metadata ws col_normalization
     * @metadata ws genome_ref as Genome
     * @metadata ws conditionset_ref as ConditionSet
     * @metadata ws length(data.row_ids) as feature_count
     * @metadata ws length(data.col_ids) as condition_count
     * </pre>
     * 
     */
    @JsonProperty("enhanced_FEM")
    private ExpressionMatrix enhancedFEM;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    /**
     * <p>Original spec-file type: ExpressionMatrix</p>
     * <pre>
     * A wrapper around a FloatMatrix2D designed for simple matricies of Expression
     * data.  Rows map to features, and columns map to conditions.  The data type 
     * includes some information about normalization factors and contains
     * mappings from row ids to features and col ids to conditions.
     * description - short optional description of the dataset
     * type - ? level, ratio, log-ratio
     * scale - ? probably: raw, ln, log2, log10
     * col_normalization - mean_center, median_center, mode_center, zscore
     * row_normalization - mean_center, median_center, mode_center, zscore
     * feature_mapping - map from row_id to feature id in the genome
     * data - contains values for (feature,condition) pairs, where 
     *     features correspond to rows and conditions are columns
     *     (ie data.values[feature][condition])
     * @optional description row_normalization col_normalization
     * @optional genome_ref feature_mapping conditionset_ref condition_mapping report
     * @metadata ws type
     * @metadata ws scale
     * @metadata ws row_normalization
     * @metadata ws col_normalization
     * @metadata ws genome_ref as Genome
     * @metadata ws conditionset_ref as ConditionSet
     * @metadata ws length(data.row_ids) as feature_count
     * @metadata ws length(data.col_ids) as condition_count
     * </pre>
     * 
     */
    @JsonProperty("enhanced_FEM")
    public ExpressionMatrix getEnhancedFEM() {
        return enhancedFEM;
    }

    /**
     * <p>Original spec-file type: ExpressionMatrix</p>
     * <pre>
     * A wrapper around a FloatMatrix2D designed for simple matricies of Expression
     * data.  Rows map to features, and columns map to conditions.  The data type 
     * includes some information about normalization factors and contains
     * mappings from row ids to features and col ids to conditions.
     * description - short optional description of the dataset
     * type - ? level, ratio, log-ratio
     * scale - ? probably: raw, ln, log2, log10
     * col_normalization - mean_center, median_center, mode_center, zscore
     * row_normalization - mean_center, median_center, mode_center, zscore
     * feature_mapping - map from row_id to feature id in the genome
     * data - contains values for (feature,condition) pairs, where 
     *     features correspond to rows and conditions are columns
     *     (ie data.values[feature][condition])
     * @optional description row_normalization col_normalization
     * @optional genome_ref feature_mapping conditionset_ref condition_mapping report
     * @metadata ws type
     * @metadata ws scale
     * @metadata ws row_normalization
     * @metadata ws col_normalization
     * @metadata ws genome_ref as Genome
     * @metadata ws conditionset_ref as ConditionSet
     * @metadata ws length(data.row_ids) as feature_count
     * @metadata ws length(data.col_ids) as condition_count
     * </pre>
     * 
     */
    @JsonProperty("enhanced_FEM")
    public void setEnhancedFEM(ExpressionMatrix enhancedFEM) {
        this.enhancedFEM = enhancedFEM;
    }

    public GetEnhancedFEMOutput withEnhancedFEM(ExpressionMatrix enhancedFEM) {
        this.enhancedFEM = enhancedFEM;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((("GetEnhancedFEMOutput"+" [enhancedFEM=")+ enhancedFEM)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
