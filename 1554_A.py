n = int(input())

while (n>0):
    l = int(input())
    
    result = 0 
    
    input_str = input()
    
    my_list = []
    input_list = input_str.split()
    
    for i in range(l):
        
        my_list.append(int(input_list[i]))
        
        if(i ==1):
            result = my_list[0]*my_list[1]
        
        elif(i>1):
            if((my_list[i]*my_list[i-1])> result):
                result = my_list[i]*my_list[i-1]
        
        
    print(result)  
    n-=1
    