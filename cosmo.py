import random
import os
# from datetime import datetime

print("Hello I am your personal assistant Cosmo. \n"
      "What is your name")
os.system("say 'Hello I am your personal assistant cosmo. '")
os.system("say 'What is your name'")

name = input(">>> ")
os.system("say 'Hello'" + name)
print("You can ask me anything or use my commands. Type help if you need to see "
      "a list of my commands")


# commands
greetings = ['hi', 'hello', 'hi there', 'hey', 'sup', 'howdy']
farewells = ['bye', 'goodbye', 'farewell', 'later']
questions = ['how are you', 'how are you doing', 'how are you today']
feelings = ['I am feeling great', 'I am feeling good', ' I am feeling awesome', 'I am feeling happy',
            'I am feeling excited']


# returns a similar string
def randomize(y):
    rand = random.choice(y)
    print("Cosmo: " + str(rand))
    os.system("say " + str(rand))


# checks if in database
def convo(x):
    if x in greetings:
        randomize(greetings)
    elif x in farewells:
        randomize(farewells)
    elif x in questions:
        randomize(feelings)
        randomize(questions)
    else:
        print("Cosmo: Error. Phrase is not recognized")
        os.system("say 'error. phrase is not recognized'")


while True:
    text = input(name + ": ")
    convo(text)
