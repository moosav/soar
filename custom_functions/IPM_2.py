def IPM_2(input_event=None, **kwargs):
    """
    Args:
        input_event
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}
    outputs["severity"] = str(kwargs.get("input_event", ""))
    return outputs