# 11)შექმენი ფუნქცია ერთი პარამეტრით —password.

# თუ პაროლი უდრის "python123" → დააბრუნოს  "წვდომა დაშვებულია"

# სხვა შემთხვევაში → "არასწორი პაროლი"

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def word(password):
    if password == "python123":
        return "წვდომა დაშვებულია."
    else:
        return "არასწორი პაროლი!"

print(word("python123"))
print(word("html321"))
print(word("gaga36"))
print(word("praga26"))
print(word("python123"))
print(word("python123"))