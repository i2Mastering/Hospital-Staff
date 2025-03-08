"""
Spam University Hospital is hiring new personnel with the expansion of a new hospital wing.
They are looking for doctors of specific specialties, surgeons regardless of board certification, and nurses.

This program manages hospital personnel by defining classes for different roles:
- Doctors with specialties that determine salary.
- Surgeons whose salary is based on board certification.
- Nurses ranked according to skill level.

Classes:
    - Personnel: Base class for employees.
    - Doctor: Extends Personnel, adding specialty.
    - Surgeon: Extends Personnel, considering board certification.
    - Nurse: Extends Personnel, categorizing rank.

Example Usage:
    $ python hospital_staff.py
    The name of our doctor is Dr. Andrew, age 2...
    Dr. Andrew specializes in pediatrics with an hourly rate of $100 per hour.
    
    The name of our Surgeon is Dr. Jessica, age 35...
    Dr. Jessica is board certified with an hourly rate of $140 per hour.
    
    The name of our nurse is ARPN. Riley, age 9, with an hourly rate of $75 per hour.

Author: Ike Iloegbu
License: MIT
"""

# Salary mappings based on profession and specialization
nurseRankings = {'CNA': 16, 'LPN': 40, 'RN': 60, 'ARPN': 75}
doctorSpecialties = {
    'PEDIATRICS': 100, 'OB/GYN': 110, 'CRITICAL CARE': 130,
    'ONCOLOGY': 150, 'UROLOGY': 200, 'ORTHOPEDICS': 250
}
boardCert = {"YES": 140, "NO": 110}

class Personnel:
    """Base class for all hospital employees."""
    def __init__(self, name, age, hourlyRate):
        self.name = name
        self.age = age
        self.hourlyRate = hourlyRate

class Doctor(Personnel):
    """Doctor class inheriting from Personnel, adding specialty attribute."""
    def __init__(self, name, age, specialty):
        hourlyRate = doctorSpecialties.get(specialty.upper(), 100)
        super().__init__(name, age, hourlyRate)
        self.specialty = specialty
    
    def displayDoctor(self):
        print(f"\nThe name of our doctor is Dr.{self.name}, age {self.age}. "
              f"Dr.{self.name} specializes in {self.specialty} with an hourly rate of ${self.hourlyRate} per hour.\n")

class Surgeon(Personnel):
    """Surgeon class inheriting from Personnel, considering board certification."""
    def __init__(self, name, age, boardCertified):
        hourlyRate = boardCert.get(boardCertified.upper(), 110)
        super().__init__(name, age, hourlyRate)
        self.boardCertified = boardCertified.upper()
    
    def displaySurgeon(self):
        print(f"The name of our Surgeon is Dr.{self.name}, age {self.age}.")
        print(f"Dr.{self.name} is {'board certified' if self.boardCertified == 'YES' else 'not yet board certified'} "
              f"with an hourly rate of ${self.hourlyRate} per hour.\n")

class Nurse(Personnel):
    """Nurse class inheriting from Personnel, categorized by rank."""
    def __init__(self, name, age, rank):
        hourlyRate = nurseRankings.get(rank.upper(), 16)
        super().__init__(name, age, hourlyRate)
        self.rank = rank
    
    def displayNurse(self):
        print(f"The name of our nurse is {self.rank}. {self.name}, age {self.age}, "
              f"with an hourly rate of ${self.hourlyRate} per hour.\n")

# Create instances for demonstration
if __name__ == "__main__":
    dr = Doctor("Andrew", 2, "Pediatrics")
    dr.displayDoctor()
    
    srg = Surgeon("Jessica", 35, "YES")
    srg.displaySurgeon()
    
    nr = Nurse("Riley", 9, "ARPN")
    nr.displayNurse()
