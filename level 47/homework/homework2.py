# 2) შექმენით 2 სია - სახელების და გვარების. for ციკლის და ფუნქციების გამოყენებით სახელების სიაში ყველა სახელის ყველა ასო გახადეთ 
# დიდი, ხოლო გვარების სიაში ყველა გვარის თითოეული ასო გახადეთ პატარა, სულ ბოლოს კი გააერთიანეთ სახელების სია გვარის 
# სიასთან და დაპრინტეთ მიღებული შედეგი.


names = ["Meryl", "Julia", "Audrey", "gwen", "marilyn", "Monica", "nicole", "anne", "scarlett"]
last_names = ["StrEEp", "Roberts", "HEPBURN", "stefani", "MONROE", "BELlUCCI", "hatHaway", "johansSon"]

for i in range(len(names)):
    names[i] = names[i].upper()

for i in range(len(last_names)):
    last_names[i] = last_names[i].lower()

both = names + last_names

print(both)
