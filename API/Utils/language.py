from googletrans import Translator
from langdetect import detect



translator=Translator()


def lang_to_eng(input_text):

    lang = detect(input_text)
    
    translated=translator.translate(input_text,dest='en')

    return lang,translated.text


def eng_to_lang(response,lang):

    translated=translator.translate(response,dest=lang)

    return translated.text





