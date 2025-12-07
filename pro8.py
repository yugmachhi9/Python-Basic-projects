#quiz compitition

print("welcome to my quiz")

play = input("do u want to play?(yes/no)")
if play == "yes":
    print("hello")
else:
    print("tq")
score = 0

answer = input("cpu stand for?")
if answer == "control processing unit":
    print("correct")
    score += 1    
else:
    print("incorrect")

answer = input("ram stand for?")
if answer == "random access memory":
    print("correct")
    score += 1    
else:
    print("incorrect")
    
answer = input("gpu stand for?")
if answer == "graphics processing unit":
    print("correct")
    score += 1    
else:
    print("incorrect")
print("your score =",score,"/3") 
