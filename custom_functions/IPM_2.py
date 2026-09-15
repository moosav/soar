def IPM_2(input_event=None, **kwargs):
    """
    Args:
        input_event (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity (CEF type: sha1): List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    outputs["severity"] = kwargs.get("input_event", "")

    return outputs