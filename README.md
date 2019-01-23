# PwD-GeN
A custom password generator tool written in Python3

## Installation:
```
$ git clone https://github.com/priyamharsh14/PwD-GeN.git
```

## Usage:
```
$ python pwd_gen.py --help

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
__________         ________      ________        _______
\______   \__  _  _\______ \    /  _____/  ____  \      \
 |     ___/\ \/ \/ /|    |  \  /   \  ____/ __ \ /   |   \
 |    |     \     / |    \   \ \    \_\  \  ___//    |    \
 |____|      \/\_/ /_______  /  \______  /\___  >____|__  /
                           \/          \/     \/        \/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Author: Priyam Harsh

Usage: pwd_gen.py [options] filename

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -l LENGTH, --length=LENGTH
                        Length of the password
  -c LOWERCASE, --lcase=LOWERCASE
                        Minimum no. of Lower Case alphabets
  -u UPPERCASE, --ucase=UPPERCASE
                        Minimum no. of Upper Case alphabets
  -s SPECIALCHARACTER, --schar=SPECIALCHARACTER
                        Minimum no. of Special Characters
  -d DIGIT, --digit=DIGIT
                        Minimum no. of Digits
  -n NUMBER, --number=NUMBER
                        Number of passwords required
```

Create password as per your need -
```
$ python pwd_gen.py [options] <output filename>
```
