def func123(x, y):
    return x+y

def concatenate_lists(l1,l2):
    return l1 + l2

def create_dict(l1,l2):

    t = tuple(zip(l1,l2))

    d = dict((x,y) for x,y in t)

    return d
        
