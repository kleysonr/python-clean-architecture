from __future__ import annotations
import dataclasses
from typing import Any, Type


@dataclasses.dataclass
class BaseModel:
    @classmethod
    def from_dict(cls: Type[Any], params: Any) -> Any:
        return cls(**params)

    def to_dict(self) -> Any:
        return dataclasses.asdict(self)
