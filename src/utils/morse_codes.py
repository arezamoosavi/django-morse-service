codes = """
0 -----
1 .----
2 ..---
3 ...--
4 ....-
5 .....
6 -....
7 --...
8 ---..
9 ----.
a .-
b -...
c -.-.
d -..
e .
f ..-.
g --.
h ....
i ..
j .---
k -.-
l .-..
m --
n -.
o ---
p .--.
q --.-
r .-.
s ...
t -
u ..-
v ...-
w .--
x -..-
y -.--
z --..
. .-.-.-
  --..--
? ..--..
! -.-.--
- -....-
/ -..-.
@ .--.-.
( -.--.
) -.--.-
""".split("\n")
morse_codes = {el[0]: el[2:] for el in codes if el}

"""from morse.models import MorseCombination
for alp, mrs in morse_codes.items():
    data = {
    "word": alp,
    "combination": mrs,
    }
    MorseCombination.objects.create(**data)
"""

def get_morse_code(word):
    return morse_codes[word]
# print(morse_codes['0'])
# print(get_morse_code('p'))