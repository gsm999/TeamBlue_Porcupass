import random
n = False
sc = False
l = False
u = False
length = 20
password = ""

if n and sc and l:
    i = 0
    while i < length:
        random1 = random.randint(48, 57)
        scrandom1 = random.randint(33, 47)
        scrandom2 = random.randint(58, 64)
        scrandom3 = random.randint(91, 96)
        scrandom4 = random.randint(123, 126)
        scL = [scrandom1, scrandom2, scrandom3, scrandom4]
        random2 = random.choice(scL)
        random3 = random.randint(97, 122)
        L = [random1, random2, random3]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif n and sc and u:
    i = 0
    while i < length:
        random1 = random.randint(48, 57)
        scrandom1 = random.randint(33, 47)
        scrandom2 = random.randint(58, 64)
        scrandom3 = random.randint(91, 96)
        scrandom4 = random.randint(123, 126)
        scL = [scrandom1, scrandom2, scrandom3, scrandom4]
        random2 = random.choice(scL)
        random3 = random.randint(65, 90)
        L = [random1, random2, random3]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif n and sc:
    i = 0
    while i < length:
        random1 = random.randint(48, 57)
        scrandom1 = random.randint(33, 47)
        scrandom2 = random.randint(58, 64)
        scrandom3 = random.randint(91, 96)
        scrandom4 = random.randint(123, 126)
        scL = [scrandom1, scrandom2, scrandom3, scrandom4]
        random2 = random.choice(scL)
        crandom1 = random.randint(65, 90)
        crandom2 = random.randint(97, 122)
        cL = [crandom1, crandom2]
        random3 = random.choice(cL)
        L = [random1, random2, random3]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif n and l:
    i = 0
    while i < length:
        random1 = random.randint(48, 57)
        random2 = random.randint(97, 122)
        L = [random1, random2]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif n and u:
    i = 0
    while i < length:
        random1 = random.randint(48, 57)
        random2 = random.randint(65, 90)
        L = [random1, random2]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif sc and l:
    i = 0
    while i < length:
        scrandom1 = random.randint(33, 47)
        scrandom2 = random.randint(58, 64)
        scrandom3 = random.randint(91, 96)
        scrandom4 = random.randint(123, 126)
        scL = [scrandom1, scrandom2, scrandom3, scrandom4]
        random1 = random.choice(scL)
        random2 = random.randint(97, 122)
        L = [random1, random2]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif sc and u:
    i = 0
    while i < length:
        scrandom1 = random.randint(33, 47)
        scrandom2 = random.randint(58, 64)
        scrandom3 = random.randint(91, 96)
        scrandom4 = random.randint(123, 126)
        scL = [scrandom1, scrandom2, scrandom3, scrandom4]
        random1 = random.choice(scL)
        random2 = random.randint(65, 90)
        L = [random1, random2]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif n:
    i = 0
    while i < length:
        random1 = random.randint(48, 57)
        crandom1 = random.randint(65, 90)
        crandom2 = random.randint(97, 122)
        cL = [crandom1, crandom2]
        random2 = random.choice(cL)
        L = [random1, random2]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif sc:
    i = 0
    while i < length:
        scrandom1 = random.randint(33, 47)
        scrandom2 = random.randint(58, 64)
        scrandom3 = random.randint(91, 96)
        scrandom4 = random.randint(123, 126)
        scL = [scrandom1, scrandom2, scrandom3, scrandom4]
        random1 = random.choice(scL)
        crandom1 = random.randint(65, 90)
        crandom2 = random.randint(97, 122)
        cL = [crandom1, crandom2]
        random2 = random.choice(cL)
        L = [random1, random2]
        value = random.choice(L)
        password += chr(value)
        i += 1
elif l:
    i = 0
    while i < length:
        value = random.randint(97, 122)
        password += chr(value)
        i += 1
elif u:
    i = 0
    while i < length:
        value = random.randint(65, 90)
        password += chr(value)
        i += 1
else:
    i = 0
    while i < length:
        crandom1 = random.randint(65, 90)
        crandom2 = random.randint(97, 122)
        cL = [crandom1, crandom2]
        value = random.choice(cL)
        password += chr(value)
        i += 1
print(password)