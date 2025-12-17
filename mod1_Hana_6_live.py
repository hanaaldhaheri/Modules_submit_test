class person_details:
    def __init__(self,name:str,contact:str,address:str,phone_number:int):
        self.name=name
        self.contact=contact
        self.address=address
        self. phone_number=phone_number
    
    def save(self):
        file=open("person_details.txt", "w")
        file.write(self.name+","+self.contact+","+self.address+","+self.phone_number+".")
        file.close()


#p1 = person_details("hana", "hana@gal.ae", "al ain", 933901)
#print(p1)

def get_input():
    name=input("Enter name : ")
    contact=input("Enter your email : ")
    address=input("Enter address details : ")
    phone_number=input("Enter phone number : ")
    return person_details(name,contact,address,phone_number)
#add_input() just to test

def save_input():
    person_details_1=get_input()
    person_details_1.save()

save_input()

