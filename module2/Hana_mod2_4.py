import json
import random

class Person:
    def __init__(self,name,number,location,job_title):
        self.name=name
        self.number=number
        self.location=location
        self.job_title=job_title

names=["Arif","Adri","Fredy","Topik","Shamsa","Cristina","John","Fidel"]
locations=["Abu Dhabi","Dubai","Alain","Fujarah","Indonesia","Colombia","RAK","Sharjah"]
jobs=["Technician","Developer","Engineer","Doctor","Nurse","Officer","Teacher","Barista"]

people = []

for _ in range(5):
    person= Person(
        name=random.choice(names),
        number=random.randint(1000000000,9999999999),
        location=random.choice(locations),
        job_title=random.choice(jobs)
    )
    people.append(person.__dict__)
    

with open("5_random _people.json","w") as f:
    json.dump(people,f,indent=4)
    print("5 random people saved to people.json")
