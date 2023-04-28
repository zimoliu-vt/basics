number_you_want_to_sqrt = float(input("which witch is which?"))
# test 
def test(x):
    if x*x==number_you_want_to_sqrt:
        return "bingo"
    elif x*x>number_you_want_to_sqrt:
        return "too large"
    else:
        return "too small"
result = test(1.414)
#print(result)

lower_bound=0
if number_you_want_to_sqrt>=1:
    upper_bound=number_you_want_to_sqrt
else:
    upper_bound=number_you_want_to_sqrt+1
    
result = test(lower_bound)
#print(result)
assert result=="too small", "Lower bound is too large"

result = test(upper_bound)
#print(result)
assert result=="too large" or result=="bingo", "Upper bound is too small"

if result=="bingo":
    print (f"{lower_bound}--{upper_bound}")
    print(f"i found it, sqrt-{number_you_want_to_sqrt}={number_you_want_to_sqrt}")
else:

    for i in range(200):

        # make the first guess
        guess=(upper_bound-lower_bound)/2+lower_bound
        #print(guess)

        result = test(guess)
        #print(result)

        if result=="too large":
            upper_bound=guess
        elif result=="too small":
            lower_bound=guess
        else:
            print (f"{lower_bound}--{upper_bound}")
            print(f"i found it, sqrt-{number_you_want_to_sqrt}={guess}")
            break
    print (f"{lower_bound}--{upper_bound}")    