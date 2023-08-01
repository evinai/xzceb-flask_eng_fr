'''
Module which includes functions that translate english to frenceh and french to english.

'''

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    '''
    Translate given english text to french text.

    '''
    french_text = MyMemoryTranslator(source="en-GB", target="fr-FR").translate(
        english_text
    )

    return french_text


def french_to_english(french_text):
    '''
    Translate given french text to fenglish text.
    
    '''
    english_text = MyMemoryTranslator(source="fr-FR", target="en-GB").translate(
        french_text
    )

    return english_text

