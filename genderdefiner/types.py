from dataclasses import dataclass
from genderdefiner.enums import Gender


@dataclass
class SubjectGender:
    gender: Gender
    probability: float
