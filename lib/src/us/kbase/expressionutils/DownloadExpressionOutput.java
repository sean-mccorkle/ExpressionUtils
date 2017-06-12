
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
 * <p>Original spec-file type: DownloadExpressionOutput</p>
 * <pre>
 * *  The output of the download method.  *
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "ws_id",
    "destination_dir"
})
public class DownloadExpressionOutput {

    @JsonProperty("ws_id")
    private String wsId;
    @JsonProperty("destination_dir")
    private String destinationDir;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("ws_id")
    public String getWsId() {
        return wsId;
    }

    @JsonProperty("ws_id")
    public void setWsId(String wsId) {
        this.wsId = wsId;
    }

    public DownloadExpressionOutput withWsId(String wsId) {
        this.wsId = wsId;
        return this;
    }

    @JsonProperty("destination_dir")
    public String getDestinationDir() {
        return destinationDir;
    }

    @JsonProperty("destination_dir")
    public void setDestinationDir(String destinationDir) {
        this.destinationDir = destinationDir;
    }

    public DownloadExpressionOutput withDestinationDir(String destinationDir) {
        this.destinationDir = destinationDir;
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
        return ((((((("DownloadExpressionOutput"+" [wsId=")+ wsId)+", destinationDir=")+ destinationDir)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
