corr_ans=0
wrong_ans=0
q=['1.what is the capital of indian?',
   '2.what is the national animal?']
ans=['delhi','tiger']
for x in range(len(q)):
    print(q[x])
    user_ans=input('enter answer:').lower()
    if user_ans ==ans[x]:
        corr_ans+=1
        print('correct ans')
    else:
        wrong_ans+=1
        print('wrong answer') 
print('percentage',((corr_ans)/(corr_ans+wrong_ans)*100) )            