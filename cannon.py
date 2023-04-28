import math

# number_you_want_to_sqrt = float(input("which witch is which?"))

# calculate the distance for a given angle
def cal_distance(angle, speed, gravity, height):
    angle_pi = angle * math.pi / 180
    _vx = math.cos(angle_pi) * speed
    _vy = math.sin(angle_pi) * speed

    _a = _vy * _vy
    _b = 2*gravity*height
    _c = _vy + math.sqrt(_a + _b)
    _t = _c / gravity
    _e = _vx * _t
    return  round(_e, 3)

# test whether the cannon hit the target 
def test(angle, speed, gravity, height, distance):
    calculated_distance = cal_distance(angle, speed, gravity, height)

    if abs(calculated_distance-distance)<0.5:
        return "bingo"
    
    if calculated_distance<distance:
        return "too small"
    else:
        return "too large"

# test cal_distance: successful
# result = cal_distance(angle=19, speed=5, gravity=20, height=15)
# print(result)
# exit(0)

# test test: just considering simple cases.
# result = test(angle=-14, speed=13, gravity=9.82, height=15, distance=18.1)
# print(result)
# exit(0)

speed=30
gravity=9.55
height=15
distance=82.9

lower_bound=-90
upper_bound=45

result = test(lower_bound, speed=speed, gravity=gravity, height=height, distance=distance)
#print(result)
assert result=="too small", "Lower bound is too large"

result = test(upper_bound, speed=speed, gravity=gravity, height=height, distance=distance)
#print(result)
assert result=="too large" or result=="bingo", "Upper bound is too small"

if result=="bingo":
    print(f"i found it. {upper_bound}")
else:

    for i in range(200):

        # make the first guess
        guess=(upper_bound-lower_bound)/2+lower_bound
        #print(guess)

        result = test(guess, speed=speed, gravity=gravity, height=height, distance=distance)
        #print(result)

        if result=="too large":
            upper_bound=guess
        elif result=="too small":
            lower_bound=guess
        else:
            print (f"{lower_bound}--{upper_bound}")
            print(f"i found it: {guess}")
            break
    print (f"{lower_bound}--{upper_bound}")    