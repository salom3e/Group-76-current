# 4) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 4-ზე მეტი სიგრძეში ან 
# დგანან კენტ ინდექსზე. გამოიყენეთ remove() ფუნქცია.

words = ["music", "disco", "ball", "glitter", "gems", "Stage", "artist", "DJ", "dance"]

for i in range(len(words) -1, -1, -1):
    if len(words[i]) > 4 or i % 2 == 1:
            words.remove(words[i])
print(words)