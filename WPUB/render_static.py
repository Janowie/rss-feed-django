from django.http import HttpRequest
from .views import test_render


def render_static():
    fake_request = HttpRequest()
    fake_request.method = 'POST'
    fake_request.POST['url'] = "https://www.sme.sk/rss-title"

    r = test_render(fake_request)

    return r


if __name__ == '__main__':
    render_static()