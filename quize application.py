corr_ans=0
wrong_ans=0
print('1.what is the capital of india?')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='delhi':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')    
print('1.what is the nationnal animal?')
user_ans=input('enter ans:').upper()
print(user_ans)
if user_ans=='TIGER':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')  
print('1.what is the national bird?')
user_ans=input('enter ans:').lower()
print(user_ans)
if user_ans=='peacock':
    corr_ans+=1
    print('correct ans')
else:
    wrong_ans+=1
    print('wrong ans')      
print('percentage',((corr_ans)/(corr_ans+wrong_ans)*100) )   