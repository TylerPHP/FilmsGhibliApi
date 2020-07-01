from rest_framework.exceptions import APIException


class NotFound(APIException):
    status_code = 404
    default_detail = "error"
    default_code = "not found"
