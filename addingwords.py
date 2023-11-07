
#https://open.kattis.com/problems/addingwords

word_dict = {}
run = True

while run:

    line = input().split()

    if line[0] == "def":
        word_dict[line[1]] = int(line[2])
    
    elif line[0] == "calc":
        try:
            result = word_dict[line[1]]
            for i in range(2, len(line)-1, 2):
                if line[i] == "+":
                    result += word_dict[line[i+1]]
                elif line[i] == "-":
                    result -= word_dict[line[i+1]]
                else:
                    result = "unknown"
                    break
            for key, value in word_dict.items():
                if value == result:
                    result = key
                    break
            print(" ".join(line[1:]), result)
        except:
            print(" ".join(line[1:]), "unknown")
    else:
        run = False
