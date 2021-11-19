import json
import http.client
from datetime import datetime
from weather.core.domain.interfaces.datasource_interface import DatasourceInterface
from weather.core.domain.entities.timezone import Timezone


class WorldtimeRestApi(DatasourceInterface):
    def __init__(self, host: str, endpoint: str) -> None:
        self.__host = host
        self.__endpoint = endpoint

    def get_utc_time(self, area: Timezone) -> datetime:

        conn = http.client.HTTPConnection(self.__host)

        target = f"{self.__endpoint}/{area.area}"

        conn.request("GET", target)

        res = conn.getresponse()
        data = res.read()
        _data = json.loads(data.decode("utf-8"))

        area_datetime = _data["datetime"]

        utc_res = datetime.strptime(area_datetime, "%Y-%m-%dT%H:%M:%S.%f%z")

        return utc_res
