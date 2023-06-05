str0='my name is pavan'
str1='my name is "pavan"'
str2="my name is 'pavan'"
chr='a'
print(str0,chr,str1,str2)

print("""Hello
welcome""")
print("hello\
      welcome")
a='Dogs are good'
print(a[0])
#a[0]='H' string is immutable
print(a[2:5])  #2,3,4
print(a[:5])  #0,1,2,3,4 start to 4th char
print(a[8:])  #8,9,10,... from 8th char
print(a[:-2]) # last two char removed
print(a[-2:]) # only last 2 char
print(a[-3:-2]) #from last 3rd char to 1 char(3-2)
print(a[-5:-2]) #from last 5th char to 3 chars(5-2)
print(a[2:2])
print(a[::2])
a='My name is '
b='pavan'
print(a+b)
print(f"My name is {b}")
print("my name is {0}".format(b))
print("my name is {b}".format(b='pavan'))
print("%s%s" %(a,b)) #%d for int,%f for float
print("hit\nghj")
print("hit\tghj")
print("hit\\ghj")
print("hit\'ghj")
print("hit\"ghj")
print(len(a))
print(str(1+3j))
print(a.lower(),a.upper())
a=' acgfji  '
print(a.strip())
b='456'
print(b.isdigit())
a="     "
print(a.isspace())
print(str0.startswith('m'))
print(str0.startswith('f'))
print("hoemeowner".find('meow'))
print("venkat".replace('v','b'))
x='No. Okay. Why?'.split('.')
print(type(x),x)
print("*".join(['red','green','blue']))
print(
'hey'<'hi',
'check'=='check',
'yes'!='no',
'ba'+'na'*2,
'na' in 'banana',
'less' not in 'helpless',
#'Hey' is 'Hi',
#'Yo' is not 'yo'
'' and '1',
'1' and '',
'1' and '1',
'' or '1',
'1' or '',
not('1'),
not("")
)
