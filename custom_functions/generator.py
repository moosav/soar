def generator(url_input=None, **kwargs):
    """
    Args:
        url_input
    
    Returns a JSON-serializable object that implements the configured data paths:
        url (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    value = kwargs.get("url_input")

    if value is not None:
        outputs["url"] = str(value)
    else:
        outputs["url"] = ""


    return outputs