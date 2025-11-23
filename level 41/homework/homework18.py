# 18)შექმენი სია:

# names = ["goga", "saba", "luka"]


# მომხმარებელს შემოატანინე ამ სამიდან რომელიმე სახელი შეინახე ცვლადში და remove()-ით წაშალე მომხმარებლის შემოტანილი 
# სახელი სიიდან.

# დაბეჭდე სია რომ გაიგო მართლა ამოიშალა თუ არა


names = ["goga", "saba", "luka"]

names_user = (input("enter name - goga, saba or luka: "))
names.remove(names_user)
print(names)


