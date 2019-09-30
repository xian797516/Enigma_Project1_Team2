import os

ROLLER = [['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J'],
        ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E'],
        ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O'],
        ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B'],
        ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']]

CHOOSE_ROLLER = [0, 1, 2]#轉盤選擇
ROLLER_START = ['H', 'D', 'X']#起始位置
PLUGBOARD = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#接線板

ROLLER_ARROW = ['R', 'F', 'W', 'K', 'A']#指針位置
UKW_B = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']#反射器

PLAINTEXT = 'IPQHUGCXZM'
GUESSTEXT = 'HEILHITLER'

A_TO_N = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
N_TO_A = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

def reflector(list, n):
    return list[n]

def roller(ROLLER_LIST, start, turn, in_out):
    if in_out == 1:#in
        index = (start + turn) % 26#位移後的字母的值
        c = A_TO_N[ROLLER_LIST[index]]#
        interval = 26 - (start - c) if (start - c > 0) else (c - start)#從起始位置到目標位置的位移量
        return interval
    elif in_out == 2:#out
        index = (start + turn) % 26#位移後的字母的值
        c = ROLLER_LIST.index(N_TO_A[index])#找轉盤的第幾個位置是起始位置位移後的字母
        interval = 26 - (start - c) if (start - c > 0) else (c - start)#從起始位置到目標位置的位移量
        return interval

def enigma(_P, _r_c_0, _r_c_1, _r_c_2, _P_index):
    _P_T = _P.copy()
    roller0_count, roller1_count, roller2_count = _r_c_0, _r_c_1, _r_c_2
    roller2_count += 1
    ROLLER_START_TEMP = [N_TO_A[(A_TO_N[ROLLER_START[0]] + roller0_count) % 26], N_TO_A[(A_TO_N[ROLLER_START[1]] + roller1_count) % 26], N_TO_A[(A_TO_N[ROLLER_START[2]] + roller2_count) % 26]]
    if A_TO_N[ROLLER_START_TEMP[1]] == (A_TO_N[ROLLER_ARROW[CHOOSE_ROLLER[1]]] - 1 or A_TO_N[ROLLER_ARROW[CHOOSE_ROLLER[1]]] + 25):
        roller0_count += 1
        roller1_count += 1
        ROLLER_START_TEMP[0], ROLLER_START_TEMP[1] = N_TO_A[(A_TO_N[ROLLER_START[0]] + roller0_count) % 26], N_TO_A[(A_TO_N[ROLLER_START[1]] + roller1_count) % 26]
    if ROLLER_START_TEMP[2] == ROLLER_ARROW[CHOOSE_ROLLER[2]]:
        roller1_count += 1
        ROLLER_START_TEMP[1] = N_TO_A[(A_TO_N[ROLLER_START[1]] + roller1_count) % 26]
    if _P_T.__contains__(PLAINTEXT[_P_index]):#如果明文有在接線板交換名單內, in_put等於明文經過接線板交換名單後的字母
        in_put = _P_T[PLAINTEXT[_P_index]]
    else:#不然就不變
        in_put = PLAINTEXT[_P_index]
    in_one = roller(ROLLER[CHOOSE_ROLLER[2]], A_TO_N[ROLLER_START_TEMP[2]], A_TO_N[in_put], 1)
    in_two = roller(ROLLER[CHOOSE_ROLLER[1]], A_TO_N[ROLLER_START_TEMP[1]], in_one, 1)
    in_three = roller(ROLLER[CHOOSE_ROLLER[0]], A_TO_N[ROLLER_START_TEMP[0]], in_two, 1)
    ref = A_TO_N[reflector(UKW_B, in_three)]
    out_three = roller(ROLLER[CHOOSE_ROLLER[0]], A_TO_N[ROLLER_START_TEMP[0]], ref, 2)
    out_two = roller(ROLLER[CHOOSE_ROLLER[1]], A_TO_N[ROLLER_START_TEMP[1]], out_three, 2)
    out_one = roller(ROLLER[CHOOSE_ROLLER[2]], A_TO_N[ROLLER_START_TEMP[2]], out_two, 2)
    if _P_T.__contains__(N_TO_A[out_one]):#如果出轉盤後的字母有在接線板交換名單內, out_put等於出轉盤後的字母經過接線板交換名單後的字母
        out_put = _P_T[N_TO_A[out_one]]
    else:#不然就不變
        out_put = N_TO_A[out_one]
    if out_put is GUESSTEXT[_P_index]:#如果確定跟我要猜的字母一樣, 就回傳各轉盤轉了多少格
        return [roller0_count, roller1_count, roller2_count]
    return [0, 0, 0]#不一樣就回傳[0, 0, 0]

def plugboard_change(_P, _i_1, _i_2, _P_index):#判斷狀況並交換
    _P_T = _P.copy()
    if PLAINTEXT[_P_index] == N_TO_A[_i_1] and N_TO_A[_i_2] == GUESSTEXT[_P_index]:#AACC
        _P_T[PLAINTEXT[_P_index]], _P_T[N_TO_A[_i_1]] = N_TO_A[_i_1], PLAINTEXT[_P_index]
        _P_T[N_TO_A[_i_2]], _P_T[GUESSTEXT[_P_index]] = GUESSTEXT[_P_index], N_TO_A[_i_2]
    elif PLAINTEXT[_P_index] == N_TO_A[_i_2] and N_TO_A[_i_1] == GUESSTEXT[_P_index]:#ACAC
        _P_T[PLAINTEXT[_P_index]], _P_T[N_TO_A[_i_1]] = N_TO_A[_i_1], PLAINTEXT[_P_index]
    elif PLAINTEXT[_P_index] == N_TO_A[_i_1] and N_TO_A[_i_2] != GUESSTEXT[_P_index]:#AACD
        _P_T[PLAINTEXT[_P_index]], _P_T[N_TO_A[_i_1]] = N_TO_A[_i_1], PLAINTEXT[_P_index]
        _P_T[N_TO_A[_i_2]], _P_T[GUESSTEXT[_P_index]] = GUESSTEXT[_P_index], N_TO_A[_i_2]
    elif PLAINTEXT[_P_index] != N_TO_A[_i_1] and N_TO_A[_i_2] == GUESSTEXT[_P_index]:#ABCC
        _P_T[PLAINTEXT[_P_index]], _P_T[N_TO_A[_i_1]] = N_TO_A[_i_1], PLAINTEXT[_P_index]
        _P_T[N_TO_A[_i_2]], _P_T[GUESSTEXT[_P_index]] = GUESSTEXT[_P_index], N_TO_A[_i_2]
    elif PLAINTEXT[_P_index] != N_TO_A[_i_1] and N_TO_A[_i_2] != GUESSTEXT[_P_index]:#ABCD
        _P_T[PLAINTEXT[_P_index]], _P_T[N_TO_A[_i_1]] = N_TO_A[_i_1], PLAINTEXT[_P_index]
        _P_T[N_TO_A[_i_2]], _P_T[GUESSTEXT[_P_index]] = GUESSTEXT[_P_index], N_TO_A[_i_2]
    else:
        return {0: 0}
    return _P_T

def dict_check(_dict, _i_1, _i_2, _P_index):#_i_1不能等於_i_2, 因為經過enigma後絕對不會是自己. 確認是否已經被換過, 且經過接線板後的字母跟換過的字母一樣
    if _i_1 == _i_2 or (_i_1 == A_TO_N[GUESSTEXT[_P_index]] and _i_2 != A_TO_N[PLAINTEXT[_P_index]]) or (_i_1 != A_TO_N[GUESSTEXT[_P_index]] and _i_2 == A_TO_N[PLAINTEXT[_P_index]]):
        return 0
    if _dict.__contains__(PLAINTEXT[_P_index]) and (_dict[PLAINTEXT[_P_index]] != N_TO_A[_i_1]):
        return 0
    if _dict.__contains__(N_TO_A[_i_1]) and (_dict[N_TO_A[_i_1]] != PLAINTEXT[_P_index]):
        return 0
    if _dict.__contains__(N_TO_A[_i_2]) and (_dict[N_TO_A[_i_2]] != GUESSTEXT[_P_index]):
        return 0
    if _dict.__contains__(GUESSTEXT[_P_index]) and (_dict[GUESSTEXT[_P_index]] != N_TO_A[_i_2]):
        return 0
    return 1

def findpair(_r_c_list, _pairs_dict_list, _P_index):
    pairs = 6#固定只有6組字母交換
    _return_r_c, _return_p_d = [], []
    if _P_index == 0:
        for m in range(26):#明文經過接線板後的字母
            for n in range(26):#密文經過接線板後的字母
                r_c_t = [0, 0, 0]
                p_d_t = {}
                if dict_check(p_d_t, m, n, _P_index) == 0:
                    continue
                p_d_t = plugboard_change({}, m, n, _P_index)
                r_c_t = enigma(p_d_t, r_c_t[0], r_c_t[1], _P_index, _P_index)
                if r_c_t[2] == 0:#如果enigma收到[0, 0, 0]表示此組合不是我們要找的, 就會跳過
                    continue
                _return_r_c = r_c_t
                _return_p_d.append(p_d_t)#是我們要找的話的話就會丟到要回傳的list裡面
    else:
        for i in range(len(_pairs_dict_list)):#同上，只是多了接線板的組合要做測試
            for m in range(26):
                for n in range(26):
                    p_d_pairs = 0
                    r_c_t = _r_c_list.copy()
                    p_d_t = _pairs_dict_list[i].copy()
                    if dict_check(p_d_t, m, n, _P_index) == 0:
                        continue
                    p_d_t = plugboard_change(_pairs_dict_list[i], m, n, _P_index)
                    for p_d_t_key in p_d_t:
                        for p_d_t_value in p_d_t[p_d_t_key]:
                            if p_d_t_key != p_d_t_value:
                                p_d_pairs += 1
                    if (p_d_pairs / 2) > pairs:
                        continue
                    r_c_t = enigma(p_d_t, r_c_t[0], r_c_t[1], _P_index, _P_index)
                    if r_c_t[2] == 0:
                        continue
                    _return_r_c = r_c_t
                    _return_p_d.append(p_d_t)
    return _return_r_c,_return_p_d#回傳各轉盤要轉幾格, 經過確認後的各種接線板組合

def main():
    global ROLLER_START
    r_c_one_start, r_c_two_start, r_c_three_start = 0, 0, 0#設定轉盤
    r_s_one_start, r_s_two_start, r_s_three_start = A_TO_N['A'], A_TO_N['A'], A_TO_N['A']#設定轉盤起始位置
    for ROLLER_CHOOSE_ONE in range(r_c_one_start, 5):
        for ROLLER_CHOOSE_TWO in range(r_c_two_start, 5):
            if ROLLER_CHOOSE_ONE == ROLLER_CHOOSE_TWO:#轉盤不能重複
                continue
            for ROLLER_CHOOSE_THREE in range(r_c_three_start, 5):
                if ROLLER_CHOOSE_ONE == ROLLER_CHOOSE_THREE or ROLLER_CHOOSE_TWO == ROLLER_CHOOSE_THREE:#轉盤不能重複
                    continue
                global CHOOSE_ROLLER
                CHOOSE_ROLLER = [ROLLER_CHOOSE_ONE, ROLLER_CHOOSE_TWO, ROLLER_CHOOSE_THREE]
                txtroller = ''.join(str(i) for i in CHOOSE_ROLLER)
                folderpath = '/Project2-1_Enigma_machine/' + txtroller
                try:
                  os.makedirs(folderpath)
                except FileExistsError:
                  print('資料夾已存在。')
                for ROLLER_START_ONE in range (r_s_one_start, 26):
                    txtpath = folderpath + '/' + txtroller + '_' + N_TO_A[ROLLER_START_ONE] + '.txt'
                    fw = open(txtpath, 'w')
                    for ROLLER_START_TWO in range (r_s_two_start, 26):
                        for ROLLER_START_THREE in range (r_s_three_start, 26):
                            ROLLER_START = [N_TO_A[ROLLER_START_ONE], N_TO_A[ROLLER_START_TWO], N_TO_A[ROLLER_START_THREE]]
                            if ROLLER_START_TWO == A_TO_N[ROLLER_ARROW[ROLLER_CHOOSE_TWO]] - 1 and ROLLER_START_THREE != A_TO_N[ROLLER_ARROW[ROLLER_CHOOSE_THREE]]:
								#當中間轉盤的起始位置是中間轉盤的指針位置的前一個, 第一個轉盤的起始位置必須是第一個轉盤的指針位置
                                continue
                            if ROLLER_START_TWO == A_TO_N[ROLLER_ARROW[ROLLER_CHOOSE_TWO]] and ROLLER_START_THREE == A_TO_N[ROLLER_ARROW[ROLLER_CHOOSE_THREE]]:
								#當中間轉盤的起始位置是中間轉盤的指針位置, 第一個轉盤的起始位置不能是第一個轉盤的指針位置
                                continue
                            r_c_list, pairs_dict_list, pairs_list = [], [], []
                            for PLAINTEXT_INDEX in range (len(PLAINTEXT)):#IPQHUGCXZM進去開始猜, 會把前一次回傳各轉盤轉多少格以及確定後的交換名單在丟進去跑
                                r_c_list, pairs_dict_list = findpair(r_c_list, pairs_dict_list, PLAINTEXT_INDEX)
                            print(CHOOSE_ROLLER, ROLLER_START)
                            if len(pairs_dict_list) != 0:#空的就表示這個轉盤組合, 起始位置, 沒有可能的交換名單
                                print(CHOOSE_ROLLER, ROLLER_START, pairs_dict_list)
                                for pairs_count in range (len(pairs_dict_list)):
                                    PLUGBOARD_TEMP = PLUGBOARD.copy()
                                    pairs_f_count = 0
                                    fw.write(''.join(str(e) for e in CHOOSE_ROLLER))
                                    fw.write('   ')
                                    fw.write(''.join(str(e) for e in ROLLER_START))
                                    fw.write('   ')
                                    for p_d_l_key in pairs_dict_list[pairs_count]:
                                        PLUGBOARD_TEMP[A_TO_N[p_d_l_key]] = pairs_dict_list[pairs_count][p_d_l_key]#接線板經過交換後輸出
                                        for p_d_l_value in pairs_dict_list[pairs_count][p_d_l_key]:
                                            if p_d_l_key != p_d_l_value:
                                                pairs_f_count += 1
                                    fw.write(str(PLUGBOARD_TEMP))
                                    fw.write('   ')
                                    fw.write(str(pairs_f_count // 2))
                                    fw.write('\n')
                    fw.close()

if __name__ == '__main__':
    main()
