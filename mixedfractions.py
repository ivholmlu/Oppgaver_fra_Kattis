
# https://open.kattis.com/problems/mixedfractions
run = True

while run:
    numerator, denominator = map(int, input().split())
    if numerator == 0 and denominator == 0:
        run = False
    else:
        whole = numerator // denominator
        numerator = numerator % denominator
        print(whole, numerator, "/", denominator)

