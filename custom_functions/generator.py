def generator(url_input=None, **kwargs):
    """
    Args:
        url_input
    
    Returns a JSON-serializable object that implements the configured data paths:
        test_output (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}
    outputs["test_output"] = repr(kwargs)
    return outputs