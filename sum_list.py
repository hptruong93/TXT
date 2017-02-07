def sum_list(input):
    # input
    k = 2
    #calculate the first k pairs
    sum_pairs = [None] * k
    while len(input) > 1: 
        for i in range (k):
            if 2*i > len(input)-1: #out
                pass
            elif 2*i == len(input)-1:# calculate first numbers
                sum_pairs[i] = input[2*i]
            elif 2*i < len(input)-1: #calculate both numbers
                #print(i,len(sum_pairs))
                sum_pairs[i] = input[2*i] + input [2*i+1]
        
        #replace the k+1, ... 2k with the results above
        for i in range (k):
            if k+i < len(input):
                if len(input) >= 2*k:
                    input[k+i] = sum_pairs[i]
                else:
                    input[len(input)//2+i] = sum_pairs[i]
                    
        #repeat calculate from k+1 ... k+2k until n
        if len(input) >= 2*k:
            input = input[k+1:]
        else:
          input = input[len(input)//2:]
        print(input)
    return input[0]
        #terminate when only one pair left. return the sum of that pair

print(sum_list([1,2,3,4,5]))
