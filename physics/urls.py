from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from physics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^student/', views.index_student, name='index_student'),
    url(r'^get_homework/', views.get_homework, name='get_homework'),
    url(r'^submit_homework/', views.submit_homework, name='submit_homework'),
    url(r'^retrieve_summary/', views.retrieve_summary, name='retrieve_summary'),
    url(r'^retrieve_homework/', views.retrieve_homework, name='retrieve_homework'),
    url(r'^enter_summary/', views.enter_summary, name='enter_summary'),
    url(r'^enter_homework/', views.enter_homework, name='enter_homework'),
    url(r'^enter_question/', views.enter_question, name='enter_question'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^verify_homework/', views.verify_homework, name='verify_homework'),
    url(r'^enter_question_part/', views.enter_question_part, name='enter_question_part'),
    url(r'^enter_question_hint/', views.enter_question_hint, name='enter_question_hint'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)