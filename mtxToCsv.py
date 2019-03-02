import sys
if((len(sys.argv) < 2) and (len(sys.argv) > 3)):
    print("Usage: python3 mtxToCsv.py <fileInput> <fileOutput>")
    exit()
try:
    mtx = open(sys.argv[1], 'r')

    try:
        csv = open(sys.argv[2], 'xa')
    except:
        csv = open(sys.argv[2], 'a')
    L = list() 
    j = 0
    while True:
        s = ","
        j += 1
        data = mtx.readline()
        L = data.split() 
        if(data == ''):
            print('eof')
            break
        s = s.join(L)
        print(s)
        csv.write(s)
        csv.write('\n')
        L.clear()

finally:
    mtx.close()
    csv.close()
