from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        # abc@gmail.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Age shuld be in between 0 and 100')





def insert_patient_data(patient:Patient): 
    print(patient.name)
    print(patient.age)
    print('inserted into database')


patient_info={'name':'Asheesh','email':'abc@hdfc.com','linkedinurl':'http://linkedin.com/1324',  'age':'21','weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1234567890'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)