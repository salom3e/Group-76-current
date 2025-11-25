# 17)შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", 
# შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.

foods = ["bread", "milk"]

if len(foods) == 2:
    foods.append("cheese")
    print(foods)
else:
    foods.append("meat")
    print(foods)
