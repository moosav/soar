def generator(artifact_data=None, **kwargs):
    """
    Args:
        artifact_data (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        url (CEF type: *)
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    artifact_id = kwargs.get("artifact_data")

    outputs["url"] = "ARTIFACT_ID=" + str(artifact_id)

    return outputs