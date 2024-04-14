import math

def dejong_1st(args):
    return sum([a**2 for a in args])


def dejong_2nd(args):
    return sum([(i + 1) * args[i]**2 for i in range(len(args))])


def schweffel(args):
    return sum([abs(args[i])**(i + 1) for i in range(len(args))])
