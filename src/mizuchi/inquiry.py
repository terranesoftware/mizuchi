from dataclasses import dataclass


@dataclass(slots=True)
class Inquiry:
    """Establishes the reason and field of consideration."""

    occasion: str
    universe: list[EntityKey]


# Doc this later
@dataclass(slots=True)
class EntityKey:
    key: str
    children: list[EntityKey]
