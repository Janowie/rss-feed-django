from django.core.management.base import BaseCommand, CommandError
from django.http import HttpRequest
from ...views import test_render


class Command(BaseCommand):
    help = "Use this command to render static page with articles."

    def handle(self, *args, **options):
        try:
            url = options.get('url') or "https://www.sme.sk/rss-title"

            fake_request = HttpRequest()
            fake_request.method = 'POST'
            fake_request.POST['url'] = url

            r = test_render(fake_request)
            self.stdout.write(r)
        except:
            raise CommandError("Something went wrong.")