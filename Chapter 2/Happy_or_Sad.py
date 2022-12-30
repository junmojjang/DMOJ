# ccc15j2

n = input()
h = 0
s = 0

for i in range(0,len(n)):
    if n[i] == ':':
        # if i+1<len(n):
        if n[i+1] == '-':
            # if i +2 <len(n):
            if n[i+2] ==")":
                h = h+1
            elif n[i+2] == '(':
                s = s+1
if s>h:
    print('sad')
elif h>s:
    print("happy")
elif h==s and h>0:
    print('unsure')
else:
    print('none')
