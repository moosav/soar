def generator(artifact_data=None, **kwargs):
    """
    Args:
        artifact_data
    
    Returns a JSON-serializable object that implements the configured data paths:
        url
    """
    ############################ Custom Code Goes Below This Line #################################
    
    import re

    outputs = {}

    data = kwargs.get("artifact_data")

    if data:
        match = re.search(r'https?://[^\s"\']+', str(data))

        if match:
                outputs["url"] = match.group(0)
        else:
             outputs["url"] = ""
    else:
        outputs["url"] = ""

    return outputs