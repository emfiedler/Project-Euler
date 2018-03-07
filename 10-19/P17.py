#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

n2w = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "onethousand"}

nd = "and"

#repeating 1-9
sa = 0
for i in range(1, 10):
    sa += len(n2w[i])*9

#repeating 10-100 in steps of 10
sb = 0
for i in range(20, 100, 10):
    sb += len(n2w[i])*10

#repeating teens
se = 0
for i in range(10, 20):
    se += len(n2w[i])

print((sa+sb+se)*9+(int(sa/9))*100+(len(n2w[100])*9)+(len(n2w[100])+len(nd))*891+len(n2w[1000])+(sa+sb+se))
