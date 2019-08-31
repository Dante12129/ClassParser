from dataclasses import dataclass
from typing import List


@dataclass
class Course:
    """ Model for a course that contains all the information the Course List has on a course. """

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
        """ Gets the open-vs-closed status of the course as a string.
            :return "Open" or "Closed" depending on the course's status.
        """
        return "Open" if self.open else "Closed"
