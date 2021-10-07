import random
points: int= 0
player: str = ""
__author__ = "730402368"
NAMED_CONSTANT = print("\U0001f600")
def randomNumberMaker():
    randomNumber = random.randint(1,200)
    return randomNumber


def greet()-> None:
    global player
    player = str("Hi, What's your name?")
    explanation= " !, in this game you have to guess an integer from 1 t0 200 that I am thinking of "
    greeting = "nice to meet you, "+ player+ f"(explanation)"

def askPlayerForInteger(reply = player+ " , Guess an integer from 1 to 200: "):
    playerInteger =int (input(reply))
    return playerInteger

def inspectPlayerInteger(playerInteger, randomNumber):
    global points
    if playerInteger > randomNumber:
        return "too high"
    if playerInteger < randomNumber:
        return "too low"
    else:
        return "correct! Yay!" + ("\U0001f600") 
def main():
    global points
    playerWins = False 

    while playerWins == True:
        points = 0
        randomNumber = randomNumberMaker()
        playerInteger = askPlayerForInteger()
        points += 1
        reply = inspectPlayerInteger(playerInteger, randomNumber)

        while reply != "correct! Yay!":
            print(reply)
            playerInteger = askPlayerForInteger("Take another stab at it!")
            reply = inspectPlayerInteger(playerInteger, randomNumber)
            print(reply, "it took you ", points, " to guess correctly")   
        print(reply)

if __name__ == "__main__":
 main()
 print("None")







