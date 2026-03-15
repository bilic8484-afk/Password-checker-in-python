
password=input("Enter a password")
w=0
m=0
s=0
if len(password) < 8:
    w=+1
else:
    for i in range(len(password)):
        if password[i] in "QWERTZUIOPŠĐASDFGHJKLČĆYXCVBNM" or password[i] in "qwertzuiopšđasdfghjklčćyxcvbnm" or password[i] in "1234567890":
            w=0
            m=+1
        elif password[i] in "!#$%&/?*":
            s=+1
            m=0
if w > 0:
    print("password is weak")
elif m > 0:
    print("password is medium")
elif s>0:
    print("password is strong")