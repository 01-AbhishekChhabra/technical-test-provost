from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from DummyData import views

app_name = 'DummyData'

urlpatterns = [
    url(r'^/addData$', views.AddDummyData.as_view(), name='AddDummyData'),
]
