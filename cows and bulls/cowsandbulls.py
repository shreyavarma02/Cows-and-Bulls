import turtle
import getpass as gp
print("INSTRUCTIONS:\n•A player will create a secret code, a 4-digit number.  This number should have no repeated digits.\n•Another player makes a guess (4-digit number) to crack the secret number. Upon making a guess, the number of cows and bulls will be provided.\n•Bulls indicate the number of correct digits in the correct position and cows indicates the number of correct digits in the wrong position. For example, if the secret code is 1234 and the guessed number is 1246 then we have 2 BULLS (for the exact matches of digits 1 and 2) and 1 COW (for the match of digit 4 in the wrong position)•The player has 8 tries to crack the code. \n•The player who guesses the code in the minimum number of tries wins. •If there is a tie between the two players, the game is played again to check for a winner.")

def player(n):
   def inp(word):
       if word=="code":
              x=gp.getpass(prompt="Enter your code(Note that the code won't be displayed on the screen while you're typing)\n")
       else:
              print("Player",n,":")
              print("Enter your guess")
              x=input()
       if (x.isdigit()==False)|(len(x)!=4)|(len(set(x))!=len(x)):
              print("Invalid",word)
              x=inp(word)
       return x
   global bc
   global cc
   global lc
   cc,bc,lc=0,0,1
  
   def check(y):
       for i in range(4):
              if y[i]==code[i]:
                     global bc
                     bc+=1
              elif (y[i] in code)&(y[i]!=code[i]):
                     global cc
                     cc+=1

   code=inp("code")

   for i in range(8):
       guess=inp("guess")
       check(guess)       
       if bc==4:
           break
       else:
              print("Number of cows=",cc,"\nNumber of bulls=",bc)
              bc,cc=0,0
              print("Try again")
       lc+=1
       print("You have",9-lc,"tries left")




   if lc<=8:
        print("You have entered the right code in",lc,"guesses")
	
   else:
       print("Sorry, you lose.\nThe correct answer was ",code,".",sep='')
   return(lc)


def winner():
   print("\nGame 1")
   print("Player 2:")
   lc1=player(1)
   print("\ngame 2")
   print("Player 1:")
   lc2=player(2)


   if(lc1<lc2):
     print("\nPlayer 1 is the winner")
   elif(lc1>lc2):
     print("\nPlayer 2 is the winner")
   else:	
     print("\nIts a tie! Play again")
     winner()

winner()

screen=turtle.Screen()
screen.setup(500,500)
screen.title("Cows and bulls")
t1=turtle.Turtle()
screen.addshape("game1.gif")
t1.shape("game1.gif")
turtle.exitonclick()