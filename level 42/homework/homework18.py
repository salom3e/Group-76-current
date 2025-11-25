# 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", 
# თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.

nums = [10, 20, 30]

user = int(input("enter some integer: "))

if user in nums:
    print("Already in list")
else:
    nums.append(40)
    print(nums)
