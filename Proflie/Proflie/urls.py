from django.urls import path, include
from proflieApp.views import message_list, Message_edit, MessageApiView, MessageDetails, Message_list, message_edit
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('sample/', Message_list),
    path('sample1/<int:pk>', Message_edit),
    path('apiview/', message_list),
    path('apiview1/<int:pk>', message_edit),
    path('class/', MessageApiView.as_view()),
    path('class1/<int:id>', MessageDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
