import math

def dejong_1st(args):
    return sum([a**2 for a in args])


def dejong_2nd(args):
    return sum([100*(args[i]**2 - args[i+1])**2 + (1 - args[i])**2 for i in range(len(args) - 1)])

def schweffel(args):
    return sum([-args[i] * math.sin(math.sqrt(abs(args[i]))) for i in range(len(args))])


def func_limits(func):
    if func.__name__ == 'schweffel':
        return (-500, 500)
    return (-5,5)