import time
sides, cut_heigth, cut_width = [int(x) for x in input().split()]

volume = 4*(max(cut_heigth, sides-cut_heigth) * max(cut_width, sides-cut_width))
print(volume)
