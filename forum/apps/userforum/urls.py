# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\11\22 0022 10:30$'

from django.urls import path
from .views import ForumDatileView,ForumView,ForumTypeView

urlpatterns = [
    path('forum_list/',ForumView.as_view(),name="forum_list"),
    path('<int:forum_id>',ForumDatileView.as_view(),name="forum_datil"),
    path('type/<int:type_id>',ForumTypeView.as_view(),name="forum_type"),
]