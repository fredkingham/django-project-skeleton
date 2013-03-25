from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns

urlpatterns = patterns('', 
    ('', direct_to_template, {"template": "index.html"}),
)