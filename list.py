q=['1.what is the capital of indian?',
   '2.what is the national animal?']
ans=['delhi','tiger']
for x in q:
    print(x)
    user_ans=input('enter answer:').lower()
    if user_ans in ans:
        print('correct ans')
    else:
        print('wrong answer')    