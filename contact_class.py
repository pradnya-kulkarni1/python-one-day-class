
from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    email: str
    phone: str

    def current_contact_details(self):
        details = f"Name: {self.first_name}{self.last_name}\n Email Address: {self.email}\n Phone Number: {self.phone}"
        return details



#  def get_person_details(self):
#         details = f"id:{self.id}, first_name: {self.first_name}, last_name: {self.last_name}"
#         details += f"email: {self.email}, phone :{ self.phone}"
#         return details