from django.conf import settings

from kavenegar import KavenegarAPI
from kavenegar import APIException, HTTPException


def get_kavenegar_api():
    return KavenegarAPI(
        settings.KAVENEGAR_API_KEY,
        timeout=20
    )


def send_sms(
    receptor,
    message,
    sender=None,
):
    """
    ارسال یک پیامک از طریق کاوه نگار
    """

    api = get_kavenegar_api()

    params = {
        "receptor": receptor,
        "message": message,
    }

    if sender:
        params["sender"] = sender

    try:

        response = api.sms_send(params)

        return {
            "success": True,
            "response": response,
        }

    except APIException as e:

        return {
            "success": False,
            "error": str(e),
        }

    except HTTPException as e:

        return {
            "success": False,
            "error": str(e),
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
        }


def send_bulk_sms(
    receptors,
    message,
    sender=None,
):
    """
    ارسال یک متن به چند شماره
    """

    api = get_kavenegar_api()

    receptors = list(receptors)

    if not receptors:
        return {
            "success": False,
            "error": "هیچ شماره‌ای برای ارسال وجود ندارد.",
        }

    params = {
        "receptor": ",".join(receptors),
        "message": message,
    }

    if sender:
        params["sender"] = sender

    try:

        response = api.sms_send(params)

        return {
            "success": True,
            "response": response,
        }

    except APIException as e:

        return {
            "success": False,
            "error": str(e),
        }

    except HTTPException as e:

        return {
            "success": False,
            "error": str(e),
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
        }

