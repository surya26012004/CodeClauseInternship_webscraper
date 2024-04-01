que=[["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3],
["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3],
["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3],
["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3],
["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3],
["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3],
["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3],
["who is the csk captain","1.virat","2.rohit","3.dhoni","4.ganguly",3]]
amount=[10000,30000,100000,1000000,3000000,5000000,70000000]

for i in range(0,len(que)):
    que1=que[i]
    print(f"{que1[0]}")
    print(f"{que1[1]}                  {que1[2]}")
    print(f"{que1[3]}                  {que1[4]}")
    a=int(input("enter your choice:"))
    if(a==que1[-1]):
       
        print("correct answer : \n you won :",amount[i])
        if(i==6):
            print(f" congratualtions!!!!!! \n you won the game \n with the money{amount[i]} ")
            break
         
    else:
        if(i>2):
            print(f"you won {amount[2]}") 
            break
        elif(i>4):
            print(f"you won {amount[4]}")
            break
        elif(i<=2):
            print("you won 0 rupees!!")
            break
    
        




    
