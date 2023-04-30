print("write,table or house")
input_user=input("")
if input_user=="table":

    print("how ,many?  (input must>0)")    
    input_num=input("")
    input_num=int(input_num)
    anser=4*input_num+2

elif input_user=="house":

    print("how ,many?  (input must>0)")
    input_num=input("")
    input_num=int(input_num)
    anser=1+5*input_num

else :
    assert False

print(anser)