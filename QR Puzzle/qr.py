kf = 'key'
qf = 'encrypted.qr'

def main():
    key = []
    with open(kf,'r') as key_file:
        for line in key_file:
            key.append(line)
    key = key[:-1]

    code = []
    with open(qf,'r') as code_file:
        for line in code_file:
            for c in line[:-1]:
                code += c

    ans = decrypt(key, code)
    print_code(ans)


def encrypt(key, qr):
    enc = qr
    for line in key[::-1]:
        mode = int(line[0])
        x = int(line[3:line.find(',')])
        y = int(line[line.find(',')+1:-2])
        
        if mode == 0:
            x2 = x-1
            y2 = y
        elif mode == 1:
            x2 = x+1
            y2 = y
        elif mode == 2:
            x2 = x
            y2 = y-1
        elif mode == 3:
            x2 = x
            y2 = y+1

        enc[y*25+x]   = str(int(qr[y*25+x]) + int(qr[y2*25+x2]))
        enc[y2*25+x2] = str(int(qr[y*25+x]) - int(qr[y2*25+x2]))
        enc[y*25+x]   = str(int(qr[y*25+x]) - int(qr[y2*25+x2]))
    return enc


def decrypt(key, qr):
    enc = qr
    for line in key:
        mode = int(line[0])
        x = int(line[3:line.find(',')])
        y = int(line[line.find(',')+1:-2])
           
        if mode == 0:
            x2 = x-1 
            y2 = y 
        elif mode == 1:
            x2 = x+1 
            y2 = y 
        elif mode == 2:
            x2 = x 
            y2 = y-1 
        elif mode == 3:
            x2 = x 
            y2 = y+1 

        enc[y*25+x]   = str(int(qr[y*25+x]) + int(qr[y2*25+x2]))
        enc[y2*25+x2] = str(int(qr[y*25+x]) - int(qr[y2*25+x2]))
        enc[y*25+x]   = str(int(qr[y*25+x]) - int(qr[y2*25+x2]))
    return enc


def print_code(code):
    for i in range(25):
        print(''.join(c for c in code[25*i:25*(i+1)]))


if __name__ == "__main__":
    main()
