name = input()

a, b, c = [int(input()) for i in range(3)]

if a-b >=0:
    print("VEIT EKKI")

elif a-b < 0:

    if c < 0:
        print("jedi")
    else:
        print("sith")