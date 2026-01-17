# 4) მომხმარებელს შემოატანინეთ პაროლი, თუ პაროლის სიგრძე არის 6-ზე ნაკლები, მაშინ თავიდან შემოატანინეთ ახალი პაროლი, როცა 
# პაროლის სიგრძე იქნება 6 ან 6-ზე მეტი, გააჩერეთ ციკლი და დაპრინტეთ "Your password is correct!" გამოიყენეთ while ციკლი.

# password = input("enter password: ")

# if len(password) < 6:
#     password = input("enter password: ")
# elif len(password) == 6 or len(password) > 6:
#     print("your password is correct!")

password = input("enter password: ")

while len(password) < 6:
        password = input("enter password: ")
print("your password is correct!")

    