tiket=[1,2,3,4,5]
print('available tiket',tiket)
user_input=int(input('enter how many tiket buy '))
for x in range(user_input):
    tiket_num=int(input('enter the tiket number'))
    tiket.remove(tiket_num)
print('available tiket',tiket)   