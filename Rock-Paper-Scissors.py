import random
def game():
    k=["Rock","Paper","Scissors"]
    cmp=random.choice(k)
    print("////ROCK-PAPER-SCISSORS GAME////")
    user=input("Enter your choice (rock,paper,scissors):").capitalize()
    print(cmp)
    if user==cmp:
        print("It's a tie!")
    elif(user=="Rock"):
        if(cmp=="Scissors"):
            print("Rock smashes scissors!")
            print("You loss!")
        else:
            print("Paper covers rock!")
            print("You loss!")
    elif user=="Paper":
        if(cmp=="Rock"):
            print("Paper covers rock!")
            print("You win!")
        else:
            print("Scissor cuts paper!")
            print("You loss!")
    elif user=="Scissors":
        if(cmp=="Paper"):
            print("Scissor cut paper!")
            print("You win!")
        else:
            print("Rock smashes scissor!")
            print("you loss!")    
    again=input("Do you want to play again?[Yes/No]:").capitalize()
   
game()
        
    