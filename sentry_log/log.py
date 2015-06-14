from django.utils.translation import ugettext as _
from sentry.interfaces.base import Interface
from sentry.web.helpers import render_to_string
import itertools

class Log(Interface):
    attrs = (
        'commit_id',
        'version',
        'assets',
        'entries',
    )

    def __init__(self, commit_id=None, version=None, assets=None, entries=None, **kwargs):
        super(Log, self).__init__()

        self.commit_id = commit_id
        self.version = version
        self.assets = assets
        self.entries = entries

    def serialize(self):
        return {
            'commit_id': self.commit_id,
            'version':   self.version,
            'assets':    self.assets,
            'entries':   self.entries,
        }

    def get_search_context(self, event):
        return {
            'text': [self.commit_id, self.version, self.assets, self.entries] +
                list(itertools.chain(*[[
                    f.type,
                    f.message
                ] for f in self.entries])), # We could add search by context etc.
        }

    def to_html(self, event, is_public=False, **kwargs):
        return render_to_string('sentry_log/log.html', {
            'is_public': is_public,
            'event':     event,
            'commit_id': self.commit_id,
            'version':   self.version,
            'assets':    self.assets,
            'entries':   self.entries,
        })

    def get_title(self):
        return _('Lavatrace log')