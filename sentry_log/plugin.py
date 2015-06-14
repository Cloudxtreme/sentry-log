import sentry_log
from sentry.plugins import Plugin

class LogPlugin(Plugin):
    title = 'Lavatrace Log'
    slug = 'lavatrace-log'
    description = 'A plugin that adds an interface sent by the Lavatrace API'
    version = sentry_log.VERSION

    author = 'Piotr Zduniak'
    author_url = 'https://github.com/lavab/sentry-log'

    def widget(self, request, group, **kwargs):
        pass