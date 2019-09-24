import itertools
alist = list(itertools.combinations(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],2))
plugboard_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


for i in range(len(alist)):
    plugboard_list_temp=plugboard_list.copy()
    plugboard_list_temp.pop(plugboard_list_temp.index(alist[i][0]))
    plugboard_list_temp.pop(plugboard_list_temp.index(alist[i][1]))
    plugboard_list_n = plugboard_list.copy()
    plugboard_list_n[ord(alist[i][0])-65],plugboard_list_n[ord(alist[i][1])-65]=plugboard_list_n[ord(alist[i][1])-65],plugboard_list_n[ord(alist[i][0])-65]
    blist = list(itertools.combinations(plugboard_list_temp, 2))
    for j in range(len(blist)):
        plugboard_list_temp2=plugboard_list_temp.copy()
        plugboard_list_temp2.pop(plugboard_list_temp2.index(blist[j][0]))
        plugboard_list_temp2.pop(plugboard_list_temp2.index(blist[j][1]))
        plugboard_list_n1 = plugboard_list_n.copy()
        plugboard_list_n1[ord(blist[j][0]) - 65], plugboard_list_n1[ord(blist[j][1]) - 65] = plugboard_list_n1[ord(blist[j][1]) - 65],plugboard_list_n1[ord(blist[j][0]) - 65]
        if j < 10:
            print(plugboard_list_n1)


