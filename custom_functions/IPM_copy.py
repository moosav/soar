def IPM_copy(**kwargs):
    """
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
   
    """
    custom_function
    """
    outputs = {}
    
    # کد شما باید اینجا قرار بگیرد:
    if not severity:
        severity = []
    elif not isinstance(severity, list):
        severity = [severity]
    
    # گرفتن مقادیر یکتا و حذف موارد خالی
    unique_severities = list({str(s).strip().lower() for s in severity if s})
    
    # تنظیم دقیق خروجی بر اساس Data Path (result.severity)
    outputs['result'] = {'severity': unique_severities}
    
    return outputs
