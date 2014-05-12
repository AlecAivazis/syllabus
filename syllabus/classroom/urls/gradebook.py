from django.conf.urls import  url

from ..views.gradebook import *

# calendar urls
urlpatterns = [
    url(r'(?i)^addGrade/$', addGrade),
    url(r'(?i)^allStudents/$', allStudents),
    url(r'(?i)^selectedAssistants/$', selectedAssistants),
    url(r'(?i)^changeCategory/$', changeCategory),
    url(r'(?i)^changePossiblePoints/$', changePossiblePoints),
    url(r'(?i)^count/$', count),
    url(r'(?i)^gradingScale/view$', gradingScale),
    url(r'(?i)^gradingScale/setScale$', setScale),
    url(r'(?i)^loadEvent/$', loadEvent),
    url(r'(?i)^sectionsForClass/$', sectionsForClass),
    url(r'(?i)^setSectionAssistants/$', setSectionAssistants),
    url(r'(?i)^totalGrade/$', totalGrade),
    url(r'(?i)^viewGradeBook/$', viewGradeBook),
    url(r'(?i)^weights/view/$', viewWeights),
    url(r'(?i)^weights/set/$', assignWeights),
    url(r'(?i)^weights/eventWeight/$', eventWeight),
    url(r'(?i)^weights/remove/$', removeWeight),
    url(r'(?i)^$', gradebookHome),
]

