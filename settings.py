from django.conf import settings as djsettings
from django.utils.translation import ugettext_lazy as _
from forum.settings.base import Setting, SettingSet


CAMPFIRE_SET = SettingSet(
    'campfire',
    _('Campfire Settings'),
    _('Announces new questions and answers on Campfire'),
    3000)


CAMPFIRE_URL = Setting('CAMPFIRE_URL', '', CAMPFIRE_SET, dict(
    label = _('URL of Campfire server'),
    help_text = _("eg. https://foobar.campfirenow.com/"),
    required = False
    ))


CAMPFIRE_TOKEN = Setting('CAMPFIRE_TOKEN', '', CAMPFIRE_SET, dict(
    label = _('Access token for Campfire user'),
    required = False
    ))


CAMPFIRE_ROOM = Setting('CAMPFIRE_ROOM', '', CAMPFIRE_SET, dict(
    label = _('Room to join'),
    required = False
    ))
