ROLLER = [['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J'],
            ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
            ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
            ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B'],
            ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']]
REVERSE_ROLLER = [['U', 'W', 'Y', 'G', 'A', 'D', 'F', 'P', 'V', 'Z', 'B', 'E', 'C', 'K', 'M', 'T', 'H', 'X', 'S', 'L', 'R', 'I', 'N', 'Q', 'O', 'J'],
            ['A', 'J', 'P', 'C', 'Z', 'W', 'R', 'L', 'F', 'B', 'D', 'K', 'O', 'T', 'Y', 'U', 'Q', 'G', 'E', 'N', 'H', 'X', 'M', 'I', 'V', 'S'],
            ['T', 'A', 'G', 'B', 'P', 'C', 'S', 'D', 'Q', 'E', 'U', 'F', 'V', 'N', 'Z', 'H', 'Y', 'I', 'X', 'J', 'W', 'L', 'R', 'K', 'O', 'M'],
            ['H', 'Z', 'W', 'V', 'A', 'R', 'T', 'N', 'L', 'G', 'U', 'P', 'X', 'Q', 'C', 'E', 'J', 'M', 'B', 'S', 'K', 'D', 'Y', 'O', 'I', 'F'],
            ['Q', 'C', 'Y', 'L', 'X', 'W', 'E', 'N', 'F', 'T', 'Z', 'O', 'S', 'M', 'V', 'J', 'U', 'D', 'K', 'G', 'I', 'A', 'R', 'P', 'H', 'B'],]
ROLLER_START = ['H','D','X']#起始位置
ROLLER_ARROW = ['R','F','W','K','A']#指針位置
PLUGBOARD = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#接線板
UKW_B = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']#反射器
PLAINTEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"#明文

choose_roller = [0,0,0]

#只需改明文跟猜密文中有什麼字串

def reflector(list, n):
    return list[n]

def roller(ROLLER_LIST, start, turn, in_out, input):
    if in_out == 1:#in
        index = (start + turn) % 26
        c = ord(ROLLER_LIST[index])-65
        interval = 26-(start-c) if (start-c>0) else (c-start)#從起始位置到目標位置的位移量
        return interval
    elif in_out == 2:#out
        index = (start + turn) % 26
        c = ROLLER_LIST.index(chr(index+65))#找轉盤的第幾個位置是起始位置位移後的字母
        interval = 26-(start-c) if (start-c>0) else (c-start)#從起始位置到目標位置的位移量
        return interval
    else:
        return PLAINTEXT[ROLLER_LIST.find(input)]

def keyRead():
    f = open('key.txt', 'r')
    choose_roller[0] = int(f.read(1)) - 1
    choose_roller[1] = int(f.read(1)) - 1
    choose_roller[2] = int(f.read(1)) - 1
    f.read(1)
    ROLLER_START[0] = f.read(1)
    ROLLER_START[1] = f.read(1)
    ROLLER_START[2] = f.read(1)
    f.read(1)
    PLUGBOARD = f.read(26)

            
def reverseList():
    REROLLER = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]]
    for x in range(5):
        for index, i in enumerate(ROLLER[x]):
            REROLLER[x][DEFAULT.find(i)] = DEFAULT[index]
        print(REROLLER[x])


def main():
    keyRead()
    print(choose_roller, ROLLER_START, PLUGBOARD)
    ROLLER_START_TEMP = ['','','']
    roller_choose = [0,1,2,3,4]
    for choose_roller_one in roller_choose:#3個轉盤變動且不重複
        choose_roller[0] = choose_roller_one
        for choose_roller_two in roller_choose:
            if choose_roller_two == choose_roller_one:
                continue
            choose_roller[1] = choose_roller_two
            for choose_roller_three in roller_choose:
                if choose_roller_three == choose_roller_one or choose_roller_three == choose_roller_two:
                    continue
                choose_roller[2] = choose_roller_three
                for ROLLER_START_ONE in range (26):#3個轉盤起始位置變動
                    for ROLLER_START_TWO in range (26):
                        for ROLLER_START_THREE in range (26):
                            CIPHERTEXT = ''
                            ROLLER_START[0] = chr(ROLLER_START_ONE+65)
                            ROLLER_START[1] = chr(ROLLER_START_TWO+65)
                            ROLLER_START[2] = chr(ROLLER_START_THREE+65)
                            ROLLER_START_TEMP[0]=ROLLER_START[0]
                            ROLLER_START_TEMP[1]=ROLLER_START[1]
                            ROLLER_START_TEMP[2]=ROLLER_START[2]
                            for i in range (len(PLAINTEXT)):
                                ROLLER_START_TEMP[2] = chr(ord(ROLLER_START_TEMP[2])+1) if(ord(ROLLER_START_TEMP[2])+1<91) else chr(65)#每輸入一個動一格
                                if ord(ROLLER_START_TEMP[1]) == (ord(ROLLER_ARROW[1])-1 or ord(ROLLER_ARROW[1])+25):#如果中間的轉盤起始位置是指針位置前一個，最後一個轉盤跟中間轉盤都會動一格(指針為A,起始位置為Z要另外處理)
                                    ROLLER_START_TEMP[1] = chr(ord(ROLLER_START_TEMP[1])+1) if(ord(ROLLER_START_TEMP[1])+1<91) else chr(65)
                                    ROLLER_START_TEMP[0] = chr(ord(ROLLER_START_TEMP[0])+1) if(ord(ROLLER_START_TEMP[0])+1<91) else chr(65)
                                if ROLLER_START_TEMP[2] == ROLLER_ARROW[2]:#
                                    ROLLER_START_TEMP[1] = chr(ord(ROLLER_START_TEMP[1])+1) if(ord(ROLLER_START_TEMP[1])+1<91) else chr(65)
                                in_put = PLUGBOARD[ord(PLAINTEXT[i])-65]#輸入字母經過接線板後的字母
                                in_one = roller(ROLLER[choose_roller[2]],ord(ROLLER_START_TEMP[2])-65,ord(in_put)-65,1,PLAINTEXT[i])
                                in_two = roller(ROLLER[choose_roller[1]],ord(ROLLER_START_TEMP[1])-65,in_one,1,PLAINTEXT[i])
                                in_three = roller(ROLLER[choose_roller[0]],ord(ROLLER_START_TEMP[0])-65,in_two,1,PLAINTEXT[i])
                                ref = ord(reflector(UKW_B,in_three))-65
                                out_three = roller(ROLLER[choose_roller[0]],ord(ROLLER_START_TEMP[0])-65,ref,2,PLAINTEXT[i])
                                out_two = roller(ROLLER[choose_roller[1]],ord(ROLLER_START_TEMP[1])-65,out_three,2,PLAINTEXT[i])
                                out_one = roller(ROLLER[choose_roller[2]],ord(ROLLER_START_TEMP[2])-65,out_two,2,PLAINTEXT[i])
                                out_put = PLUGBOARD.index(chr(out_one+65))
                                CIPHERTEXT += chr(out_put+65)
                            if CIPHERTEXT.find('CIW')is not -1:#猜測可能有的關鍵字，找到就印出轉盤哪3個、起始位置哪3個、密文
                                print('roller:',choose_roller)
                                print('start:',ROLLER_START)
                                print('result:',CIPHERTEXT)

if __name__ == '__main__':
    main()
