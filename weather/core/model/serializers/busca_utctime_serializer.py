import json
from typing import Any, Dict


class BuscaUtctimeJsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Dict[str, Any]:

        try:

            to_serialize = {
                "status": "Success",
                "code": 0,
                "message": {"date": o.date, "time": o.time},
            }

            return to_serialize

        except AttributeError:
            return super().default(o)
