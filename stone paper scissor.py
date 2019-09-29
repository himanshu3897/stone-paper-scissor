def game():                         #it is used as menu to select from option stone, paper, scissor
    print("enter 1 for stone")
    print("enter 2 for paper")
    print("enter 3 for scissor")

import random       #it is used to import random library
result=0            #it is used for checking which will win the game
score_comp=0        #used to store the score of computer
score_user=0        #used to store the score of the user 
print("\t\twelcome to the game of stone, paper and scissors")  #welcoming note
c=int(input("enter 1 to play=>")) #for entering in to the game
print('')
print("RULE OF THE GAME")  #it will print the rule of the game so user can check it 
print("if stone vs paper, paper will win")
print("if paper vs scissor, scissors will win")
print("if stone vs scissor, stone will win \n")
if c==1:
    choice=True
    while(choice):
        
        
        game()        #function game is called that is define above
        print("")
        
        input1=int(input("enter your choice from the above menu=>"))  #takes input from the user
        print("")
        
        if(input1==1):            #it will show which input is choosen by the user
            choice_name="stone"
        elif(input1==2):
            choice_name="paper"
        elif(input1==3):
            choice_name="scissor"
        else:
            print("please choice correct option from the menu") #it is used for whether if anyone has choose wrong option from the menu
            continue
        print("you choose =>",choice_name)#print the choice of the user
        print("")
        a=random.randint(1,3)#random dunction is used so that cpu can randomly choose its option 
        if(a==1): #used to check which option has been choosen by the cpu
            comp_choice_name="stone"
        elif(a==2):
            comp_choice_name="paper"
        elif(a==3):
            comp_choice_name="scissor"
        print("choice of computer =>",comp_choice_name)#print the choice of the cpu
        print("")
        if((input1==1 and a==1)or(input1==2 and a==2)or(input1==3 and a==3)):#it will check the cases and decide whether who wins the game
            print(choice_name,"vs",comp_choice_name)
            print("Game draw")
       
        elif ((input1==1 and a==2) or (input1==2 and a==1)):
            print(choice_name,"vs",comp_choice_name)
            print("")   
            print("paper wins")
            result=2
            
            
        elif ((input1==2 and a==3) or (input1==3 and a==2)):
            print(choice_name,"vs",comp_choice_name)
            print("")
            print("scissor wins")
            result=3
            
        elif ((input1==3 and a==1) or (input1==1 and a==3)):
            print(choice_name,"vs",comp_choice_name)
            print("")
            print("stone wins")
            result=1

            
             
        else:
            print("")
            print("please try again") 
        if a==input1: #if both have same option then no will win the game
            print("")
            print("no one wins")
        
        elif a==result: #it is used to check the result of the above game who win and loss
                      print("")
                      print ("computer wins ")
                      score_comp=score_comp+1 #if computer wins it will update the score of the cpu 
                      print("")
                      print("score of computer is",score_comp)#print the score of the cpu
        else:
                      print("")
                      print("user wins")
                      print("")
                      score_user=score_user+1 #if user wins it will update the score of the user
                      print("score of user=>",score_user)#print the score of the user
        if(score_user==5):#it will check if anybody wins 5 matches it will declare the winner of the game
            print("\t\tCONGRATULATIONS YOU WIN THE GAME ")
            
            break
        elif(score_comp==5):
            print("\t\tCOMPUTER WINS THE GAME")
            break
        
            
else:
     print ("please try again and enter correct option")
     

        
