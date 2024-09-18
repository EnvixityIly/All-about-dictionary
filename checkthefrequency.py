test_dict = {
    'Codingal' : 3,
    'Is'  : 2,
    'best' : 2,
    'for' : 2,
    'coding' : 1,

}

print ("The org dictionary :  + str(test_dict)")

k = int(input("Enter the frequency :"))
res  = 0

for key in test_dict:
    if test_dict[key] == k:
        res = res + 1

print("Frequency of K is : " , res)