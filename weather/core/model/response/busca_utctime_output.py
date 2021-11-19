import dataclasses

from weather.core.model.base_model import BaseModel


@dataclasses.dataclass
class BuscaUtctimeOutputDto(BaseModel):

    date: str
    time: str
