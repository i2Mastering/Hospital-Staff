# Spam University Hospital Staff Management

## Description
Spam University Hospital is expanding its operations and hiring new personnel. This program models hospital staff, allowing easy management of:
- Doctors categorized by specialty.
- Surgeons, differentiated by board certification status.
- Nurses ranked by qualification levels.

The system calculates salaries based on specialization, certification, and rank, displaying detailed information about each staff member.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Classes](#classes)
- [Requirements](#requirements)
- [License](#license)

## Features
- Assigns and displays doctors, surgeons, and nurses with their details.
- Calculates salaries based on medical specialization or certification status.
- Supports easy expansion for additional staff roles.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/hospital-staff-management.git
   ```
2. Navigate to the project directory:
   ```sh
   cd hospital-staff-management
   ```
3. Ensure Python 3.x is installed.

## Usage
1. Run the script:
   ```sh
   python hospital_staff.py
   ```
2. The program will:
   - Display a doctor with specialization details.
   - Display a surgeon and confirm board certification status.
   - Display a nurse with rank and hourly rate.

## Example
```sh
The name of our doctor is Dr. Andrew, age 2.
Dr. Andrew specializes in Pediatrics with an hourly rate of $100 per hour.

The name of our Surgeon is Dr. Jessica, age 35.
Dr. Jessica is board certified with an hourly rate of $140 per hour.

The name of our nurse is ARPN. Riley, age 9, with an hourly rate of $75 per hour.
```

## Classes
### `Personnel`
- Base class representing all hospital employees.
- Attributes: `name`, `age`, `hourlyRate`.

### `Doctor`
- Inherits from `Personnel`, adding `specialty`.
- Determines salary based on specialization.
- **Method:** `displayDoctor()` – Prints doctor details.

### `Surgeon`
- Inherits from `Personnel`, adding `boardCertified` status.
- Determines salary based on board certification.
- **Method:** `displaySurgeon()` – Prints surgeon details.

### `Nurse`
- Inherits from `Personnel`, categorized by `rank`.
- Determines salary based on rank.
- **Method:** `displayNurse()` – Prints nurse details.

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License.
