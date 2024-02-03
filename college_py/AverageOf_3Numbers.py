# # eval is to convert the number (string) to number (int)
# # type tells 
# '''
#   This is a multiple line comment
# '''
# num1 = eval(input("Enter number: "))
# num2 = eval(input("Enter number: "))
# # print("Type is : ",type(num2)) -> It will 
# avg = (num1+num2)/2
# print("Type is : ",type(num2))
# print("avg is ", avg)

import time
start = time.time()

list = [1,2,3,4,5]
del list

end = time.time()

print("Time taken: ", format(end-start))