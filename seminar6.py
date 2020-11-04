def compare_function(x, y):
    if x>y:
        return 1;
    elif x==y:
        return 0;
    elif x<y:
        return -1;

print(compare_function(10, 20))
print(compare_function(0, -15))
print(compare_function(10, 10))