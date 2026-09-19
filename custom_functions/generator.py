def generator(artifact_data=None, **kwargs):
    """
    Args:
        artifact_data
    
    Returns a JSON-serializable object that implements the configured data paths:
        url
    """
    ############################ Custom Code Goes Below This Line #################################
    
    outputs = {}

    data = kwargs.get("artifact_data")

    outputs["url"] = str(data)

    return outputs