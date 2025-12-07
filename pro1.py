# e mail validation
k,j,d = 0,0,0
email = input("Enter your Email")
if len(email) >= 6:     # y@g.in

    if email[0].isalpha():   # starting at character
        
        if ("@" in email) and (email.count("@") == 1):    # number of @ is 1
            if(email[-4] == ".") ^ (email[-3] == "."):     # .com or .in  (^ is xor operater)
                
                for i in email:
                    if i == i.isspace():  #check space
                        k=1
                    #elif i.isalpha():
                    elif i==i.upper():   # A=A
                            j=1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i =="." or i =="@": 
                         continue
                    else:
                        d=1



                if k==1 or j==1 or d==1:
                    print("right e mail")        
            else:
                print("wrong Email 4")
        else:
            print("wrong Email 3")

    else:
        print("wrong Email 2")
else:
    print("wrong Email 1")

