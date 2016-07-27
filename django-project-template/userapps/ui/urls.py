from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^project/$', project, name='project'),
    url(r'^collect/$', collect,
        name='collect'),
    url(r'^summary/$', summary, name='summary'),
    url(r'^email/$', email, name='email'),
    url(r'^content/$', content, name='content'),
    url(r'^commit/$', commit, name='commit'),
    url(r'^upgrade/$', upgrade, name='upgrade'),
    url(r'^jenkins/$', jenkins, name='jenkins'),
    url(r'^shell/$', shell, name='shell'),
    url(r'^schedule/$', schedule, name='schedule'),
    url(r'^publishing/$', publishing, name='publishing'),
]
