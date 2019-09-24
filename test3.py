import itertools
alist = list(itertools.combinations(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],2))
plugboard_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count = 0

def combo( p_l_t ,p_l , a_l ,count):
    c = 0
    for i in range(len(a_l)):
        plugboard_list_temp=p_l.copy()
        plugboard_list_temp.pop(plugboard_list_temp.index(a_l[i][0]))
        plugboard_list_temp.pop(plugboard_list_temp.index(a_l[i][1]))
        plugboard_list_n = p_l_t.copy()
        plugboard_list_n[ord(a_l[i][0])-65],plugboard_list_n[ord(a_l[i][1])-65]=plugboard_list_n[ord(a_l[i][1])-65],plugboard_list_n[ord(a_l[i][0])-65]
        blist = list(itertools.combinations(plugboard_list_temp, 2))
        # if count == 5:
        #     c += 1
        if count == 5:
            print(plugboard_list_n)

        if count < 6:
            combo(plugboard_list_n,plugboard_list_temp,blist,count)
            count+=1
if __name__ == '__main__':
    combo(plugboard_list,plugboard_list,alist,count)
