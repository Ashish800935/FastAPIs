from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height: float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI',patient.bmi)
    print('inserted into database')
        
    


patient_info={'name':'Asheesh','email':'abc@hdfc.com','linkedinurl':'http://linkedin.com/1324',  'age':'22','weight':75.2,'height':1.72,  'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1234567890'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)