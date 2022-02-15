from googletrans import Translator

# print(googletrans.LANGUAGES)

translator = Translator()
result = translator.translate('Приет как дела', src='ru', dest='en')
print(result.text)