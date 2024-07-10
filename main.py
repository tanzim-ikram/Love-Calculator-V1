# LOVE CALCULATOR - V1

print("Welcome to the Love Calculator!")
your_name = input("Enter your name: ").lower()
partner_name =input("Enter your partner's name: ").lower()

for x in your_name:
    if x in partner_name:
        your_name = your_name.replace(x, "")
        partner_name = partner_name.replace(x, "")
        
name = your_name + partner_name
# print(name)

length = len(name)
# print(length)
remainder = length % 6
# print(remainder)

if remainder==0:
    print("Relationship status: Friends")
elif remainder==1:
    print("Relationship status: Lovers")
elif remainder==2:
    print("Relationship status: Affection")
elif remainder==3:
    print("Relationship status: Marriage")
elif remainder==4:
    print("Relationship status: Enemy")
elif remainder==5:
    print("Relationship status: Siblings")
else:
    pass