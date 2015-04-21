isbn = input("input a number of 10 digits")

def convert(isbn):
    while len(str(isbn) !=10
    print ("please enter a sensible 10 digit number")
    isbn = input("input a 10 digit number")

    dig1 = int(isbn[0])*11
    dig2 = int(isbn[1])*10
    dig3 = int(isbn[2])*9
    dig4 = int(isbn[3])*8
    dig5 = int(isbn[4])*7
    dig6 = int(isbn[5])*6
    dig7 = int(isbn[6])*5
    dig8 = int(isbn[7])*4
    dig9 = int(isbn[8])*3
    dig10 = int(isbn[9])*2
    
    mainnumber = (int(dig1) + int(dig2) + int(dig3) + int(dig3) + int(dig4) + int(dig5) + int(dig6) + int(dig7) + int(dig8) + int(dig9) + int(dig10))
    answer = int(mainnumber) % 11
    
    if answer == 0:
        num11 = 0
        
        else:
            dig11 = 11 - answer
            if dig11 == 10:
                dig11 = "X"
                
    isbn = str(dig) + str(dig11)
    return isbn
    
convert(dig)

if len(dig) == 10:
    print "the isbn number is:", convert(dig)
