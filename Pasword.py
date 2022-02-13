import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "0123456789"
symbols="[]{}()*;/,._-"
all = lower + upper +number +symbols
length = 16
password ="".join(random.samplef (all,length))
print(password)
