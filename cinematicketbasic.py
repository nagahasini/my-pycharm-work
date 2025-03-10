films={
    "Aa":{'tickets':4,'age':5},
    "Arjun Reddy":{'tickets':100,'age':18}
}

while True:
    choice=input("which film u wanna watch.." ).strip().title()
    if choice in films:
        age= int(input("enter your age: ").strip())
        if age<=films[choice]['age']:
            print("you cant watch the film ")
        else:
            print("you can watch the film")
            if films
    else:
        print("no such film available")