from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str

    def to_dict(self):
        return asdict(self)
