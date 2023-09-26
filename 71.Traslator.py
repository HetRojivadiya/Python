import speech_recognition as sr
from googletrans import Translator, LANGUAGES

def translate_hindi_to_english(text):
    try:
        translator = Translator()
        translation = translator.translate(text, src='hi', dest='en')
        return translation.text
    except Exception as e:
        return str(e)

def main():
    recognizer = sr.Recognizer()
   
    with sr.Microphone() as source:
        print("Say something in Hindi (or type 'exit' to quit):")
        audio = recognizer.listen(source)

    try:
        hindi_text = recognizer.recognize_google(audio, language='hi-IN')

        print("Hindi Input:", hindi_text)

        english_translation = translate_hindi_to_english(hindi_text)
        print("English Translation:", english_translation)

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()
