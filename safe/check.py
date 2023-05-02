g_real_pin = None

def set_real_pin(real_pin):
    global g_real_pin
    g_real_pin = real_pin

def check(pin):
    if pin==g_real_pin:
        print("...")
        return True
    else:
        return False