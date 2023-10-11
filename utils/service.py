from googletrans import Translator

translator = Translator()


def translate_uz(text):
    translation = translator.translate(text, src='uz', dest='en')
    return translation.text


def translate_en(text):
    translation = translator.translate(text, src='en', dest='uz')
    return translation.text