# %% In process...

converted_list = {2:['a','b','c'], 3:['d','e','f',], 4:['g','h','i'], 5:["j",'k','l'],
                    6:["m",'n','o'], 7:["p",'q','r','s'], 8:['t','u','v'], 9:['w','x','z','y']
                    }
    

digits = '23'
i = 0

lst = []

a = [lst.append(converted_list[int(digits[i])]) for i in range(len(digits))]
print(lst)
for l in range(len(lst)):
    result=converted_list[int(digits[l])]


    for i in range(1,len(result)):
        for j in range(len(lst[i])):
            result[j] += lst[i][j]

    print(result)