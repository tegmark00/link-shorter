

def get_ip_from_request(request):
    print(request.META)
    return request.META.get("HTTP_X_REAL_IP") or request.META.get('REMOTE_ADDR')
