import check
import guessing
real_pin = input("please give me the password of your safe. thank you!")

check.set_real_pin(real_pin)

guessing.guessing(4)