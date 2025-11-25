# 21)შექმენი სია pets = ["cat", "dog", "hamster"].  მომხმარებელს შემოატანინე შინაური ცხოველის სახელი. თუ იგი არის სიის შიგნით, 
# remove()-ით ამოშალე და დაბეჭდე "Removed", თუ არა — დაბეჭდე "Not found" და სია უცვლელი დატოვე; საბოლოოდ დაბეჭდე სია.

pets = ["cat", "dog", "hamster"]

user_pet = input("enter any pet: ")

if user_pet in pets:
    pets.remove(user_pet)
    print("Removed")
else:
    print("Not found")
print(pets)