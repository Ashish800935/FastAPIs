# def insert_patient_data(name,age): # but type issue occured 
#     print(name)
#     print(age)
#     print('inserted into database')


# insert_patient_data('Asheesh','21')    


# Solve manually
# def insert_patient_data(name:str,age:int):  # But manually take time and not scalable at all now pydantic comes in picture 
#     if type(name)==str and type(age)==int:
#         if age <0:
#             raise ValueError('age can not be negative')
#         else:
#             print(name)
#         print(age)
#         print('inserted into database')

#     else:
#         raise ValueError('invalid data type')    


# insert_patient_data('Asheesh',21) 





## PYDANTIC 
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):

    name:Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 chars',examples=['Asheesh','Amit'])]
    email:EmailStr
    linkedinurl:AnyUrl
    age:int=Field(gt=0,lt=90)
    weight: Annotated[float,Field(gt=0,strict=True)] # strict for default type conversion by pydantic 
    married:bool=False ## Default value
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)] 
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient): 
    print(patient.name)
    print(patient.age)
    print('inserted into database')


patient_info={'name':'Asheesh','email':'abc@gmail.com','linkedinurl':'http://linkedin.com/1324',  'age':21,'weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'1234567890'}}

patient1=Patient(**patient_info)

insert_patient_data(patient1)