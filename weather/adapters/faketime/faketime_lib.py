from datetime import datetime
from weather.core.domain.interfaces.datasource_interface import DatasourceInterface
from weather.core.domain.entities.timezone import Timezone


class FaketimeLib(DatasourceInterface):
    def get_utc_time(self, area: Timezone) -> datetime:

        my_fake_date = "1900-01-01T00:00:00"

        res = datetime.strptime(my_fake_date, "%Y-%m-%dT%H:%M:%S")

        return res
