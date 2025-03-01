from django.contrib import admin
from django.urls import path
from .views import Home,DetailView
app_name = 'core'
urlpatterns = [
    path('', Home.as_view(),name = 'home'),
    # path('related/', Related.as_view(),name = 'related-view'),
    path('detail/<slug:slug>/', DetailView.as_view(),name = 'detail-view'),
]


