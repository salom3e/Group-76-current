def multiplication_table(number):
    
    result = ""
    for i in range(1, 11):
        result += str(i) + " " + "*" + " " + str(number) + " " + "=" + " " + str(i * number)
        if i != 10:
            result += "\n"
    return result
        
print(multiplication_table(5))


# def multiplication_table(number):
    
#     result = ""
#     for i in range(1, 11):
#         result += str(i) + " * " + str(number) + " = " + str(i * number)
#         if i != 10:
#             result += "\n"
#     return result
        

