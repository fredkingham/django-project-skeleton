from django.views.generic import TemplateView
from django.conf.urls.defaults import patterns

urlpatterns = patterns('', 
    ('', TemplateView.as_view(template_name="index.html")),
)
