# while loops
# add   names into list till length is three
# L=[]
# while len(L)<3:
#     names=input("enter names").strip().capitalize()
#     L.append(names)
#
# print("limit of list is done")
# print(L)
from start import ranges

# for loop
# for i in range(1,11,2):
#     print(i)

# consonents=0
# vowels=0
# name= input("enter name")
# for i in name:
#     if i.lower() in "aeiou":
#         vowels=vowels+1
#     elif i.lower()=="":
#         pass
#     else:
#         consonents=consonents+1
#
# print("vowels are {} and cosonants are {}".format(vowels,consonents))


# vowels and consonants in list of names in dictionary
# names={
#     "male":['aasish','tansu','sathvik',],
#     "female":['hasini','istha','manasa','hjk']
#
# }
# consonant=0
# vowel=0
# for i in names.keys():
#     for name in names[i]:
#         if('a'or'e'or'i'or'u')in name:
#             print(name)
#         for j in name:
#             if j in "aeiou":
#                 vowel=vowel+1
# print(vowel)

# ******************************************************************************************************************
# LIST COMPREHENSIONS
evennum= [x for x in range(1,101) if(x%2==0)]
print(evennum)





