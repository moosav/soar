def IPM_2(event_message=None, **kwargs):
    """
    Args:
        event_message (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity_list: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    outputs = {}

    outputs["severity_list"] = [
        "informational",
        "low",
        "medium",
        "high",
        "critical"
    ]

    return outputs