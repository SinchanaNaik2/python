name=input('enter the name:')
exp=int(input(f'enter {name} experince'))
if exp>=1:
    if exp>=1 and exp<=5:
       print('25k')
    elif exp>=6 and exp<=10:
         print('50k') 
    else:
        print('75k')
else:
    print('not aloowed')            