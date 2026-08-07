from django.urls import path

from .views import (
    SMSDashboardView,
    ReadyDevicesView,
    SendReadyDeviceSMSView,
    SendSingleSMSView,
    SendBulkSMSView,
    SMSLogListView,
)


app_name = "sms"


urlpatterns = [

    path(
        "",
        SMSDashboardView.as_view(),
        name="dashboard"
    ),

    path(
        "ready/",
        ReadyDevicesView.as_view(),
        name="ready-devices"
    ),

    path(
        "ready/<int:pk>/send/",
        SendReadyDeviceSMSView.as_view(),
        name="send-ready"
    ),

    path(
        "single/",
        SendSingleSMSView.as_view(),
        name="send-single"
    ),

    path(
        "bulk/",
        SendBulkSMSView.as_view(),
        name="send-bulk"
    ),

    path(
        "logs/",
        SMSLogListView.as_view(),
        name="logs"
    ),
]

