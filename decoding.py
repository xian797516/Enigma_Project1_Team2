import os

ROLLER = [['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'],
        ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'],
        ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'],
        ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'],
        ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']]

CHOOSE_ROLLER = [0, 0, 0]
ROLLER_START = ['A', 'A', 'A']
PLUGBOARD = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#接線板

ROLLER_ARROW = ['R', 'F', 'W', 'K', 'A']#指針位置
UKW_B = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']#反射器

PLAINTEXT = 'ZATVAWORBRQGRJSXZVNORWZBLORMEGRASLQLAFWXZYODVVTDHCIRDMNWOPNIXVKASIIIALOOSZXAMSYCQHYGPRLMSACGAWPCPAVZTMUUZCTJDVBUZAGFWMIVEZGBTLFIQDPPRZHDNKIPQHUGCXZM'
CIPHERTEXT = ''

A_TO_N = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
N_TO_A = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

def reflector(list, n):
    return list[n]

def roller(ROLLER_LIST, start, turn, in_out):
    if in_out == 1:#in
        index = (start + turn) % 26
        c = A_TO_N[ROLLER_LIST[index]]
        interval = 26 - (start - c) if (start - c > 0) else (c - start)
        return interval
    elif in_out == 2:#out
        index = (start + turn) % 26
        c = ROLLER_LIST.index(N_TO_A[index])
        interval = 26 - (start - c) if (start - c > 0) else (c - start)
        return interval

def enigma():
    global CIPHERTEXT
    CIPHERTEXT = ''
    roller0_count, roller1_count, roller2_count = 0, 0, 0
    for i in range (len(PLAINTEXT)):#更新起始位置後開始塞入明文(老師給的密文)
        roller2_count += 1
        ROLLER_START_TEMP = [N_TO_A[(A_TO_N[ROLLER_START[0]] + roller0_count) % 26], N_TO_A[(A_TO_N[ROLLER_START[1]] + roller1_count) % 26], N_TO_A[(A_TO_N[ROLLER_START[2]] + roller2_count) % 26]]
        if A_TO_N[ROLLER_START_TEMP[1]] == (A_TO_N[ROLLER_ARROW[CHOOSE_ROLLER[1]]] - 1 or A_TO_N[ROLLER_ARROW[CHOOSE_ROLLER[1]]] + 25):
            roller0_count += 1
            roller1_count += 1
            ROLLER_START_TEMP[0], ROLLER_START_TEMP[1] = N_TO_A[(A_TO_N[ROLLER_START[0]] + roller0_count) % 26], N_TO_A[(A_TO_N[ROLLER_START[1]] + roller1_count) % 26]
        if ROLLER_START_TEMP[2] == ROLLER_ARROW[CHOOSE_ROLLER[2]]:
            roller1_count += 1
            ROLLER_START_TEMP[1] = N_TO_A[(A_TO_N[ROLLER_START[1]] + roller1_count) % 26]
        in_put = PLUGBOARD[A_TO_N[PLAINTEXT[i]]]
        in_one = roller(ROLLER[CHOOSE_ROLLER[2]], A_TO_N[ROLLER_START_TEMP[2]], A_TO_N[in_put], 1)
        in_two = roller(ROLLER[CHOOSE_ROLLER[1]], A_TO_N[ROLLER_START_TEMP[1]], in_one, 1)
        in_three = roller(ROLLER[CHOOSE_ROLLER[0]], A_TO_N[ROLLER_START_TEMP[0]], in_two, 1)
        ref = A_TO_N[reflector(UKW_B, in_three)]
        out_three = roller(ROLLER[CHOOSE_ROLLER[0]], A_TO_N[ROLLER_START_TEMP[0]], ref, 2)
        out_two = roller(ROLLER[CHOOSE_ROLLER[1]], A_TO_N[ROLLER_START_TEMP[1]], out_three, 2)
        out_one = roller(ROLLER[CHOOSE_ROLLER[2]], A_TO_N[ROLLER_START_TEMP[2]], out_two, 2)
        out_put = PLUGBOARD.index(N_TO_A[out_one])
        print(PLAINTEXT[i], in_put, N_TO_A[in_one], N_TO_A[in_two], N_TO_A[in_three], N_TO_A[ref], N_TO_A[out_three], N_TO_A[out_two], N_TO_A[out_one], N_TO_A[out_put], PLUGBOARD, roller0_count, roller1_count, roller2_count)
        CIPHERTEXT += N_TO_A[out_put]#最後會是148字加密後的值

def main():
    folderpath = '/Project2-1_Enigma_machine'
    try:
      os.makedirs(folderpath)
    except FileExistsError:
      print("資料夾已存在。")
    fr = open(folderpath + '/整理.txt', 'r')
    fw = open(folderpath + '/可能.txt', 'w')
    line = fr.readline()
    count = 0
    global CHOOSE_ROLLER, ROLLER_START, PLUGBOARD
    while line:
        CHOOSE_ROLLER = [int(line[0]), int(line[1]), int(line[2])]#依照main.py輸出的txt中取出CHOOSE_ROLLER, ROLLER_START_GUESS, PLUGBOARD, 記住此時的起始位置是輸入138字之後的起始位置
        ROLLER_START_GUESS = [line[6], line[7], line[8]]
        for i in range (26):
            PLUGBOARD[i] = line[14 + (5 * i)]
        shit = 0
        for i in range (26):#確定PLUGBOARD有A-Z
            if N_TO_A[i] not in PLUGBOARD:
                shit = 1
        if shit == 1:
            print('shit', CHOOSE_ROLLER, ROLLER_START_GUESS, PLUGBOARD)
        else:#找138字之前的起始位置, 其實可以寫逆推比較好, 不用一個一個試
            findit = 0
            ROLLER_START = ['','','']
            for ROLLER_START_ONE in range (26):
                for ROLLER_START_TWO in range (26):
                    for ROLLER_START_THREE in range (26):
                        roller0_count, roller1_count, roller2_count = 0, 0, 0
                        for i in range (138):#推138字
                            roller2_count += 1
                            ROLLER_START = [N_TO_A[(ROLLER_START_ONE + roller0_count) % 26], N_TO_A[(ROLLER_START_TWO + roller1_count) % 26], N_TO_A[(ROLLER_START_THREE + roller2_count) % 26]]
                            if A_TO_N[ROLLER_START[1]] == (A_TO_N[ROLLER_ARROW[CHOOSE_ROLLER[1]]] - 1 or A_TO_N[ROLLER_ARROW[CHOOSE_ROLLER[1]]] + 25):
                                roller0_count += 1
                                roller1_count += 1
                                ROLLER_START[0], ROLLER_START[1] = N_TO_A[(ROLLER_START_ONE + roller0_count) % 26], N_TO_A[(ROLLER_START_TWO + roller1_count) % 26]
                            if ROLLER_START[2] == ROLLER_ARROW[CHOOSE_ROLLER[2]]:#
                                roller1_count += 1
                                ROLLER_START[1] = N_TO_A[(ROLLER_START_TWO + roller1_count) % 26]
                        if ROLLER_START == ROLLER_START_GUESS:#找到就把起始位置改掉給等等的enigma用
                            ROLLER_START = [N_TO_A[ROLLER_START_ONE], N_TO_A[ROLLER_START_TWO], N_TO_A[ROLLER_START_THREE]]
                            findit = 1
                            break
                    if findit == 1:
                        break
                if findit == 1:
                    break

            enigma()#回傳148字加密後的值

            if ROLLER_START == ['', '', '']:
                print('also shit', CHOOSE_ROLLER, ROLLER_START_GUESS, PLUGBOARD)
            else:
                count += 1
                print(count,ROLLER_START)
                print(CIPHERTEXT)
                fw.write(str(count))
                fw.write('\n')
                fw.write('CHOOSE_ROLLER = ')
                fw.write(str(CHOOSE_ROLLER))
                fw.write('\n')
                fw.write('ROLLER_START = ')
                fw.write(str(ROLLER_START))
                fw.write('\n')
                fw.write('PLUGBOARD = ')
                fw.write(str(PLUGBOARD))
                fw.write('\n')
                fw.write(CIPHERTEXT)
                fw.write('\n')
                fw.write('\n')

        line = fr.readline()
    fr.close()
    fw.close()

if __name__ == '__main__':
    main()
