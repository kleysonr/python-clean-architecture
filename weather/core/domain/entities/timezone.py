import dataclasses

from .base_entity import BaseEntity


@dataclasses.dataclass
class Timezone(BaseEntity):
    area: str

    def __post_init__(self) -> None:

        valid_timezones = [
            "America/Araguaina",
            "America/Bahia",
            "America/Belem",
            "America/Boa_Vista",
            "America/Campo_Grande",
            "America/Cuiaba",
            "America/Fortaleza",
            "America/Maceio",
            "America/Manaus",
            "America/Porto_Velho",
            "America/Recife",
            "America/Rio_Branco",
            "America/Santarem",
            "America/Sao_Paulo",
        ]

        # Validate `area`
        if self.area not in valid_timezones:
            raise ValueError("Timezone inválida.")
