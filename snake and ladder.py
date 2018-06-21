import random
count=0
while count<=100:
    roll=input("press r to roll a dice")
    if roll=='r':
        r=random.randit(1,6)
        count=count+r
        print("the present value",count)
        print("the dice value",r)
        if(count==8):
            count=8
            print("climb :dice moves to 37")
        elif(count==11):
            count=2
            print("bite:dice moves to 2")
        elif(count==13):
            count=34
            print("climb;dice moves to 34")
        elif(count==25):
            count=4
            print("bite:dice moves to 4")
        elif(count==38):
            count=9
            print("bite:dice moves to 9")
        elif(count==40):
            count=68
            print("climb:dice moves to 68")
        elif(count==52):
            count=81
            print("climb:dice moves to 81")
        elif(count==87):
            count==90
            print("climb:dice moves to 90")
        
    
            
        
    
