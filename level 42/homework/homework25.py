# 25) შექმენი სია mix = ["x", "y", "z"]. extend()-ით დაუმატე [1, 2, 3]. შემდეგ მომხმარებელს შემოატანინე ასო; თუ ეს ასო არის სიაში, 
# remove()-ით წაშალე პირველად როცა შეგხვდება და დაბეჭდე "Removed", თუ არა — დაბეჭდე "No such element". ბოლოს დაბეჭდე სია.

mix = ["x", "y", "z"]

add = [1, 2, 3]

mix.extend(add)

user = input("enter letter: ")
if user in mix:
    mix.remove(user)
    print("Removed")
else:
    print("No such element")
print(mix)

