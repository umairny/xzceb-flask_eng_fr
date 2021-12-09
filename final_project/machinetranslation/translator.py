""" Translator for flask app """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    '''The fuction translate english into french'''
    translation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    frenchtext = translation['translations'][0]['translation']
    return frenchtext

#french to english function
def french_to_english(frenchtext):
    '''The fuction translate french into english'''
    translation = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    englishtext = translation['translations'][0]['translation']
    return englishtext

#print(englishToFrench('Hello'))
#print(frenchToEnglish('Bonjour'))
