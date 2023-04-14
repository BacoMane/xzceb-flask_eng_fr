"""```py
```"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get('apikey')
url = os.environ.get('url')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ func en-fr """
    #write the code here
    if english_text in ('', None):
        french_text = None
    else:
        french_text = language_translator.translate(text=english_text,model_id='en-fr').\
         get_result()['translations'][0]['translation']
        #print(french_text)
    return french_text

def french_to_english(french_text):
    """ func fr-en """
    #write the code here
    if french_text in ('', None):
        english_text = None
    else:
        english_text = language_translator.translate(text=french_text,model_id='fr-en').\
         get_result()['translations'][0]['translation']
    return english_text
print(english_to_french('hello'))