from enum import Enum


class Semester(Enum):
    Fall = 1
    Spring = 2


class Subject(Enum):
    All = 0
    AfricanaStudies = "AFST"
    AmericanStudies = "AMST"
    Anthropology = "ANTH"
    AppliedScience = "APSC"
    Arabic = "ARAB"
    Art = "ART"
    ArtHistory = "ARTH"
    AsianMiddleEasternStudies = "AMES"
    AsianPacificIslanderStudies = "APIA"
    Biology = "BIOL"
    BusinessAdministration = "BUAD"
    Chemistry = "CHEM"
    Chinese = "CHIN"
    ClassicalCivilization = "CLCV"
    CollegeCourses = "COLL"
    CommunityStudies = "CMST"
    CAMS = "CAMS"
    ComputerScience = "CSCI"
    CreativeWriting = "CRWR"
    CurriculumInstruction = "CRIN"
    Dance = "DANC"
    DataScience = "DATA"
    Economics = "ECON"
    EdPolicyPlanningLeadership = "EPPL"
    Education = "EDUC"
    ElementaryEducation = "ELEM"
    English = "ENGL"
    EnvironmentalScience = "ENSP"
    EuropeanStudies = "EURS"
    FilmMediaStudies = "FMST"
    French = "FREN"
    GenderSexualityWomenStudies = "GSWS"
    GeographicInformationSystems = "GIS"
    Geology = "GEOL"
    German = "GRMN"
    GlobalStudies = "GBST"
    Government = "GOVT"
    Graduate = "GRAD"
    Greek = "GREK"
    HealthSciences = "HSCI"
    Hebrew = "HBRW"
    HispanicStudies = "HISP"
    History = "HIST"
    InterdisciplinaryStudies = "INTR"
    InternationalRelations = "INRL"
    Italian = "ITAL"
    Japanese = "JAPN"
    Kinesiology = "KINE"
    Latin = "LATN"
    LatinAmericanStudies = "LAS"
    Law = "LAW"
    Linguistics = "LING"
    MarineScience = "MSCI"
    Math = "MATH"
    MedievealRenaissanceStudies = "MRAS"
    MilitarySciecne = "MLSC"
    ModernLanguages = "MDLL"
    Music = "MUSC"
    Neuroscience = "NSCI"
    Philosophy = "PHIL"
    Physics = "PHYS"
    Psychology = "PSYC"
    PublicHealth = "PBHL"
    PublicPolicy = "PUBP"
    ReligiousStudies = "RELG"
    Russian = "RUSN"
    RussianPostSovietStudies = "RPSS"
    Sociology = "SOCL"
    Speech = "SPCH"
    Theatre = "THEA"
    Writing = "WRIT"


class Status(Enum):
    Any = 0
    Open = "OPEN"
    Closed = "CLOSED"


def buildURL(year: int, semester: Semester, subject: Subject, status: Status):
    semester_code = "10" if semester == Semester.Fall else "20"
    full_year = str(year + (1 if semester == Semester.Fall else 0)) + semester_code

    base_url = "https://courselist.wm.edu/courselist/courseinfo/searchresults"
    return f"{base_url}?term_code={full_year}&term_subj={subject.value}&attr=0&attr2=0&levl=UG&status={status.value}&ptrm=0&search=Search"