def IPM_2(**kwargs):
    """
    Returns a JSON-serializable object that implements the configured data paths:
        severity_list: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    import json

    outputs = {}

    outputs["severity_list"] = [
        "informational",
        "low",
        "medium",
        "high",
        "critical"
    ]

    assert json.dumps(outputs)

    return outputs