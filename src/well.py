import datetime
from typing import Optional
class Well(object):

    def __init__(self,position: int,sample_name: str, test_type: str, slide_ID: str, sample_type:str,
                 titer:int = 1, patient_name: Optional[str] = None,surname: Optional[str] = None, dayob: Optional[str] = None,
                 monob: Optional[str] = None, yearob: Optional[str] = None, patientID: Optional[str] = None,
                 comment: Optional[str] = None) -> None:
        super().__init__()
        datetime_object = datetime.datetime.now()
        hour, minute, second = str(datetime_object.hour).zfill(2), str(datetime_object.minute).zfill(2), str(
            datetime_object.second).zfill(2)
        date, year, month = str(datetime_object.day).zfill(2), str(datetime_object.year), str(
            datetime_object.month).zfill(2)
        self.date = f"{month}/{date}/{year}"
        self.time = f"{hour}:{minute}:{second}"
        self.position = position
        self.sample_name = sample_name
        self.test_type = test_type
        self.slide_ID = slide_ID
        self.sample_type = sample_type
        self.titer = titer
        self.patient_name = patient_name
        self.surname = surname
        self.dayob = dayob
        self.monob = monob
        self.yearob = yearob
        self.patient_ID = patientID
        self.comment = comment


    def __str__(self) -> str:
        return f"{self.date};{self.sample_name};{self.test_type};{self.position};{self.slide_ID};{self.test_type};" \
               f"{self.titer};{self.time};{self.sample_type};{self.patient_name};{self.surname};{self.dayob};" \
               f"{self.monob};{self.yearob};{self.patient_ID};{self.comment}"







