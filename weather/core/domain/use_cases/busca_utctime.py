from weather.core.domain.interfaces.datasource_interface import DatasourceInterface
from weather.core.model.request.busca_utctime_input import BuscaUtctimeInputDto
from weather.core.model.response.busca_utctime_output import BuscaUtctimeOutputDto
from weather.core.domain.entities.timezone import Timezone


class BuscaUtcTime:
    def __init__(
        self, input_dto: BuscaUtctimeInputDto, repo: DatasourceInterface
    ) -> None:

        self.input_dto = input_dto
        self.repo = repo

    def run(self) -> BuscaUtctimeOutputDto:

        # Create an entity to create a business object and run business logic validation
        tz_area = Timezone.from_dict({"area": self.input_dto.area})

        # Access an external layer through an injected object (Dependency Inversion Principle).
        res = self.repo.get_utc_time(tz_area)

        # Return result object
        return BuscaUtctimeOutputDto.from_dict(
            {"date": res.strftime("%Y-%M-%d"), "time": res.strftime("%H:%M:%S")}
        )
