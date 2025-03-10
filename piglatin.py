# pig latin is funny way of adding ay to end of word by reversing the word and we dont reverse the word if it starts with vowel
# ************ we have method called SPLIT to split words in string into list
#                we use JOIN to join words ex: "".join()

input_sentence=input("enter normal language sentence: ").strip().lower()
words=input_sentence.split()
new_words=[]
for word in words:
    if word[0] in "aeiou":
        l_word=word+'yay'
        new_words.append(l_word)
    else:
        vowel_finder=0
        for i in word:
            if i not in "aeiou":
                vowel_finder=vowel_finder+1
            else:
                break
        portion=word[vowel_finder:]
        cons=word[:vowel_finder]
        ll_word=portion+cons+"yay"
        new_words.append(ll_word)


new_sentance= " ".join(new_words)
print(new_sentance)







