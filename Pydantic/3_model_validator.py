from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model

    


def insert_patient_data(patient:Patient): 
    print(patient.name)
    print(patient.age)
    print('inserted into database')


patient_info={'name':'Asheesh','email':'abc@hdfc.com','linkedinurl':'http://linkedin.com/1324',  'age':'22','weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1234567890'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)