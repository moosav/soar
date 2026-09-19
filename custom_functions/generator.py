def generator(artifact=None, **kwargs):
    """
    Args:
        artifact (CEF type: url)
    
    Returns a JSON-serializable object that implements the configured data paths:
        url (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    outputs["url"] = kwargs.get("input_event")

    return outputs