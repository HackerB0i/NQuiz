import os
import random
import math

"""
python study script
"""

flashcards = {}
terms_only = []
definitions_only = []
temp_learned = []
learned = open("learned.txt", "a", encoding="utf8") 
terms = open('terms.txt', 'r', encoding="utf8")

for line in terms:
    stripped_line = line.strip().split(":")
    flashcards[stripped_line[0]] = stripped_line[1]
    terms_only.append(stripped_line[0])
    definitions_only.append(stripped_line[1])
    #learned.write("0\n")
    temp_learned.append("0\n")

def get_percentage_learned():
    learned = open("learned.txt", "r", encoding="utf8") 
    learned_amt = 0
    data = learned.readlines()
    for term in data:
        if term == "1\n":
            learned_amt += 1
    return [round((learned_amt / len(terms_only)) * 100, 2), learned_amt]

def change_learned_line(line, value):
    data = []
    with open('learned.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        data[line] = f"{value}\n"
    with open('learned.txt', 'w') as file:
        file.writelines(data)

def is_learned(line):
    data = []
    with open('learned.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
    return data[line] == "1\n"

while True:
    os.system('cls')
    print("NQuiz: free in-console flashcard memorization")
    print("type <learn> to get started, or <reset> to reset your progress!")
    command = input()
    if command == "learn":
        while True:
            os.system('cls')
            print(f"percent learned: {get_percentage_learned()[0]}% ({get_percentage_learned()[1]}/{len(terms_only)}) | hint: <h>")
            random_index = random.randint(0, len(terms_only)-1)
            while True:
                random_index = random.randint(0, len(terms_only)-1)
                if not is_learned(random_index):
                    break
            print(flashcards[terms_only[random_index]])
            learn_command = input()
            correct = False
            if learn_command == "h":
                print(f"hint: {terms_only[random_index][0]}...")
                learn_command = input()
                if learn_command.lower() == terms_only[random_index].lower():
                    print("correct!")
                    correct = True
                else:
                    print(f"incorrect! the answer is: {terms_only[random_index]}\nactually correct? input <c> to mark as correct")
                learn_command = input()
                if learn_command == "c" or correct:
                    change_learned_line(random_index, 1)
            else:
                if learn_command.lower() == terms_only[random_index].lower():
                    print("correct!")
                    correct = True
                else:
                    print(f"incorrect! the answer is: {terms_only[random_index]}\nactually correct? input <c> to mark as correct")
                learn_command = input()
                if learn_command == "c" or correct:
                    change_learned_line(random_index, 1)
    elif command == "reset":
        with open('learned.txt', 'w', encoding="utf8") as file:
            file.writelines(temp_learned)