arr=[]
def line(n):
    while n>0:
        print("================================")
        n-=1
while True:
    n=int(input())
    if n in arr:
        arr.append(n)
        line(2)
        print(arr,"\n")
        print(f"The duplicate number is {n}")
        line(2)
        quit()
    else:
        arr.append(n)