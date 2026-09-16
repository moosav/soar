def IPM_2(input_event=None, **kwargs):
    """
    Args:
        input_event (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity (CEF type: *): List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}
    outputs["severity"] = str(kwargs)
    return outputs