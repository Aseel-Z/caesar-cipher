# english_words = nltk.corpus.words.words()

import ntlk 
def encrypt(phrase, shift):
    """ a function that takes in a plain text phrase and a numeric shift, 
    shifts the letters in the phrase according to the shift value and returns a shifted phrase.

    #1 E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’

    *** Note that shifts that exceed 26 should wrap around *** 
    #2 E.g. encrypt(‘abc’,27) would return ‘bcd’

    *** shifts that push a letter out or range should wrap around  ***
    #3 E.g. encrypt(‘zzz’,1) would return ‘aaa’ """
    encrypted_phrase = ''
    for character in phrase:
        if character.isupper():
            char_unicode = ord(character)
            char_index = char_unicode - ord('A')
            shifted_index = (char_index + shift)%26 + ord('A')
            char_shifted = chr(shifted_index)
            encrypted_phrase+=char_shifted
        elif character.islower():
            char_unicode = ord(character)
            char_index = char_unicode - ord('a')
            shifted_index = (char_index + shift)%26 + ord('a')
            char_shifted = chr(shifted_index)
            encrypted_phrase+=char_shifted
    return encrypted_phrase


def decrypt(encrypted_text,shift):
    """function that takes in encrypted text and numeric shift which will restore the encrypted
     text back to its original form when correct key is supplied."""
    return encrypt(encrypted_text, -1*shift)




def crack(encrypted_text):
    """function that will decode the cipher so that 
    an encrypted message can be transformed into its original state WITHOUT access to the key. """
    words = encrypted_text.split()
    # word_count = 



def is_code_broken():
    """ Devise a method for the computer to determine if code was broken with minimal human guidance."""

