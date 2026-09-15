def IPM_2(input_severity=None, **kwargs):
    """
    Args:
        input_severity (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    outputs["severity"] = kwargs

    return outputs