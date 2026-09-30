def test_2(url=None, **kwargs):
    """
    Args:
        url
    
    Returns a JSON-serializable object that implements the configured data paths:
        target_url
    """
    ############################ Custom Code Goes Below This Line #################################
    
def build_http_request(url):
    # Remove spaces from the beginning/end of the URL
    target_url = url.strip()

    # Basic validation
    if not target_url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    return {
        "target_url": target_url,
         "method": "GET"
           }