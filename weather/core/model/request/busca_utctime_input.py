import re
import dataclasses
from ..base_model import BaseModel


@dataclasses.dataclass
class BuscaUtctimeInputDto(BaseModel):

    area: str

    def __post_init__(self) -> None:

        timezone_regex = r"^[A-Z]{1}\w+/[A-Z]{1}\w+[a-z]{1}$"

        # Validate `area`: formato esperado `America/Fortaleza`
        if not bool(re.match(timezone_regex, self.area)):
            raise ValueError("Formato do timezone inválido.")
