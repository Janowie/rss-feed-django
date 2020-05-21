from django.test import TestCase
from django.http import HttpRequest
from urllib.request import urlopen
from .views import test_render
import os


class RenderPageTest(TestCase):

    def test_healthcheck(self):
        self.assertEqual("OK", "OK")

    def test_render(self):
        fp = os.path.join(os.path.dirname(__file__), 'rendered_pages/index.html')
        try:
            fake_request = HttpRequest()
            fake_request.method = 'POST'
            fake_request.POST['url'] = "https://www.sme.sk/rss-title"

            r = test_render(fake_request)

            with open(fp, 'w') as static_file:
                static_file.write(r)

        except:
            self.fail("render failed")
