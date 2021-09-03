#import re
# i=input('enter string')
# x='[\D]{8,15}'
# match=re.fullmatch(x,i)
# if match is not None:
#     print('valid')
# else:
#     print('invalid');
# import re
# i=input('enter string')
# x='(^[A-Z][A-Za-z\d\W]*)'
# match=re.fullmatch(x,i)
# if match is not None:
#     print('valid')
# else:
#     print('invalid');
# import re
# f1=open('phone','r')
# x = '[+][9][1]\d{10}$'
# for i in f1:
#    n1=i.rstrip('\n')
#    # print(i,end=' ')
#    match=re.fullmatch(x,n1)
#    if match != None:
#         print(i)
import re
f1=open('stdsort','r')
f2=open('stdsort1','w')
rl='([l][u][m]\d{2}[p][y]\d{3})'
for i in f1:
  #print(i)
  l = i.rstrip('\n')
  match = re.fullmatch(rl,l)
  #print(l)
   # print(i,end=' ')

  if match != None:
     f2.write (l)
     f2.write('\n ')
   #      print(i)



