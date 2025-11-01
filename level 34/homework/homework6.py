# 6) <= Boss Level =>
# შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
# --> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი

strings = ["Sakartvelo", "Xelovneba", "babylon", "club"]

longest = strings[0]

for i in strings:
    if len(i) > len(longest):
        longest = i

print(longest)
