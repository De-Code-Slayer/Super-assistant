from datetime import date
from ..helpers.data_types import Gender


class Person:

    Number_of_persons = 0  # a class attribute to keep track of persons recognized in the system
    """ for example a person must have these characteristics(attributes) and be able to perform some functions(methods)"""
    def __init__(self, first_name: str, last_name: str, dob: int, gender:Gender, address: str, occupation:str):

        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.address = address
        self.occupation = occupation

        # increase number of person count
        # add person to database 
        # triger post init methods

    def get_age(self, today:date) -> int:
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'