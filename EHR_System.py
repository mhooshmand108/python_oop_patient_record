class Patient:
    hospital_name= "imam hossein"
    hospital_location= "Hashtrud"
    
    def __init__(self,name,diagnosis,age,symptom):
        self.name = name
        self.diagnosis = diagnosis
        self.age = age
        self.symptom = symptom
    
    def show_symptom(self):
        print(f"{self.name} has this symptom= {self.symptom}")
        
    def info(self):
        print(f"the patient's record in {Patient.hospital_name} hospital")
        print(f"location in {Patient.hospital_location}")
        print(str(self))
        
    def __str__(self):
        return (f"[name= {self.name} | age = {self.age} | diagnosis= {self.diagnosis} | symptom = {self.symptom} ]")
    
class Chronicpatient (Patient) :
    def __init__(self, name, diagnosis, age, symptom, chronic_disease):
       super().__init__(name, diagnosis, age, symptom)
       self.chronic_disease = chronic_disease
       
    def show_symptom(self):
       print(f"namechronicpatient={self.name} " f"(diagnosis={self.chronic_disease}) symptom:{self.symptom}")
     
    def __str__(self):
        return (f"[chronic record {self.name} | age = {self.age} | diagnosis = {self.diagnosis} | zamineh = {self.chronic_disease}]")
    
    #test
    
    
p1= Patient  ('ali','DM','38','Polyuria')
p2 = Patient('sara', 'virus', '21', 'fever')

print(p1)
print(p2)


print("\n recording to info :")
p1.info() 

p2.info()

