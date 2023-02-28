import random

class Joke:
    def __init__(self, newPrompt, newAnswer):
        self.__Prompt = newPrompt
        self.__Answer = newAnswer

    def PrintRandomJoke(self):
        guess = input(self.__Prompt)
        print(self.__Answer)


jokes = []

try:
    f = open("DadJokes.txt", "r")
    while True:
        promptLine = f.readline().strip()
        if promptLine == "":
            break
        answerLine = f.readline().strip()
        jokes.append(Joke(promptLine, answerLine))
    f.close()
except FileNotFoundError:
    print("File not found.")

thisJoke = random.choice(jokes)
Joke.PrintRandomJoke(thisJoke)