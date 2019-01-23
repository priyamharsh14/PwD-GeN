import string
import random
from optparse import OptionParser

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("__________         ________      ________        _______   ")
print("\______   \__  _  _\______ \    /  _____/  ____  \      \  ")
print(" |     ___/\ \/ \/ /|    |  \  /   \  ____/ __ \ /   |   \ ")
print(" |    |     \     / |    \   \ \    \_\  \  ___//    |    \ ")
print(" |____|      \/\_/ /_______  /  \______  /\___  >____|__  /")
print("                           \/          \/     \/        \/")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("Author: Priyam Harsh")
print()

allchar = ''.join([string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation])
parser = OptionParser(usage="Usage: %prog [options] filename",version="%prog 1.0")
parser.add_option("-l", "--length",dest="length", default=4, help="Length of the password", type="int")
parser.add_option("-c", "--lcase",dest="lowercase", default=1, help="Minimum no. of Lower Case alphabets", type="int")
parser.add_option("-u", "--ucase",dest="uppercase", default=1, help="Minimum no. of Upper Case alphabets", type="int")
parser.add_option("-s", "--schar",dest="specialcharacter", default=1, help="Minimum no. of Special Characters", type="int")
parser.add_option("-d", "--digit",dest="digit", default=1, help="Minimum no. of Digits", type="int")
parser.add_option("-n", "--number",dest="number", default=1, help="Number of passwords required", type="int")

(options, args) = parser.parse_args()

if len(args) != 1:
    parser.error("[-] Please enter the output filename")

if (options.lowercase+options.uppercase+options.specialcharacter+options.digit)>options.length:
    parser.error("[-] Length of the password should be greater or equal to the entered parameters")

fp = open(args[0],'w')
l = []
n = options.number

while n!=0:
    password = ''.join([random.choice(allchar) for _ in range(options.length)])
    sl,su,sd,sp = 0,0,0,0
    for i in password:
        if i in string.ascii_lowercase:
            sl+=1
        if i in string.ascii_uppercase:
            su+=1
        if i in string.digits:
            sd+=1
        if i in string.punctuation:
            sp+=1
    if sl>=options.lowercase and su>=options.uppercase and sd>=options.digit and sp>=options.specialcharacter:
        l.append(password)
        n-=1

for i in l:
    fp.write(i+"\n")

print("[+] Password Generated Successfully !!")
