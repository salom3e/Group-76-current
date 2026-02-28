# You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(num):
    sum = 0
    for i in num:
        if i > 0:
            sum += i
        i += 1
    return sum