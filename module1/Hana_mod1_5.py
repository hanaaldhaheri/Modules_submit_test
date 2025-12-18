def string_words_price(string,price_letter):
    shifted_letter=""
    letter_count=0

    for char in string:
        if char.isalpha():
            letter_count +=1
            if char =='z':
                shifted_letter +='a'
            elif char == 'Z':
                shifted_letter +='A'
            else:
                shifted_letter +=chr(ord(char)+1)
        else:
            shifted_letter +=char

    word_count= len(string.split())
    total_price = letter_count*price_letter
    return{
        "shifted_string": shifted_letter,
        "word_count": word_count,
        "price_of_string": total_price
    }
print(string_words_price(string="ghij",price_letter=5))

#I defined a function that has a parameters of string and price_letter.
#then declared shifted_letter to any "" also letter_count=0 as the start then later i added +1 to shift.
#i added a condition if the char is 'z' then it will shift to 'a' else (ord=character to numerical+1 then change to character)
#then word_count will show the length of the parameter and split if it has more than one word it will also show the price of the string.