import itertools

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
#PLAINTEXT = "IPQHUGCXZM"#"IPQHUGCXZM"#明文
PLAINTEXT = "IPQHUGCXZM"
GUESSTEXT = "HEILHITLER"

A_TO_N = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
N_TO_A = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}

choose_roller = [0,0,0]

#只需改明文跟猜密文中有什麼字串

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

'''def reverseList():
    REROLLER = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]]
    for x in range(5):
        for index, i in enumerate(ROLLER[x]):
            REROLLER[x][DEFAULT.find(i)] = DEFAULT[index]
        print(REROLLER[x])'''

def plugboard_gen(_p_l_t,_list):
    p_l_t=_p_l_t.copy()
    p_l_t.pop(p_l_t.index(_list[0]))
    p_l_t.pop(p_l_t.index(_list[1]))
    for i in range(len(p_l_t)):
        if A_TO_N[_list[0]] > A_TO_N[p_l_t[0]]:
            p_l_t.pop(0)
        else:
            break
    list_n = list(itertools.combinations(p_l_t,2))
    return p_l_t,list_n

def swap(_list,_change):
    p_l_a = _list.copy()
    p_l_a[A_TO_N[_change[0]]], p_l_a[A_TO_N[_change[1]]] = p_l_a[A_TO_N[_change[1]]], p_l_a[A_TO_N[_change[0]]]
    return p_l_a

def check_list(_list,_new):
    for ori in _list:
        c = set(ori) & set(_new)
        if(len(c) > 0):
            return -1
    return 0

def main():
    keyRead()
    fw=open('ans.txt','w')
    #print(choose_roller, ROLLER_START, PLUGBOARD)
    ROLLER_START_TEMP = ['','','']
    roller_choose = [0,1,2,3,4]
    for choose_roller_one in roller_choose[1:2]:#3個轉盤變動且不重複
        choose_roller[0] = choose_roller_one
        for choose_roller_two in roller_choose[0:1]:
            if choose_roller_two == choose_roller_one:
                continue
            choose_roller[1] = choose_roller_two
            for choose_roller_three in roller_choose[3:4]:
                if choose_roller_three == choose_roller_one or choose_roller_three == choose_roller_two:
                    continue
                choose_roller[2] = choose_roller_three
                print('--------',choose_roller)
                for roller_start_one in range (A_TO_N['Z']+1):#3個轉盤起始位置變動
                    for roller_start_two in range (A_TO_N['Z']+1):
                        for roller_start_three in range (A_TO_N['Z']+1):
                            ROLLER_START[0] = N_TO_A[roller_start_one]
                            ROLLER_START[1] = N_TO_A[roller_start_two]
                            ROLLER_START[2] = N_TO_A[roller_start_three]
                            ROLLER_START_TEMP[0]=ROLLER_START[0]
                            ROLLER_START_TEMP[1]=ROLLER_START[1]
                            ROLLER_START_TEMP[2]=ROLLER_START[2]
                            print('------',ROLLER_START)
                            fw.write(str(ROLLER_START))
                            fw.write('\n')
                            letter = ['I']
                            letter.append(PLUGBOARD)
                            for List in itertools.product(*letter):
                                ROLLER_START_TEMP[2] = N_TO_A[A_TO_N[ROLLER_START_TEMP[2]]+1] if(A_TO_N[ROLLER_START_TEMP[2]]+1<26) else N_TO_A[0]#每輸入一個動一格
                                if A_TO_N[ROLLER_START_TEMP[1]] == (A_TO_N[ROLLER_ARROW[1]]-1 or A_TO_N[ROLLER_ARROW[1]]+25):#如果中間的轉盤起始位置是指針位置前一個，最後一個轉盤跟中間轉盤都會動一格(指針為A,起始位置為Z要另外處理)
                                    ROLLER_START_TEMP[1] = N_TO_A[A_TO_N[ROLLER_START_TEMP[1]]+1] if(A_TO_N[ROLLER_START_TEMP[1]]+1<26) else N_TO_A[0]
                                    ROLLER_START_TEMP[0] = N_TO_A[A_TO_N[ROLLER_START_TEMP[0]]+1] if(A_TO_N[ROLLER_START_TEMP[0]]+1<26) else N_TO_A[0]
                                if ROLLER_START_TEMP[2] == ROLLER_ARROW[2]:#
                                   ROLLER_START_TEMP[1] = N_TO_A[A_TO_N[ROLLER_START_TEMP[1]]+1] if(A_TO_N[ROLLER_START_TEMP[1]]+1<26) else N_TO_A[0]
                                in_put = List[1]#輸入字母經過接線板後的字母
                                in_one = roller(ROLLER[choose_roller[2]],A_TO_N[ROLLER_START_TEMP[2]],A_TO_N[in_put],1,PLAINTEXT[0])
                                in_two = roller(ROLLER[choose_roller[1]],A_TO_N[ROLLER_START_TEMP[1]],in_one,1,PLAINTEXT[0])
                                in_three = roller(ROLLER[choose_roller[0]],A_TO_N[ROLLER_START_TEMP[0]],in_two,1,PLAINTEXT[0])
                                ref = A_TO_N[reflector(UKW_B,in_three)]
                                out_three = roller(ROLLER[choose_roller[0]],A_TO_N[ROLLER_START_TEMP[0]],ref,2,PLAINTEXT[0])
                                out_two = roller(ROLLER[choose_roller[1]],A_TO_N[ROLLER_START_TEMP[1]],out_three,2,PLAINTEXT[0])
                                out_one = roller(ROLLER[choose_roller[2]],A_TO_N[ROLLER_START_TEMP[2]],out_two,2,PLAINTEXT[0])                                
                                ans = [N_TO_A[out_one],GUESSTEXT[0]]
                                if 0 == check_list(list(List),ans): #接電板沒重複組合
                                    c = ['','']
                                    c[0] = list(List)#List為輸入的組合
                                    c[1] = ans#ans輸出的組合
                                    fw.write(str(c))
                                    fw.write('\n')
                                #out_put = plugboard_temp.index(N_TO_A[out_one])
                                #print(enum,List)
                                #if out_put is not A_TO_N[GUESSTEXT[0]]:
                                #    break
                                #CIPHERTEXT += N_TO_A[out_put]
                                #if CIPHERTEXT.find(GUESSTEXT)is not -1:#猜測可能有的關鍵字，找到就印出轉盤哪3個、起始位置哪3個、密文
                                #    fw.write('roller:')
                                #    for c_r in range(len(choose_roller)):
                                #        fw.write(str(choose_roller[c_r]))
                                #        fw.write('\n')
                                #        fw.write('start:')
                                #    for R_S in range(len(ROLLER_START)):
                                #        fw.write(ROLLER_START[R_S])
                                #        fw.write('\n')
                                #        fw.write('plugboard:')
                                #    for p_l_a_ in range(len(plugboard_list_ans)):
                                #        fw.write(plugboard_list_ans[p_l_a_])
                                #        fw.write('\n')
                                #        fw.write('result:')
                                #        fw.write(CIPHERTEXT)
                                #        fw.write('\n')
                                #        print('----',plugboard_list_ans)
                                #        print('--',CIPHERTEXT)     
def second():  
    fw = open('ans.txt',r)
    new = open('ans1.txt',w)
    for choose_roller_one in roller_choose[1:2]:#3個轉盤變動且不重複
        choose_roller[0] = choose_roller_one
        for choose_roller_two in roller_choose[0:1]:
            if choose_roller_two == choose_roller_one:
                continue
            choose_roller[1] = choose_roller_two
            for choose_roller_three in roller_choose[3:4]:
                if choose_roller_three == choose_roller_one or choose_roller_three == choose_roller_two:
                    continue
                choose_roller[2] = choose_roller_three
                print('--------',choose_roller)
                
                for roller_start_one in range (A_TO_N['Z']+1):#3個轉盤起始位置變動
                    for roller_start_two in range (A_TO_N['Z']+1):
                        for roller_start_three in range (A_TO_N['Z']+1):
                            ROLLER_START[0] = N_TO_A[roller_start_one]
                            ROLLER_START[1] = N_TO_A[roller_start_two]
                            ROLLER_START[2] = N_TO_A[roller_start_three]
                            ROLLER_START_TEMP[0]=ROLLER_START[0]
                            ROLLER_START_TEMP[1]=ROLLER_START[1]
                            ROLLER_START_TEMP[2]=ROLLER_START[2]
                            print('------',ROLLER_START)
                            fw.write(str(ROLLER_START))
                            fw.write('\n')
                            letter = ['I']
                            letter.append(PLUGBOARD)
                            for enum ,List in itertools.product(*letter):
                                ROLLER_START_TEMP[2] = N_TO_A[A_TO_N[ROLLER_START_TEMP[2]]+1] if(A_TO_N[ROLLER_START_TEMP[2]]+1<26) else N_TO_A[0]#每輸入一個動一格
                                if A_TO_N[ROLLER_START_TEMP[1]] == (A_TO_N[ROLLER_ARROW[1]]-1 or A_TO_N[ROLLER_ARROW[1]]+25):#如果中間的轉盤起始位置是指針位置前一個，最後一個轉盤跟中間轉盤都會動一格(指針為A,起始位置為Z要另外處理)
                                    ROLLER_START_TEMP[1] = N_TO_A[A_TO_N[ROLLER_START_TEMP[1]]+1] if(A_TO_N[ROLLER_START_TEMP[1]]+1<26) else N_TO_A[0]
                                    ROLLER_START_TEMP[0] = N_TO_A[A_TO_N[ROLLER_START_TEMP[0]]+1] if(A_TO_N[ROLLER_START_TEMP[0]]+1<26) else N_TO_A[0]
                                if ROLLER_START_TEMP[2] == ROLLER_ARROW[2]:#
                                   ROLLER_START_TEMP[1] = N_TO_A[A_TO_N[ROLLER_START_TEMP[1]]+1] if(A_TO_N[ROLLER_START_TEMP[1]]+1<26) else N_TO_A[0]
                                in_put = List#輸入字母經過接線板後的字母
                                in_one = roller(ROLLER[choose_roller[2]],A_TO_N[ROLLER_START_TEMP[2]],A_TO_N[in_put],1,PLAINTEXT[0])
                                in_two = roller(ROLLER[choose_roller[1]],A_TO_N[ROLLER_START_TEMP[1]],in_one,1,PLAINTEXT[0])
                                in_three = roller(ROLLER[choose_roller[0]],A_TO_N[ROLLER_START_TEMP[0]],in_two,1,PLAINTEXT[0])
                                ref = A_TO_N[reflector(UKW_B,in_three)]
                                out_three = roller(ROLLER[choose_roller[0]],A_TO_N[ROLLER_START_TEMP[0]],ref,2,PLAINTEXT[0])
                                out_two = roller(ROLLER[choose_roller[1]],A_TO_N[ROLLER_START_TEMP[1]],out_three,2,PLAINTEXT[0])
                                out_one = roller(ROLLER[choose_roller[2]],A_TO_N[ROLLER_START_TEMP[2]],out_two,2,PLAINTEXT[0])
                                ori = [enum,List]
                                ans = [N_TO_A[out_one],GUESSTEXT[0]]
                                c = ['','']
                                c[0] = ori
                                c[1] = ans
                                fw.write(str(c))
                                fw.write('\n')

if __name__ == '__main__':
    main()
    second()
