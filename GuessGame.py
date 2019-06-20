from random import randint
def no_repeat(number):
    #Function to check unique digits
    x1=int(number%10)
    number/=10
    x2=int(number%10)
    number/=10
    x3=int(number%10)
    if x1==x2 or x1==x3 or x2==x3:
        return 1
    else:
        return 0
def bull(n1,n2):
    #Function to check right place right digit
    if n1==n2:
        return 1
    else:
        return 0
def check(actual,guess):
    #gives analysis to user
    x=int(actual)
    y=int(guess)
    x3=int(x%10)
    x/=10
    x2=int(x%10)
    x/=10
    x1=int(x%10)
    y3=int(y%10)
    y/=10
    y2=int(y%10)
    y/=10
    y1=int(y%10)
    #print("%d %d %d : guess %d %d %d"%(x1,x2,x3,y1,y2,y3))
    b=bull(x1,y1)+bull(x2,y2)+bull(x3,y3)
    c=bull(x1,y2)+bull(x1,y3)+bull(x2,y1)+bull(x2,y3)+bull(x3,y1)+bull(x3,y2)
    print("%d B and %d C"%(b,c))
    result=str(b) + str("B") +str(c)+str("C")
    #print(result)
    return result
def game(n1,n2):
    #Game code
    s1="0"
    s2="0"
    while s1!="3B0C" and s2!="3B0C":
        guess1=input("Player 1:Enter your guess ")
        s1=check(n2,guess1)
        guess2=input("Player 2:Enter you guess ")
        s2=check(n1,guess2)
    if s1=="3B0C" and s2=="3B0C":
        print("It's a Draw.")
    elif s1=="3B0C":
        print("Player 1 wins!!")
    else:
        print("Player 2 Congratulations!!")
    #print("Game works for 2-player mode")
def singleplayer():
    #code for single player mode
    print("Welcome to 1-player mode")
    check_unique=1
    while check_unique:
        cpu=randint(100,999)
        number=int(cpu)
        check_unique=no_repeat(number)
    #print("Random number is %d, phase clear"%(int(cpu)))
    s2="0"
    while s2!="3B0C":
        guess1=input("Player 1:Enter your guess ")
        s2=check(cpu,guess1)
    print("That's Correct!")   
    #Phase checked
def twoplayer():
    #code for two player mode
    print("Welcome to 2-player mode")
    print("Player 1: Enter a 3 digit number")
    p1=input("Enter your number ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")#Need better code to to this
    print("Player 2: Enter a 3 digit number")
    p2=input("Enter your number ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")#So that players cannot see each other's numbers
    game(p1,p2)
    #Phase checked
def checker(players):
    #code for checking valid input
    if int(players)==1 or int(players)==2:
        return True
    else:
        print("Invalid Input")
        return False
def Game_mode(players):
    #code to start game
    if int(players)==1:
            singleplayer()
    elif int(players)==2:
            twoplayer()
#Program start
print("Welcome to GuessGame")
print("In this game, the player shall try to guess the 3 digit number\nthe other player has in mind.\n(Cow will be denoted by C and means that there's a right number in the wrong place\n Bull will be denoted by B which means there's a right number in the right place)")  
play=1
while int(play):
    status=False
    while status==False:
        players=input("How many players are playing(1 or 2)?")
        status=checker(players)
        Game_mode(players)
    play=input("Play again?(1/0)")
#print("Checking Phase Clear")
