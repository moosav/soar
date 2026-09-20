def generator(url_input=None, **kwargs):
    """
    Args:
        url_input
    
    Returns a JSON-serializable object that implements the configured data paths:
        test_output (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    value = kwargs.get("url_input")

    outputs["test_output"] = str(value)


    return outputs