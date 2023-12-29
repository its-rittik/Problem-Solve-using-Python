n = input()
input_list = n.split()
number = int(input_list[0])

for i in range(int(input_list[1])):
    if(number%10==0):
         number //=10
    else:
        number-=1
print(number)