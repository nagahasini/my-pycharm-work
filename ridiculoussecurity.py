from emailslicing import output

users=['Hasini','Tan','Aasish','Sathvik']

while True:
    name = input("enter your name: ").strip().capitalize()
    if name in users:
        outputs="hello {}".format(name)
        print(outputs)
        remove=input("do u want to leave(y/n)").lower()
        if remove=='y':
            users.remove(name)
            print("come back soon:(")
            print(users)
        elif remove=='n':
            print("thanks for staying back")

    else:
        add=input("do u want to get added(y/n").lower()
        if add=='y':
            users.append(name)
        print("you are added")



