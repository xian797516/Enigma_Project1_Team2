ROLLER_ONE = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
ROLLER_TWO = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']
ROLLER_THEREE = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
ROLLER_FOUR = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
ROLLER_FIVE = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
ROLLER_START = ['H','D','X']#起始位置
ROLLER_ARROW = ['R','F','W']#指針位置
PLUGBOARD = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#接線板
UKW_B = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']#反射器
PLAINTEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"#明文

def reflector(list, n):
    return list[n]

def roller(ROLLER_LIST, start, turn, in_out, input):
    if in_out==1:#in
        index = (start + turn) % 26
        c=ord(ROLLER_LIST[index])-65
        interval=26-(start-c) if(start-c>0) else c-start
        return interval
    elif in_out==2:#out
        index = (start + turn) % 26
        c=ROLLER_LIST.index(chr(index+65))
        interval=26-(start-c) if(start-c>0) else c-start
        return interval
    else:
        return PLAINTEXT[ROLLER_LIST.find(input)]

def main():
    CIPHERTEXT=''
    for i in range (len(PLAINTEXT)):
        ROLLER_START[2]=chr(ord(ROLLER_START[2])+1) if(ord(ROLLER_START[2])+1<91) else chr(65)
        if ord(ROLLER_START[1])==ord(ROLLER_ARROW[1])-1:
            ROLLER_START[1]=chr(ord(ROLLER_START[1])+1)
            ROLLER_START[0]=chr(ord(ROLLER_START[0])+1)
        if ROLLER_START[2]==ROLLER_ARROW[2]:
            ROLLER_START[1]=chr(ord(ROLLER_START[1])+1)
        in_put = PLUGBOARD[ord(PLAINTEXT[i])-65]
        in_one = roller(ROLLER_THEREE,ord(ROLLER_START[2])-65,ord(in_put)-65,1,PLAINTEXT[i])
        in_two = roller(ROLLER_TWO,ord(ROLLER_START[1])-65,in_one,1,PLAINTEXT[i])
        in_three = roller(ROLLER_ONE,ord(ROLLER_START[0])-65,in_two,1,PLAINTEXT[i])
        ref = roller(UKW_B,0,in_three,1,PLAINTEXT[i])
        out_three = roller(ROLLER_ONE,ord(ROLLER_START[0])-65,ref,2,PLAINTEXT[i])
        out_two = roller(ROLLER_TWO,ord(ROLLER_START[1])-65,out_three,2,PLAINTEXT[i])
        out_one = roller(ROLLER_THEREE,ord(ROLLER_START[2])-65,out_two,2,PLAINTEXT[i])
        out_put = roller(PLUGBOARD,0,out_one,2,PLAINTEXT[i])
        CIPHERTEXT+=chr(out_put+65)
    print('result:',CIPHERTEXT)

if __name__ == '__main__':
    main()
