from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str


class Patient(BaseModel):
    name:str
    age:int
    gender:str
    address:Address

address_dict={'city':'gurgaon','state':'haryana','pin':'122001'}
address1=Address(**address_dict)  

patient_dict={'name':'Asheesh','age':22,'gender':'male','address':address1}
patient1=Patient(**patient_dict)

print(patient1)
print(patient1.address.city)

temp=patient1.model_dump(include=['name','gender'])

print(temp)
print(type(temp))


temp2=patient1.model_dump_json()

print(temp2)
print(type(temp2))