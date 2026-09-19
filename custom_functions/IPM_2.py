def IPM_2(input_event=None, **kwargs):
    """
    Args:
        input_event (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    raw = kwargs.get("input_event")

    outputs["severity"] = "DEBUG_" + repr(raw)


    return outputs