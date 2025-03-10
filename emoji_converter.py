message = input("> : ")
emojis = {
    "happy": '😊',
    "sad": '🥲'
}

words = message.split()
output = ''

for word in words:
    if word in emojis:
        output += emojis[word]  # Append the emoji if the word is found
    else:
        output+=word

print(output.strip())  # Strip to remove the trailing space

#alt= emojis.get(word,word)