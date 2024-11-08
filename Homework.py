space=" "
input=int(input("Enter the number of rows you want: "))
star="*"

star2=star

while input>0:
    space=space *(input-1)
    print(space + star, end=" ")
    print()
    star=star+"*"
    space=" "
    input=input-1