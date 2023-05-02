import check

real_pin = input("please give me the password of your safe. thank you!")
real_pin = int(real_pin)
check.set_real_pin(real_pin)
answer=check.check(real_pin)

assert answer == True, "please check the code"

