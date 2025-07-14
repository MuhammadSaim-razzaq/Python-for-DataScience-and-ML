spam = False;


name = input("enter your name: ")
age = input("enter your age: ")
birth_year = int(input("enter your birth year: "))



if "win" in name:
    name = name.replace("win","Don't spam")
elif "lottery" in name:
    name = name.replace("lottery","Don't span")

details = f'Name: {name} \nage: {age} \nBirth year: {birth_year} '

if len(age)>3 or birth_year<1940 :
    spam = True
if not spam:
    print(details)
    print(f'The length of your detail is {len(details)}')
else :
    print(f"Don't spam")

