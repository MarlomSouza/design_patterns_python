def metodo(*args):
    iter()

    for length in args:
        print(length)
    

def color(red, green, blue, **kwargs):
    print("r=", red)
    print("g=", green)
    print("b=", blue)
    print(kwargs)

k = {'redi': 21, 'blue': 12,'green': 10, 'alpa': 13}

# color(**k)

def concatArray():
    monday = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sunday = [1, 2, 3, 4, 5, 6, 7, 8,10]

    for target_list in zip(monday, sunday):
        print(target_list)

concatArray()
    


