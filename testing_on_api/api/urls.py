from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/testing_on_api/(?P<pk>[0-9]+)$',
        views.get_delete_update_api,
        name='get_delete_update_api'
    ),
    url(
        r'^api/v1/testing_on_api/$',
        views.get_post_api,
        name='get_post_api'
    )
]
