import random

print("Hello there!!")
print("I want to play a game with you!")
print("It is a 'Rock, Paper, Scissors' game.")
print("If you want to stop simply just type 'x'.")
rps = ['Rock' , 'Paper' , 'Scissors']
abc = rps[random.randint(0,2)]
while True:
    print("What is your weapon?")
    ans = str(input())
    if ans != abc:
        if ans == "x":
            print("Thanks for playing!")
            break
        elif ans == "Rock":
            if abc == "Paper":
                print("Yes! I win! (Paper)")
                abc = rps[random.randint(0,2)]
            else:
                print("Man, you win! (Scissors)")
                abc = rps[random.randint(0,2)]
        elif ans == "Paper":
            if abc == "Rock":
                print("Man, you win! (Rock)")
                abc = rps[random.randint(0,2)]
            else:
                print("Yes! I win! (Scissors)")
        elif ans == "Scissors":
            if abc == "Paper":
                print("Man, you win! (Paper)")
                abc = rps[random.randint(0,2)]
            else:
                print("Yes, I win! (Rock)")
                abc = rps[random.randint(0,2)]
        else:
            print("A,A,A.. You cheating! Go to Hell!!!!")
            break
    else:
        print("Draw (" + abc + ")")
