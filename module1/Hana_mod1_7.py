# try:
#     print("Hana"+12)
# except:
#     print("Error")

def accept_string(text=None):
    try:
        if  text is None or not isinstance(text,str):
            raise Exception
        return text
    except:
        return "Null"
    
    
print(accept_string("cup"))


        
#make funtion and make it print if it is string/text then it will print the variable given
#  if not it will raise exception and print Null.