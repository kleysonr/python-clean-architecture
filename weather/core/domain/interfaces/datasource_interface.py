import abc
from datetime import datetime
from weather.core.domain.entities.timezone import Timezone


class DatasourceInterface(abc.ABC):
    @abc.abstractmethod
    def get_utc_time(self, area: Timezone) -> datetime:
        pass
