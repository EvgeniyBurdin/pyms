import json
from datetime import datetime
from uuid import UUID


class ApiJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return int(obj.timestamp())
        return json.JSONEncoder.default(self, obj)


def json_dumps(obj):
    return json.dumps(obj, cls=ApiJSONEncoder)
