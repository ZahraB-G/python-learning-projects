# Check whether two strings are isomorphic or not.
first_str,second_str  = 'paper', 'title'
flag = True
if len(first_str) != len(second_str):
    flag=False
else:
    map1,map2 = {},{}
    for i,j in zip(first_str,second_str):
        if i in map1:
            if map1[i] != j:
                flag = False
        else:
            map1[i] = j

        if j in map2:
            if map2[j] != j:
                flag = False
        else:
            map2[j] = i

if flag:
    print('It is Isomrphic.')
else:
    print('It is NOT Isomrphic!')