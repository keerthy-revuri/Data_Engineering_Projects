
temp = ' https://az620379.vo.msecnd.net/images/Contract '
final = temp.split('/')
x = final[2].replace('.','_')

for str in final:
    if str == final[2]:
       final[2] = x

output = '/'.join(final)
print(output)
