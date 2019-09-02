from enum import Enum


class Semester(Enum):
    Fall = 1
    Spring = 2


def buildURL(year: int, semester: Semester):
    semester_code = "10" if semester == Semester.Fall else "20"
    full_year = str(year + 1 if semester == Semester.Fall else 0) + semester_code

    base_url = "https://courselist.wm.edu/courselist/courseinfo/searchresults"
    return f"{base_url}?term_code={full_year}&term_subj=CSCI&attr=0&attr2=0&levl=UG&status=0&ptrm=0&search=Search"