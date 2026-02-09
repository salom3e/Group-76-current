# 4)შექმენი ფუნქცია ერთი პარამეტრით — age.

# თუ ასაკი არის 18 ან მეტი, დააბრუნოს:
# სრულწლოვანი ხარ

# სხვა შემთხვევაში:
# არ ხარ სრულწლოვანი

def number(age):
    if age >= 18:
        return "You're adult!"
    elif age < 18 and age > 12:
        return "You're a teenager."
    else:
        return "You're underage <3"
    
print(number(int(input("enter your age: "))))