# built-in functions - ფუნქციაში ფუნქციის ჩაშენება. მაგ: print(type(26)), print ფუნქციის არგუმენტი


# string functions: 

# .lower() - აპატარავებს ასოს. არ გადაეცემა არგუმენტი.

#name = "salome"
#print(name.lower())

#Name = "sandro"
#lowered = Name.lower()
#print(lowered)


# .upper() - პირიქით

#surname = "luka"
# upperred = surname.upper()
# print(upperred)



# .capitalize() - სტრინგის პირველ ასოს ადიდებს

#name = "salome"
#capitalized = name.capitalize()
#print(capitalized)


# .find() - მარტო ამას გადაეცემა არგუმენტები (ყველა ფუნქციას არგუმენტი გადაეცემა ფრჩხილებში). პოულობს არგუმენტად გადაცემული
# ასოს იდექსს.

# name = "gigi"
# found = name.find("g")
# print(found)


# split.() - ხლიჩავს სტრინგს და აუცილებლად გადაჰყავს სიაში. 

# sentence = "unda vwamot wavedit"

# sentence.split() --> sentence.split(" ") - ფრჩხილებში იგულისხმება სფეისი, თუ მნიშვნელობა ჩვენით არ გადავეცით, ამიტომ 
# სფეისი სადაც შეხვდება, გაწყვეტს და სფეისამდე გავლილ ასოებს ჩაამატებს სიაში, როგორც სიის ელემენტი. 

# sentence = "unda vwamot wavedit"
# print(sentence.split())