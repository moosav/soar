def generator(url_input=None, **kwargs):
    """
    Args:
        url_input
    
    Returns a JSON-serializable object that implements the configured data paths:
        url (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}
    outputs["url"] = str(url_input)
    return outputs