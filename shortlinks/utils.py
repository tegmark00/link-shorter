from config import settings


def get_ip_from_request(request):
    return request.META.get("HTTP_X_REAL_IP") or request.META.get('REMOTE_ADDR')


def get_host_from_request(request):
    return request.META.get('HTTP_HOST') or settings.WEBSITE_URL
