

def number_to_text(number):
  pass

if __name__ == "__main__":
  numbers = [1, 2, 7, 10, 14, 25, 37, 48, 59, 99, 101, 134, 157, 587, 10547, 4927854]
  for number in numbers:
    print(number_to_text(number))

#How to pronunce
nums = ("không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín")
cols = ("tỉ","trăm","mươi","triệu","trăm","mươi","nghìn","trăm","mươi","")


for input in range (1000001,1000002):
    
    str_input = str(input)
        result = []
            for i in range(1,len(str_input)+1):
                a=nums[int(str_input[-i])]+ " " + cols[-i]
                    if a == "một mươi":
                        a = "mười"
                            if a == "không mươi":
                                a = "lẻ"
                                    
                                    if "mươi" in a:
                                        result[-1] = result[-1].replace("một","mốt")
                                            result[-1] = result[-1].replace("năm","lăm")
                                                
                                                #print(result[-1])
                                                
                                                
                                                elif a in ["không nghìn","không triệu", "không tỉ"]:
                                                    a = a.replace( "không ", "")
                                                        
                                                        result.append(a)
                                                            if i > 1:
                                                                if result[1] != "":
                                                                    if result[0] == "không ":
                                                                        result[0] = ""
                                                                            if 654 == 0:
                                                                                nghin -> x
                                                                                    if nghin ko co:
                                                                                        tram -> x 
                                                                                            if tram ko co:
                                                                                                le -> bo 
                                                                                                    
                                                                                                    #print(result)
                                                                                                    
                                                                                                    print(result)
# result.reverse()
# print(" ".join(result))

# result.reverse()
# print(" ".join(result))


#hàng đơn vị
#0  không
#1  một
#2  hai
#3  ba
#4  bốn tư
#5  năm lăm
#6  sáu
#7  bảy
#8  tám
#9  chín
#10 mười

#mươi
#trăm
#nghìn
#triệu
#tỉ

#Read the number

input must be in this form [0-9]+

#number -> string
str_input = str(input)

#read from the back of the string
for i in (1,len(str_input))
 str_input[-i] -> [1st]

# first element -> hang don vi
# second element -> hang chuc
# ...
# until there is no more element

rule to pronounce
[10th] tỉ [9th] tram [8th] muoi [7th] trieu [6th] tram [5th] muoi [4th] nghin [3rd] tram [2nd] muoi [1st]



for i in range(1,len(str_input)+1):
    print(str_input[-i])

