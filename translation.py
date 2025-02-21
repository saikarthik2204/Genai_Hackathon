import streamlit as st
from googletrans import Translator
import socket
import time

# Initialize the translator
translator = Translator()

# Streamlit UI
st.title("TransLingua: AI-Powered Multi-Language Translator")
st.markdown("Translate text seamlessly between multiple languages.")

# Input text and language selection
text_to_translate = st.text_area("Enter the text to translate", "")

# Adding more languages
languages = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Chinese (Simplified)': 'zh-CN',
    'Chinese (Traditional)': 'zh-TW',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Estonian': 'et',
    'Finnish': 'fi',
    'French': 'fr',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Hebrew': 'he',
    'Hindi': 'hi',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Indonesian': 'id',
    'Italian': 'it',
    'Japanese': 'ja',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Korean': 'ko',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Macedonian': 'mk',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Polish': 'pl',
    'Portuguese (Portugal)': 'pt',
    'Portuguese (Brazil)': 'pt-BR',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Serbian': 'sr',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Spanish': 'es',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Yiddish': 'yi'
}

# Language options for source and target languages
language_list = list(languages.keys())

# User selects source and target languages
source_language = st.selectbox("Select Source Language", language_list)
target_language = st.selectbox("Select Target Language", language_list)

# Translate function
def translate_text(text, source_lang, target_lang):
    try:
        # Perform translation
        translated = translator.translate(text, src=languages[source_lang], dest=languages[target_lang])
        return translated.text
    except socket.error:
        st.error("Network error. Please check your internet connection.")
        return None
    except Exception as e:
        st.error(f"Error occurred during translation: {str(e)}")
        return None

# Button to trigger translation
if st.button('Translate'):
    if text_to_translate:
        translated_text = translate_text(text_to_translate, source_language, target_language)
        if translated_text:
            st.success(f"Translated Text: {translated_text}")
    else:
        st.error("Please enter text to translate.")
