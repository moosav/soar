def IPM_2(event_message=None, **kwargs):
    """
    Args:
        event_message (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        severity_list: List of supported event severity values
    """
    ############################ Custom Code Goes Below This Line #################################
    severity_map = {
        "0": "Emergency",
        "1": "Alert",
        "2": "Critical",
        "3": "Error",
        "4": "Warning",
        "5": "Notification",
        "6": "Informational",
        "7": "Debugging"
    }

    severity = ""
    severity_name = ""

    if "-" in event_message:
        parts = event_message.split("-")

        if len(parts) >= 2:
            severity = parts[1].split(":")[0]

            if severity in severity_map:
                severity_name = severity_map[severity]

    outputs = {
        "severity": severity,
        "severity_name": severity_name
    }

    return outputs