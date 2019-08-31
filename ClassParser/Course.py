from dataclasses import dataclass
from typing import List


@dataclass
class Course:
    """ Documentation """

    crn: int
    id: str
    attributes: List[str]
    title: str
    instructor: str
    credits: int
    time: str
    projected_enrollment: int
    current_enrollment: int
    seats_available: int
    open: bool

    @property
    def status(self) -> str:
        """ Documentation """
        return "Open" if self.open else "Closed"
