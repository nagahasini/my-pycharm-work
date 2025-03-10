import random  

# Input from the user
gamer_name = input("Enter gamer name: ")
health = int(input("Current health: "))
difficulty_level = input("Enter difficulty level (easy/medium/hard): ")

# Adjust health based on difficulty level
if difficulty_level == 'medium':
    health = health / 2
elif difficulty_level == 'hard':
    health = health / 3

# Ensure health is less than 100 before generating random health
if health < 100:
    random_health = random.randint(int(health), 100)  # Cast health to int for randint
    health = health + random_health
else:
    print("Health exceeds 100")

# Print final health
print("After health potion, health is " + str(int(health)))
