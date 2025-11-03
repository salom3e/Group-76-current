# 1) შემოაყვანიეთ მომხმარებელს რაღაცა სიტყვა:
# -> შეამოწმეთ არის თუ არა 'a' ან 'A' ამ სიტყვაში/ტექსტში
# -> შეამოწმეთ თუ არ არის სიტყვა 'car' ამ სიტყვაში/ტექსტში

word = input("enter some word: ")
if "a" or "A" in word:
    print("there is 'a' or 'A' in your word")
else:
    print("there is not 'a' or 'A' in your word")

if "car" not in word:
    print("there's no 'car' in your word")
else:
    print("there is 'car' in your word")