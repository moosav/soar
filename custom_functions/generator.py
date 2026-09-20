def generator(**kwargs):
    """
    Returns a JSON-serializable object that implements the configured data paths:
        url (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    outputs["url"] = kwargs.get("articat")

    return outputs