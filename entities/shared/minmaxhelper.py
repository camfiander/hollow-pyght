def maxMag(*args):
    if(args[0] < 0):
        return min(args)
    else:
        return max(args)

def minMag(*args):
    if(args[0] < 0):
        return max(args)
    else:
        return min(args)

   