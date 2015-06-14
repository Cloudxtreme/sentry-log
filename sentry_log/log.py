from __future__ import absolute_import

__all__ = ('Log',)

from django.utils.translation import ugettext as _
from sentry.interfaces.base import Interface
from sentry.web.helpers import render_to_string
import itertools, datetime

class Log(Interface):
    @classmethod
    def to_python(cls, data):
        data = data.copy()
        kwargs = {
            'commit_id': data.pop('commit_id'),
            'version': data.pop('version'),
            'assets': data.pop('assets'),
            'entries': data.pop('entries'),
        }

        return cls(**kwargs)

    def __init__(self, commit_id=None, version=None, assets=None, entries=None, **kwargs):
        super(Log, self).__init__()

        self.commit_id = commit_id
        self.version = version
        self.assets = assets
        self.entries = entries

        for (i, item) in enumerate(self.entries):
            self.entries[i]["date"] = datetime.datetime.fromtimestamp(item["date"] / 1000)

    def get_api_context(self):
        return {
            'commit_id': self.commit_id,
            'version':   self.version,
            'assets':    self.assets,
            'entries':   self.entries,
        }

    def get_path(self):
        return 'sentry_log.Log'

    def get_hash(self):
        return []

    def get_context(self):
        return {
            'log_commit_id': self.commit_id,
            'log_version':   self.version,
            'log_assets':    self.assets,
            'log_entries':   self.entries,
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

    def to_email_html(self, event, is_public=False, **kwargs):
        return render_to_string('sentry_log/log.html', {
            'is_public': is_public,
            'event':     event,
            'commit_id': self.commit_id,
            'version':   self.version,
            'assets':    self.assets,
            'entries':   self.entries,
        })