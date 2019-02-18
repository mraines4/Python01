# make blastoff counter with message at end
import time

num_count = int(input("gimme a numba fool "))

def num_num(entered):
    while entered > 20:
        entered=int(input('Try again, this time less than 20 '))
    while entered < 20 and entered >= 0:
        return (entered)
        entered = entered - 1
        time.sleep(1)
    return ("WE MADE IT YASSSS")

print(num_num(num_count))
