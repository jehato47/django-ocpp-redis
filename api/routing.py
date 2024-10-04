from django.urls import re_path
from . import consumers


print("routing worked")
websocket_urlpatterns = [
    re_path(r'IonBee/ocpp/(?P<company_id>\w+)/(?P<charge_point_id>\w+)/$', consumers.OcppConsumer.as_asgi()),
    re_path(r'IonBee/external_control/(?P<company_id>\w+)/(?P<charge_point_id>\w+)/$', consumers.ExternalCommandsConsumer.as_asgi()),
]