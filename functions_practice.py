def hello():
    print('Hello')

hello()



def pack(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

pack("beans", "spice", "deoderant")



def eat_lunch(arg):
    if len(arg) == 0:
        print("I'm a hungry boi")
    else:
        for i in range(len(arg)):
            if i == 0:
                print(f"First I eat {arg[0]}")
            else:
                print(f"Next I eat {arg[i]}")

faud = ["apple", "banana", "pear", "brownie"]

eat_lunch(faud)
        
