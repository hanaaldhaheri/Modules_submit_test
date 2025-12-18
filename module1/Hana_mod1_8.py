def word_count ():
    line = ""
    char_len = 0
    with open(".\\module1\\person_details.txt","r") as f:
        line=f.readline()
        word_len=line.split(",")
        char_len = len(word_len)
    
    with open(".\\module1\\person_details.txt","a") as f:
        f.write(str(char_len))
    
word_count()

#I created a word count foe each address then append it display in the same file where the text is.