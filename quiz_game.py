Ask=input('Are You Ready Play Quiz? ')

if Ask.lower()!='yes':
    quit()

print('Welcome To The Quiz Game :)')

Name=input("Enter Your Name : ")

score=0

q=input('what is full form of URl?  ')

if q.lower()=='uniform resource locating':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!! :- Correct  answer is "Uniform Resource Locating"')


q=input('what is full form of HTTP?  ')
if q.lower()=='hyper text transfer protocal':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!! :- Correct answer is "Hyper Text Transfer Protocal"')    

q=input('what is full form of HTTPS?  ')
if q.lower()=='hyper text transfer protocal security':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!! :- Correct answer is  "Hyper Text Transfer Protocol Security".') 

q=input('what is full form of ASGI?  ')
if q.lower()=='asynchronous server gateway interface':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!! :-  Correct Answer is "Asynchronous Server Gateway Interface"')  

q=input('what is full form of WSGI?  ')
if q.lower()=='web server gateway interface':
    print('Correct!!')
    score+=1
else:
    print('Incorrect!!! :-  Correct Answer is "Web Server Gateway Interface"')          

print(f'\n\nYour Score Is {score}/5.')
if score<3:
    print(f'{Name} Better Luck Next Time!!!!!')
elif score ==3:
    print(f'{Name} You are Average Performer, Keep it Up!!')
elif  score>3:
    print(f'{Name} You Excellent. \nYou Won The Quiz!!!!!')