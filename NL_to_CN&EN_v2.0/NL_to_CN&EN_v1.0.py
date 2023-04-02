import requests

DEEPL_API_KEY = '9f826866-2180-bd24-65e6-9f26bd072725:fx'

def translate(text, target_lang):
    url = 'https://api-free.deepl.com/v2/translate'
    params = {
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'target_lang': target_lang
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        raise Exception('Failed to translate text: {}'.format(response.content))
    return response.json()['translations'][0]['text']

while True:
    dutch_text = input('Enter Dutch text to translate (or "q" to quit): ')
    if dutch_text == 'q':
        break
    english_text = translate(dutch_text, 'EN')
    chinese_text = translate(dutch_text, 'ZH')
    print('Dutch text: {}'.format(dutch_text))
    print('English translation: {}'.format(english_text))
    print('Chinese translation: {}\n'.format(chinese_text))
