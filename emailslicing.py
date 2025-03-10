email_adress=input("enter email address: ")
username= email_adress[:email_adress.index("@")]
domain=email_adress[(email_adress.index("@")+1):]
out="your username is '{1}' with domain as '{0}' "
output=out.format(domain,username)
print(output)