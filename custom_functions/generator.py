def generator(input_event=None, **kwargs):
    """
    Args:
        input_event (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        url (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    raw = kwargs.get("input_event")
 
    outputs["url"] = "DEBUG_" + str(raw)

    return outputs