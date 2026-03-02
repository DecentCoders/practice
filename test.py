def filtered(a):
    return a>5
l=[1,2,4,5,6,3,6]
new_l = list(filter(filtered, l))
print(new_l)