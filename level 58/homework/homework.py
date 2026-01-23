# 1) შექმენით რიცხვებით სავსე სია, ამ სიიდან იპოვეთ და დაპრინტეთ მეორე ყველაზე დიდი რიცხვი, გამოიყენეთ for ციკლი.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

max = nums[0]

for i in nums:
    if i > max:
        max = i

max_2 = nums[0]

for i in nums:
    # if i != max and i > max_2:
    if i != max:
        max_2 = i
print(max_2)

