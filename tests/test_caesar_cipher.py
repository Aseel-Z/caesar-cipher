import pytest

from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt
from caesar_cipher.caesar_cipher import decrypt
from caesar_cipher.caesar_cipher import crack
from caesar_cipher.caesar_cipher import is_code_broken

def test_version():
    assert __version__ == '0.1.0'

# 1 encrypt a string with a given shift
def test_encrypt():
    actual = encrypt('abc',1)
    expected = 'bcd'
    assert actual == expected


#2 decrypt a previously encrypted string with the same shift
def test_decrypt():
    actual = decrypt('abc',-1)
    expected = encrypt('abc',1)
    assert actual == expected

#3 encryption should handle upper and lower case letters
#4 encryption should allow non-alpha characters but ignore them, including white space
#5 decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.