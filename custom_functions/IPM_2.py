def IPM_2(**kwargs):
    """
    Returns a JSON-serializable object that implements the configured data paths:
        json_output: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    outputs = {}

    severity = str(kwargs.get("input_event", ""))

    outputs["json_output"] = json.dumps({
    "severity": severity
})

    return outputs