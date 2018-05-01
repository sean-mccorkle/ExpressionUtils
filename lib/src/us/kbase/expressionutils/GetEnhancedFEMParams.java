
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
 * <p>Original spec-file type: getEnhancedFEMParams</p>
 * <pre>
 * *
 * Input parameters and method for getting the enhanced Filtered Expresion Matrix
 * for viewing
 *     *
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "fem_object_ref"
})
public class GetEnhancedFEMParams {

    @JsonProperty("fem_object_ref")
    private String femObjectRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("fem_object_ref")
    public String getFemObjectRef() {
        return femObjectRef;
    }

    @JsonProperty("fem_object_ref")
    public void setFemObjectRef(String femObjectRef) {
        this.femObjectRef = femObjectRef;
    }

    public GetEnhancedFEMParams withFemObjectRef(String femObjectRef) {
        this.femObjectRef = femObjectRef;
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
        return ((((("GetEnhancedFEMParams"+" [femObjectRef=")+ femObjectRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
