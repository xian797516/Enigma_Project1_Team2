ROLLER = [['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J'],
            ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E'],
            ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O'],
            ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B'],
            ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']]

ROLLER_START = ['A','A','A']#起始位置
ROLLER_ARROW = ['R','F','W','K','A']#指針位置
PLUGBOARD = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
UKW_B = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']#反射器

PLAINTEXT = 'HEILHITLER'
CIPHERTEXT = ''

A_TO_N = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
N_TO_A = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

def reflector(list, n):
    return list[n]

def roller(ROLLER_LIST, start, turn, in_out, input):
    if in_out == 1:#in
        index = (start + turn) % 26
        c = A_TO_N[ROLLER_LIST[index]]
        interval = 26-(start-c) if (start-c>0) else (c-start)#從起始位置到目標位置的位移量
        return interval
    elif in_out == 2:#out
        index = (start + turn) % 26
        c = ROLLER_LIST.index(N_TO_A[index])#找轉盤的第幾個位置是起始位置位移後的字母
        interval = 26-(start-c) if (start-c>0) else (c-start)#從起始位置到目標位置的位移量
        return interval
    else:
        return PLAINTEXT[ROLLER_LIST.find(input)]

def main():
    CIPHERTEXT = ''
    roller0_count = 0
    roller1_count = 0
    roller2_count = 0
    ROLLER_START_TEMP = ['','','']
    ROLLER_START_TEMP[0] = ROLLER_START[0]
    ROLLER_START_TEMP[1] = ROLLER_START[1]
    ROLLER_START_TEMP[2] = ROLLER_START[2]
    choose_roller = [1,0,2]
    for i in range (len(PLAINTEXT)):
        roller0_count += 1
        ROLLER_START_TEMP[2] = N_TO_A[A_TO_N[ROLLER_START[2]]+roller0_count] if(A_TO_N[ROLLER_START[2]]+roller0_count<26) else N_TO_A[(A_TO_N[ROLLER_START[2]]+roller0_count)%26]#每輸入一個動一格
        ROLLER_START_TEMP[1] = N_TO_A[A_TO_N[ROLLER_START[1]]+roller1_count] if(A_TO_N[ROLLER_START[1]]+roller1_count<26) else N_TO_A[(A_TO_N[ROLLER_START[1]]+roller1_count)%26]
        ROLLER_START_TEMP[0] = N_TO_A[A_TO_N[ROLLER_START[0]]+roller2_count] if(A_TO_N[ROLLER_START[0]]+roller2_count<26) else N_TO_A[(A_TO_N[ROLLER_START[0]]+roller2_count)%26]
        if A_TO_N[ROLLER_START_TEMP[1]] == (A_TO_N[ROLLER_ARROW[choose_roller[1]]]-1 or A_TO_N[ROLLER_ARROW[choose_roller[1]]]+25):#如果中間的轉盤起始位置是指針位置前一個，最後一個轉盤跟中間轉盤都會動一格(指針為A,起始位置為Z要另外處理)
            roller1_count += 1
            roller2_count += 1
            ROLLER_START_TEMP[1] = N_TO_A[A_TO_N[ROLLER_START[1]]+roller1_count] if(A_TO_N[ROLLER_START[1]]+roller1_count<26) else N_TO_A[(A_TO_N[ROLLER_START[1]]+roller1_count)%26]
            ROLLER_START_TEMP[0] = N_TO_A[A_TO_N[ROLLER_START[0]]+roller2_count] if(A_TO_N[ROLLER_START[0]]+roller2_count<26) else N_TO_A[(A_TO_N[ROLLER_START[0]]+roller2_count)%26]
        if ROLLER_START_TEMP[2] == ROLLER_ARROW[choose_roller[2]]:#
            roller1_count += 1
            ROLLER_START_TEMP[1] = N_TO_A[A_TO_N[ROLLER_START[1]]+roller1_count] if(A_TO_N[ROLLER_START[1]]+roller1_count<26) else N_TO_A[(A_TO_N[ROLLER_START[1]]+roller1_count)%26]
        #print(ROLLER_START_TEMP)
        in_put = PLUGBOARD[A_TO_N[PLAINTEXT[i]]]#輸入字母經過接線板後的字母
        in_one = roller(ROLLER[choose_roller[2]],A_TO_N[ROLLER_START_TEMP[2]],A_TO_N[in_put],1,PLAINTEXT[i])
        in_two = roller(ROLLER[choose_roller[1]],A_TO_N[ROLLER_START_TEMP[1]],in_one,1,PLAINTEXT[i])
        in_three = roller(ROLLER[choose_roller[0]],A_TO_N[ROLLER_START_TEMP[0]],in_two,1,PLAINTEXT[i])
        ref = A_TO_N[reflector(UKW_B,in_three)]
        out_three = roller(ROLLER[choose_roller[0]],A_TO_N[ROLLER_START_TEMP[0]],ref,2,PLAINTEXT[i])
        out_two = roller(ROLLER[choose_roller[1]],A_TO_N[ROLLER_START_TEMP[1]],out_three,2,PLAINTEXT[i])
        out_one = roller(ROLLER[choose_roller[2]],A_TO_N[ROLLER_START_TEMP[2]],out_two,2,PLAINTEXT[i])
        out_put = PLUGBOARD.index(N_TO_A[out_one])
        print(PLAINTEXT[i],in_put,N_TO_A[in_one],N_TO_A[in_two],N_TO_A[in_three],N_TO_A[ref],N_TO_A[out_three],N_TO_A[out_two],N_TO_A[out_one],N_TO_A[out_put],PLUGBOARD,roller0_count,roller1_count,roller2_count)
        CIPHERTEXT += N_TO_A[out_put]
    print(CIPHERTEXT)

if __name__ == '__main__':
    main()
