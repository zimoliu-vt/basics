import check

num = input("please give me the password of your safe. thank you!")
num = int(num)
check.set_real_pin(num)
answer=check.check(num)

assert answer == True, "please check the code"