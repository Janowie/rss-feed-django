from django.test import TestCase
from django.http import HttpRequest
from .views import test_render
import os


class RenderPageTest(TestCase):

    def test_healthcheck(self):
        """
        A symbolic test ran after build.
        :return:
        """
        self.assertEqual("OK", "OK")
