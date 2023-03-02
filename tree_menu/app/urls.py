from django.urls import path
from django.views.generic import TemplateView

app_name = 'app'

urlpatterns = [
    path(
        'menu/',
        TemplateView.as_view(
            template_name='menu/index.html',
            extra_context={'title': 'Меню'},
        ),
        name='index',
    ),
]
