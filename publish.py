from camplight import Request, Campfire
from django.utils.translation import ugettext_lazy as _
from forum.actions import AskAction, AnswerAction, CommentAction
from forum.models import Question
from forum.settings import APP_URL

from settings import CAMPFIRE_URL, CAMPFIRE_TOKEN, CAMPFIRE_ROOM


def enabled():
    return len(CAMPFIRE_URL) and len(CAMPFIRE_TOKEN) and len(CAMPFIRE_ROOM)


def speak(message):
	request = Request(str(CAMPFIRE_URL), str(CAMPFIRE_TOKEN))
	campfire = Campfire(request)
	room = campfire.room(str(CAMPFIRE_ROOM))
	room.speak(unicode(message))


def full_app_url(url):
	return APP_URL + url


def question_posted(action, new):
    if not enabled():
        return
	question = action.node
	speak(_('New question: %(headline)s - %(url)s' % {
            'headline': question.headline,
            'url': full_app_url(question.get_absolute_url())
            }))


def answer_posted(action, new):
    if not enabled():
        return
	answer = action.node
	question = answer.question
	speak(_('New answer posted for question: %(headline)s - %(url)s' % {
		'headline': question.headline,
        'url': full_app_url(question.get_absolute_url())
        }))


AskAction.hook(question_posted)
AnswerAction.hook(answer_posted)
