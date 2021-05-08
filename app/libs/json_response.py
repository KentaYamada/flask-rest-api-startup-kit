import json
from flask import Response


def json_dumps_handler(payload):
    if not isinstance(payload, object) and hasattr(payload, '__dict__'):
        raise ValueError()
    return payload.__dict__


class BaseJsonResponse(Response):
    def __init__(self, payload=None):
        super().__init__()
        self.mimetype = 'application/json'
        if payload is not None:
            self.set_payload(payload)

    def _to_json_object(self, payload):
        if payload is None:
            raise ValueError()
        return json.dumps(
            payload,
            default=json_dumps_handler,
            ensure_ascii=False,
            indent=2
        )

    def set_payload(self, payload):
        data = self._to_json_object(payload)
        self.set_data(data)


class OK(BaseJsonResponse):
    """ HTTP status: 200(OK) response class """
    def __init__(self, payload):
        super().__init__(payload)
        self.status_code = 200


class Created(BaseJsonResponse):
    """ HTTP status: 201(Created) response class """
    def __init__(self, payload):
        super().__init__(payload)
        self.status_code = 201


class NoContent(BaseJsonResponse):
    """ HTTP status: 204(No Content) response class """
    def __init__(self):
        super().__init__()
        self.status_code = 204
