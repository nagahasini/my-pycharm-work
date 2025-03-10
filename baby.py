from random import choice
questions= ["why are you weird?","who is he","where is star"]
question=choice(questions)
answer=input(question).strip().lower()
while answer!="shut up":
    answer=input("why?").strip().lower()

print("fine...")