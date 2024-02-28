#WAP TO PRINT HOW MANY ELEMENTS ARE PRESENT IN THE GIVEN STRING WITHOUT USING FUNCTION
'''
s=input('enter the string:')#1st take input as a string from user then store in s variable
count=0#assumed no element present so created count and assigned with 0

#my input string is 'kiran1234'

for i in s:#iteration through my string,we take i variable for take from 1st one by one

#then i check and took 1 after another and execute for block
#how many time i checks in side s string and sucessfully controler comes to for block that times increase count values add 1    

    count+=1
print (count)#when iteration or i check there is no element then
            # comes to outer print statement what amount is sore in count variable that amount display'''    
    
# given string how many digits are present
'''s=input()
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)      

1-first i am taking string as input from user
2-assumed no elements.so created c and assigned with 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking condition
        if condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking condition
        if condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking condition
        if condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking condition
        if condition is true,so count(c) 1 and go to next iteration  
    iteration-5
        i='2',now checking condition
        if condition is true,so count(c) value is 1 then add 1 and go to next iteration
    iteration-6
        i='3',now checking condition
        if condition is true,so count(c) value is 2 then add 1  and go to next iteration  
    There is no more iteration i take empty string then if condition check if condition is false then come out from iteration.
so we want to print count(c) value  and get output as 3'''


#given string how many even digits are present
'''s=input()
c=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            c+=1
print(c)  '''

'''1-first i am taking string as input from user
2-assumed no elements.so createdc and assigned with 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition, condition is true then string'1' convert into integer 1 and check if even condition,
        condition is false,so skip and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition, condition is true then '2' convert into integer 2 and check if even condition,
        condition is true,so count 1 and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert into integer 3 and check if even condition,
        condition is false,so skip and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output     '''


#given string how many odd digits are present
'''s=input()
c=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==1:
            c+=1
print(c)  '''

'''1-first i am taking string as input from user
2-assumed no elements.so created c and assigned with 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition,condition is true then '1' convert integer and check if condition,
        condition is true,so count 1 and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition,condition is true then '2' convert integer and check if condition,
        condition is false,so skip and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert integer and check if condition,
        condition is true,so count 2 and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output     '''


#given string how many even  and odd digits are present
'''s=input()
even=0
odd=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            even+=1
        else:
            odd+=1    
print(even)
print(odd)  '''

'''1-first i am taking string as input from user
2-assumed no elements.so created even & odd and assigned with 0 & 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition, condition is true then '1' convert integer.
        first check if condition is false so go to else part and condition is true
        so count 1 and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition, condition is true then '2' convert integer.
        first check if condition is true,so count 1 and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert integer.
        first check if condition is false so go to else part and condition is true
        so count 2 and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output     '''
#wap to find out sum of even no from given sring
'''
s=input()
evensum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            evensum=evensum+k
print(evensum) '''       
        
'''1-first i am taking string as input from user        
   2-assumed no elements.so created evensum & assigned 0
   3-my string is 'hai1234'
   4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition, condition is true then '1' convert integer.
        then check if  even condition part and condition is false 
        so skip and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition, condition is true then '2' convert integer 2.
        first check if even condition is true,so evensum is 0 added  2 and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert integer.
        first check if even condition is false 
        so go to next iteration
    iteration-7
        i='4',now checking isdigit() condition, condition is true then '4' convert integer 4 .
        first check if even condition is true,so evensum is 2 added 4 and go to next iteration
    There is no more iteration.
so iteration 7 goes to print and get output '''
#how many elements present in given string without using length function
'''a=input('enter a string:')
c=0
for i in a:
    c+=1
print(c)'''    

'''1-first i am taking string as input from user
2-assumed no elements.so created c and assigned with 0
4-my string is 'hai123'
5-iterating through my string
    iteration-1
        i='h',
        count 1 and go to next iteration
    iteration-2
        i='a',
        count 2 and go to next iteration
    iteration-3
        i='i',
        count 3 and go to next iteration
    iteration-4
        i='1',
        count 4 and go to next iteration 
    iteration-5
        i='2',
        count 5 and go to next iteration
    iteration-6
        i='3',
        count 6 and go to next iteration 
    There is no more iteration.
6-Go to print function  and get output'''


#how many time a given substring is present in a specified string
'''a=input('enter a string:')
b=input('enter a sub-string:')
c=0
for i in a:
    if i==b:
        c+=1
print(c)  '''      

'''1-first i am taking string as input from user
2-Now i am taking a sub-string as input from user
3-assumed no elements.so created c and assigned with 0
4-my string is 'k1anha'
5-my sub-string is 'a'
6-iterating through my string
    iteration-1
        i='k',now checking  condition, the condition is false.
        so skip and go to next iteration
    iteration-2
        i='1',now checking  condition,the condition is false.
        so skip and go to next iteration
    iteration-3
        i='a',now checking  condition,the condition is true.
        so count 1 and go to next iteration
    iteration-4
        i='n',now checking condition,the condition is false.
        so skip and go to next iteration  
    iteration-5
        i='h',now checking  condition,the condition is false.
        so skip and go to next iteration
    iteration-6
        i='a',now checking  condition,the condition is true.
        so count 2 and go to next iteration  
    There is no more iteration.
7-Go to print function  and get output'''


#a given string how many vowel are present
'''s=input('enter a string:')
s1='aeiouAEIOU'
#s1='a','e','i','o','u','A','E','I','O','U'
c=0
for i in s:
    if i in s1:
        c+=1
print(c)        
'''

'''1-first i am taking string as input from user
2-Now i am mention s1='aeiouAEIOU' bcz in alphabet  'aeiouAEIOU' are vowels.
3-assumed no elements.so created c and assigned with 0
4-my string is 'k1anha'
5-iterating through my string
    iteration-1
        i='k',now checking  condition,condition is false.
        so skip and go to next iteration
    iteration-2
        i='1',now checking  condition,the condition is false.
        so skip and go to next iteration
    iteration-3
        i='a',now checking  condition,the condition is true.
        so count 1 and go to next iteration
    iteration-4
        i='n',now checking condition,the condition is false.
        so skip and go to next iteration  
    iteration-5
        i='h',now checking  condition,the condition is false.
        so skip and go to next iteration
    iteration-6
        i='a',now checking  condition,the condition is true.
        so count 2 and go to next iteration  
    There is no more iteration.
6-Go to print function  and get output  '''


#a given string how many consonant are present
'''s=input('enter a string:')
s1='aeiouAEIOU'
c=0
for i in s:
    if i.isalpha():
        if i not in s1:
            c+=1
print(c)  '''

'''for i in s:
    if i.isalpha() and i not in s1:
        c+=1
print(c) 
'''
'''1-first i am taking string as input from user
2-Now i am mention s1='aeiouAEIOU' bcz in alphabet without 'aeiouAEIOU' rest of alphabet are consonant.
3-assumed no elements.so created c and assigned with 0
4-my string is 'k1anha'
5-iterating through my string
    iteration-1
        i='k',now checking isalpha() condition,the condition is true.so go to if condition and check this.
        condition is true,so count 1 and go to next iteration
    iteration-2
        i='1',now checking isalpha() condition,the condition is false.
        so skip and go to next iteration
    iteration-3
        i='a',now checking isalpha() condition,the condition is true.so go to if condition and check this.
        condition is false,so skip and go to next iteration
    iteration-4
        i='n',now checking isalpha() condition,the condition is true.so go to if condition and check this.
        condition is true,so count 2 and go to next iteration  
    iteration-5
        i='h',now checking isalpha() condition,the condition is true.so go to if condition and check this.
        condition is true,so count 3 and go to next iteration
    iteration-6
        i='a',now checking isalpha() condition,the condition is true.so go to if condition and check this.
        condition is false and go to next iteration  
    There is no more iteration.
6-Go to print function  and get output'''

# given string how many digits are present
'''s=input()
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)      '''

'''1-first i am taking string as input from user
2-assumed no elements.so created c and assigned with 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking condition,
        the condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking condition,
        the condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking condition,
        the condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking condition,
        the condition is true,so count 1 and go to next iteration  
    iteration-5
        i='2',now checking condition,
        the condition is true,so count 2 and go to next iteration
    iteration-6
        i='3',now checking condition,
        the condition is true,so count 3 and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output        '''


#given string how many even digits are present
'''s=input()
c=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            c+=1
print(c)  '''

'''1-first i am taking string as input from user
2-assumed no elements.so created c and assigned with 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition, condition is true then '1' convert integer and check if condition,
        condition is false,so skip and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition, condition is true then '2' convert integer and check if condition,
        condition is true,so count 1 and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert integer and check if condition,
        condition is false,so skip and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output     '''


#given string how many odd digits are present
'''s=input()
c=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==1:
            c+=1
print(c)  '''

'''1-first i am taking string as input from user
2-assumed no elements.so created c and assigned with 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition,condition is true then '1' convert integer and check if condition,
        condition is true,so count 1 and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition,condition is true then '2' convert integer and check if condition,
        condition is false,so skip and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert integer and check if condition,
        condition is true,so count 2 and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output     '''


#given string how many even  and odd digits are present
'''s=input()
even=0
odd=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            even+=1
        else:
            odd+=1    
print(even)
print(odd)  '''

'''1-first i am taking string as input from user
2-assumed no elements.so created even & odd and assigned with 0 & 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition, condition is true then '1' convert integer.
        first check if condition is false so go to else part and condition is true
        so count 1 and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition, condition is true then '2' convert integer.
        first check if condition is true,so count 1 and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert integer.
        first check if condition is false so go to else part and condition is true
        so count 2 and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output     '''


#given string findout sum of  even numbers
'''s=input()
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            sum+=k
print(sum)  '''

'''1-first i am taking string as input from user
2-assumed no elements.so created sum and assigned with 0
3-my string is 'hai124'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition, condition is true then '1' convert integer and check if condition,
        condition is false,so skip and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition, condition is true then '2' convert integer and check if condition,
        condition is true,so sum=sum+k and go to next iteration
    iteration-6
        i='4',now checking isdigit() condition, condition is true then '4' convert integer and check if condition,
        condition is true,so sum=sum+k and go to next iteration  
    There is no more iteration.
5-Go to print function  and get output '''

#given string absolute difference between even and odd numbers
'''s=input()
evensum=0
oddsum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            evensum+=k
        else:
            oddsum+=k    
print(evensum)
print(oddsum)
if evensum>oddsum:
    diff=evensum-oddsum
else:
    diff=oddsum-evensum
print('absolute difference is ',diff)    
'''

'''1-first i am taking string as input from user
2-assumed no elements.so created even & odd and assigned with 0 & 0
3-my string is 'hai123'
4-iterating through my string
    iteration-1
        i='h',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='a',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-3
        i='i',now checking isdigit() condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='1',now checking isdigit() condition, condition is true then '1' convert integer and store in k.
        first check if condition is false so go to else part and condition is true
        so oddsum=oddsum+k and go to next iteration  
    iteration-5
        i='2',now checking isdigit() condition, condition is true then '2' convert integer and store in k.
        first check if condition is true,so evensum=evensum+k and go to next iteration
    iteration-6
        i='3',now checking isdigit() condition, condition is true then '3' convert integer and store in k.
        first check if condition is false so go to else part and condition is true
        so oddsum=oddsum+k and go to next iteration  
    There is no more iteration.
5-Go to print function  and print evensum and oddsum.
6-Now checking if condition,
        if condition is true,so diff=evensum-oddsum 
        if condition is false, so diff=oddsum-evensum
7-Then go to print function and print(diff)            '''


# given string how many special characters are present
'''s=input()
sc=0
for i in s:
    if not i.isalnum():
        sc+=1
print(sc)       ''' 

'''1-first i am taking string as input from user
2-assumed no elements.so created sc and assigned with 0
3-my string is 'h@a%3'
4-iterating through my string
    iteration-1
        i='h',now checking condition
        condition is false,so skip and go to next iteration
    iteration-2
        i='@',now checking condition
        condition is true,so count 1 and go to next iteration
    iteration-3
        i='a',now checking condition
        condition is false,so skip and go to next iteration
    iteration-4
        i='%',now checking condition
        condition is true,so count 2 and go to next iteration  
    iteration-5
        i='3',now checking condition
        condition is false,so skip and go to next iteration 
    There is no more iteration.
5-Go to print function  and get output'''
#print first N numbers
'''n=int(input('enter the values of n:'))
for i in range(1,n+1):
    print(i)  '''

'''1-first i am taking a values as input from user
2-this values store in variables n.
3-the value of n=5
4-iterating through given values
    iteration-1
        i=1, bcz user gives the starting values is 1. now check range function
        then go to next iteration.
    iteration-2
        i=2,now check range function
        then go to next iteration.
    iteration-3
        i=3,now check range function
        then go to next iteration.
    iteration-4
        i=4,now check range function
        then go to next iteration.
    iteration-5
        i=5,now check range function
        then go to next iteration.
    There is no more iteration.  
5-Go to print function  and get output'''


#print sum of first n numbers
'''n=int(input('enter the values of n:'))
s=0
for i in range(1,n+1):
    s=s+i
print(s)   '''

'''1-first i am taking a values as input from user
2-this values store in variables n.
3-assumed no elements.so created c and assigned with 0 bcz sum is 0. 
4-the value of n=5
5-iterating through given values
    iteration-1
        i=1, bcz user gives the starting values is 1. now check range function
        then  add the values of i with s.now s=1,go to next iteration.
    iteration-2
        i=2,now check range function
        then  add the values of i with s.now s=3,go to next iteration.
    iteration-3
        i=3,now check range function
        then  add the values of i with s.now s=6,go to next iteration.
    iteration-4
        i=4,now check range function
        then  add the values of i with s.now s=10,go to next iteration.
    iteration-5
        i=5,now check range function
        then  add the values of i with s.now s=15,go to next iteration.
    There is no more iteration.  
6-Go to print function  and get output  '''


#print factorial of given numbers
'''n=int(input('enter the values of n:'))
f=1
for i in range(1,n+1):
    f=f*i
print(f)    '''

'''1-first i am taking a values as input from user
2-this values store in variables n.
3-assumed no elements.so created c and assigned with 0 bcz factoria of 0  is 1. 
4-the value of n=5
5-iterating through given values
    iteration-1
        i=1, bcz user gives the starting values is 1. now check range function
        then  multiply the values of i with f.now f=1,go to next iteration.
    iteration-2
        i=2,now check range function
        then  multiply the values of i with f.now f=2,go to next iteration.
    iteration-3
        i=3,now check range function
        then  multiply the values of i with f.now f=6,go to next iteration.
    iteration-4
        i=4,now check range function
        then  multiply the values of i with f.now f=24,go to next iteration.
    iteration-5
        i=5,now check range function
        then  multiply the values of i with f.now f=120,go to next iteration.
    There is no more iteration.  
6-Go to print function  and get output  '''


#given numbers is perfect or not
'''n=int(input('enter the values of n:'))
sd=0
for i in range(1,n//2+1):
    if n%i==0:
        sd+=i
if sd==n:
    print('perfect number')
else:
    print('not a perfect number')     ''' 

'''1-first i am taking a values as input from user
2-this values store in variables n.
3-assumed no elements.so created sd and assigned with 0 bcz sum divisor is 0. 
4-the value of n=6
5-iterating through given values
    iteration-1
        i=1, bcz user gives the starting values is 1. now check range function
        then  go to if condition,condition is true.so sd=1 and go to next iteration.
    iteration-2
        i=2,now check range function
        then  go to if condition,condition is true.so sd=3 and go to next iteration.
    iteration-3
        i=3,now check range function
        then  go to if condition,condition is true.so sd=6 and go to next iteration.
    iteration-4
        i=4,now check range function
        then  go to if condition,condition is false.go to next iteration
    iteration-5
        i=5,now check range function.range function not satisfied.   
    There is no more iteration.  
6-now check if condition.if condition is true.   
7-Go to print function  and get output'''
#breaking inner loop with inner loop value            [I]
'''
for i in range(1,5):
    for j in range(1,5):
        if j==3:
            break
        print(i,j)
        
outer loop take i=1
    then inner loop take j=1
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=1 and j=1

    then inner loop take j=2
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=1 and j=2
        
    then inner loop take j=3
    then check if condition ( satishfies)
    then go if block
    break the inner loop
outer loop take i=2
    then inner loop take j=1
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=2 and j=1

    then inner loop take j=2
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=2 and j=2
        
    then inner loop take j=3
    then check if condition ( satishfies)
    then go if block
    break the inner loop       
outer loop take i=3
    then inner loop take j=1
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=3 and j=1

    then inner loop take j=2
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=3 and j=2
        
    then inner loop take j=3
    then check if condition ( satishfies)
    then go if block
    break the inner loop        
outer loop take i=4
    then inner loop take j=1
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=4 and j=1

    then inner loop take j=2
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=4 and j=2
        
    then inner loop take j=3
    then check if condition ( satishfies)
    then go if block
    break the inner loop'''
#breaking inner loop with inner loop value            [II]
  '''  
for i in range(1,5):
    for j in range(1,5):
         print(i,j)
         if j==3:
            break
        
outer loop take i=1 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=1,j=1
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=2
    then enter print statement ,print i=1,j=2
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=1
    then enter print statement ,print i=1,j=3
    then enter to if block,check condition(satishfies)
    break inner loop
outer loop take i=2 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=2,j=1
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=2
    then enter print statement ,print i=2,j=2
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=1
    then enter print statement ,print i=2,j=3
    then enter to if block,check condition(satishfies)
    break inner loop    
outer loop take i=3 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=3,j=1
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=2
    then enter print statement ,print i=3,j=2
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=1
    then enter print statement ,print i=3,j=3
    then enter to if block,check condition(satishfies)
    break inner loop    
outer loop take i=4 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=4,j=1
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=2
    then enter print statement ,print i=4,j=2
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=1
    then enter print statement ,print i=4,j=3
    then enter to if block,check condition(satishfies)
    break inner loop '''
 #
 '''
 for i in range(1,6):
    for j in range(1,6):
        if i==3:
            break
        print(i,j)

        
outer loop take i=1
    then inner loop take j=1
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=1 and j=1

    then inner loop take j=2
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=1 and j=2
        
    then inner loop take j=3
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=1 and j=3

        
    then inner loop take j=4
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=1 and j=4
    
        
    then inner loop take j=5
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=1 and j=5

outer loop take i=2
    then inner loop take j=1
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=2 and j=1

    then inner loop take j=2
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=2 and j=2
        
    then inner loop take j=3
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=2 and j=3

        
    then inner loop take j=4
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=2 and j=4
    
        
    then inner loop take j=5
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=2 and j=5
outer loop take i=3
    then enter to inner loop j=1
    then enter to if condition and check condition condition(satisfies)
    enter to if bloock and break the loop
outer loop take i=4
    then inner loop take j=1
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=4 and j=1

    then inner loop take j=2
    then check if condition (not satishfies)
    then do not go if block
    then come to print statement ,print the value i=4 and j=2
        
    then inner loop take j=3
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=4 and j=3

        
    then inner loop take j=4
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=4 and j=4
    
        
    then inner loop take j=5
    then check if condition ( not satishfies)
    then  dont go if block
    then come to print statement ,print the value i=4 and j=5
'''
#
'''
  for i in range(1,5):
    for j in range(1,5):
        print(i,j)
        if i==3:
            break
outer loop take i=1 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=1,j=1
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=2
    then enter print statement ,print i=1,j=2
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=3
    then enter print statement ,print i=1,j=3
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=4
    then enter print statement ,print i=1,j=4
    then enter to if block,check condition(not satishfies)
    
outer loop take i=2 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=2,j=1
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=2
    then enter print statement ,print i=2,j=2
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=3
    then enter print statement ,print i=2,j=3
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=4
    then enter print statement ,print i=2,j=4
    then enter to if block,check condition(not satishfies)
    
outer loop take i=3 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=3,j=1
    then enter to if block,check condition(satishfies)
    break inner loop
    
outer loop take i=4 and enter to inner loop
    then inner loop take j=1
    then enter print statement ,print i=4,j=1
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=2
    then enter print statement ,print i=4,j=2
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=3
    then enter print statement ,print i=4,j=3
    then enter to if block,check condition(not satishfies)
    
    then inner loop take j=4
    then enter print statement ,print i=4,j=4
    then enter to if block,check condition(not satishfies)
    '''
#
'''
  for i in range(1,5):
    for j in range(1,5):
        print(i,j)
    if i==3:
        break
        
outer loop take i=1 and enter the inner loop
    then inner loop take j=1
    then enter print satement,print i=1,j=1
    
    then inner loop take j=2
    then enter print satement,print i=1,j=2

    then inner loop take j=3
    then enter print satement,print i=1,j=3

    then inner loop take j=4
    then enter print satement,print i=1,j=4
    
    come out from inner loop
    then check if condition(not satisfied)
    
outer loop take i=2 and enter the inner loop
    then inner loop take j=1
    then enter print satement,print i=2,j=1
    
    then inner loop take j=2
    then enter print satement,print i=2,j=2

    then inner loop take j=3
    then enter print satement,print i=2,j=3

    then inner loop take j=4
    then enter print satement,print i=2,j=4
    
    come out from inner loop
    then check if condition(not satisfied)
    
outer loop take i=3 and enter the inner loop
    then inner loop take j=1
    then enter print satement,print i=3,j=1
    
    then inner loop take j=2
    then enter print satement,print i=3,j=2

    then inner loop take j=3
    then enter print satement,print i=3,j=3

    then inner loop take j=4
    then enter print satement,print i=3,j=4
    
    come out from inner loop
    then check if condition(satisfied)
    break the outer loop
    '''
#
''''
  for i in range(1,5):
    for j in range(1,5):
        print(i,j)
    if j==3:
        break
outer loop take i=1 and enter the inner loop
    then inner loop take j=1
    then enter print satement,print i=1,j=1
    
    then inner loop take j=2
    then enter print satement,print i=1,j=2

    then inner loop take j=3
    then enter print satement,print i=1,j=3

    then inner loop take j=4
    then enter print satement,print i=1,j=4
    
    come out from inner loop
    then check if condition(not satisfied)
    
outer loop take i=2 and enter the inner loop
    then inner loop take j=1
    then enter print satement,print i=2,j=1
    
    then inner loop take j=2
    then enter print satement,print i=2,j=2

    then inner loop take j=3
    then enter print satement,print i=2,j=3

    then inner loop take j=4
    then enter print satement,print i=2,j=4
    
    come out from inner loop
    then check if condition(not satisfied)

outer loop take i=3 and enter the inner loop
    then inner loop take j=1
    then enter print satement,print i=3,j=1
    
    then inner loop take j=2
    then enter print satement,print i=3,j=2

    then inner loop take j=3
    then enter print satement,print i=3,j=3

    then inner loop take j=4
    then enter print satement,print i=3,j=4
    
    come out from inner loop
    then check if condition(not satisfied)
    
outer loop take i=4 and enter the inner loop
    then inner loop take j=1
    then enter print satement,print i=4,j=1
    
    then inner loop take j=2
    then enter print satement,print i=4,j=2

    then inner loop take j=3
    then enter print satement,print i=4,j=3

    then inner loop take j=4
    then enter print satement,print i=4,j=4
    
    come out from inner loop
    then check if condition(not satisfied)    
    
