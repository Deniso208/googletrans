from colorama import Fore,Style
from googletrans import Translator, LANGUAGES

def TransLate(txt, lang):
    try:
        translator = Translator()
        result = translator.translate(txt, dest=lang)
        languages, confidence = LangDetect(result.text)
        print(f"Мова тексту: {languages}",f" Confidence: {confidence}")
        CodeLang(lang)
        print(Fore.GREEN  + result.text)
        print(Style.RESET_ALL)
    except Exception as e:
        print("Помилка перекладу\nError Translate")
        print(e)

def LangDetect(txt):
    translator = Translator()
    detection = translator.detect(txt)
    language = LANGUAGES[detection.lang]
    return language, detection.confidence

def CodeLang(lang):
    language_code = lang
    language_name = LANGUAGES.get(language_code)
    print(f"Назва мови для коду '{language_code}': {language_name}")


def main():
    txt = input('Введіть текст для перекладу: ')
    lang = input('Введіть код мови, на яку потрібно перевести: ')
    TransLate(txt, lang)

if __name__ == '__main__':
    main()