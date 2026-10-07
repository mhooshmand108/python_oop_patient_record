# python-oop-patient-record     

A beginner-friendly Python OOP project for managing patient records.
🏥 Python EHR System


The project was built to practice core Object-Oriented Programming (OOP) concepts in Python, including classes, objects, inheritance, "super()", method overriding, class attributes, and magic methods.

---

📖 About the Project

This project models a simple hospital patient record system.

Each patient has basic information such as:

- Name
- Age
- Diagnosis
- Symptoms

The project also includes a "ChronicPatient" class that inherits from "Patient" and adds information about an underlying chronic disease.

---

✨ Features

- ✅ "Patient" class for creating patient records
- ✅ "ChronicPatient" subclass
- ✅ Patient name, age, diagnosis, and symptoms
- ✅ Chronic disease information for chronic patients
- ✅ Class attributes for hospital name and location
- ✅ "show_symptom()" method
- ✅ "info()" method for displaying patient records
- ✅ "__str__()" for readable object representation
- ✅ Method overriding in "ChronicPatient"
- ✅ Use of "super()" in inheritance

---

🧠 OOP Concepts Covered

Concept| Where
Class & Object| "Patient", "ChronicPatient"
Constructor "__init__"| Both classes
Instance Attributes| "self.name", "self.age", "self.diagnosis", "self.symptom"
Class Attributes| "hospital_name", "hospital_loc"
Inheritance| "ChronicPatient(Patient)"
"super()"| "ChronicPatient.__init__"
Method Overriding| "show_symptom()", "__str__()"
Magic Method| "__str__()"

---

🚀 How to Run

Requirements

- Python 3.8 or higher

Run

python ehr_system.py

---

🔮 Future Improvements

This project is an ongoing learning project, and new features will be added as I continue learning Python and OOP.

Possible future improvements include:

- [ ] Add more patient types
- [ ] Add patient search functionality
- [ ] Add editing and deleting patient records
- [ ] Add input validation
- [ ] Store patient records in JSON
- [ ] Add a hospital management class
- [ ] Improve project structure
- [ ] Add automated tests

---

📚 Purpose

This project is part of my journey in learning Python and Object-Oriented Programming and is intended to grow over time as new concepts and features are learned.
