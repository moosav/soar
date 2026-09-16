def IPM_2(artifact_input=None, **kwargs):
    """
    Args:
        artifact_input (CEF type: phantom artifact id)
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    severity = str(kwargs.get("input_event", ""))

    outputs["severity"] = severity

    return outputs