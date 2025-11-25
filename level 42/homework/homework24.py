# 24)შექმენი სია nums = [2, 4, 6].  მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი დადებულია, append()-ით დაამატე; 
# თუ 0-ია ან ნაკლებია ნულზე, დაბეჭდე "Only positive allowed". ბოლოს დაბეჭდე სია.

nums = [2, 4, 6]

user = int(input("enter number: "))

if user > 0:
    nums.append(user)
else:
    print("Only positive allowed")
print(nums)
