def Geberator_2(severity_input=None, url_input=None, **kwargs):
    """
    Args:
        severity_input
        url_input
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity
        url
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    
    outputs["url"] = str(url_input)
    outputs["severity"] = str(severity_input)
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
