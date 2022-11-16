print("encrpter by chase byrne, if you see this and you are not running it kill the app your running!!!")
a = input('?')
if(a[0]=='f'):
    if(a[1]==':'):
        a = a.replace('f:','');
        a = open(a,'r').read();
aint =0
password =0;
try:
    aint = int(a)
    password = int(input('?'))
except:
    print("error only numbers for now!!!")
    exit();

output = aint * password;
print (output)
