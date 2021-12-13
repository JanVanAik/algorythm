import hashlib

s = 'lalalolo, its time to code, comrade!co'
substring_1 = 'la'
substring_2 = 'co'
substring_3 = 'lo'
substring_4 = 'time'
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
for i in range(len(s) - len(substring_1) + 1):
    if hashlib.sha1(substring_1.encode('utf-8')).hexdigest() == hashlib.sha1(
            (s[i:i + len(substring_1)]).encode('utf-8')).hexdigest():
        counter_1 += 1
    if hashlib.sha1(substring_2.encode('utf-8')).hexdigest() == hashlib.sha1(
            (s[i:i + len(substring_2)]).encode('utf-8')).hexdigest():
        counter_2 += 1
    if hashlib.sha1(substring_3.encode('utf-8')).hexdigest() == hashlib.sha1(
            (s[i:i + len(substring_3)]).encode('utf-8')).hexdigest():
        counter_3 += 1
    if hashlib.sha1(substring_4.encode('utf-8')).hexdigest() == hashlib.sha1(
            (s[i:i + len(substring_4)]).encode('utf-8')).hexdigest():
        counter_4 += 1
print(
    f'{substring_1} : {counter_1},\n{substring_2} : {counter_2},\n{substring_3} : {counter_3},\n{substring_4} : {counter_4}')
