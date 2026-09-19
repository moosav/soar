def generator(artifact_data=None, **kwargs):
    """
    Args:
        artifact_data (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        url (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    outputs["url"] = "TEST"
    outputs["debug"] = repr(kwargs)

    return outputs