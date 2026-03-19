import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
tts = pyttsx3.init()

def diagnose_microphone():
    mic_list = sr.Microphone.list_microphone_names()
    if not mic_list:
        print('No microphones found.')
        return None
    print('Microphones detected:')
    for i, mic in enumerate(mic_list):
        print(f'[{i}] {mic}')
    return mic_list

# Function for Google Speech Recognition
def google_speech_recognition():
    try:
        with sr.Microphone() as source:
            print('Please speak something:')
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='pt-PT')
            print('You said: ' + text)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print(f'Could not request results from Google Speech Recognition service; {e}')

# Function for PocketSphinx fallback
def pocketsphinx_fallback():
    try:
        with sr.Microphone() as source:
            print('Please speak something (PocketSphinx):')
            audio = recognizer.listen(source)
            text = recognizer.recognize_sphinx(audio, language='pt-PT')
            print('You said (PocketSphinx): ' + text)
    except sr.UnknownValueError:
        print('PocketSphinx could not understand audio')

# Function for keyboard fallback
def keyboard_fallback():
    text = input('Please type something: ')
    print('You typed: ' + text)

# Main function
if __name__ == '__main__':
    diagnose_microphone()
    google_speech_recognition()  # Try Google first
    pocketsphinx_fallback()  # Fallback to PocketSphinx
    keyboard_fallback()  # Fallback to keyboard input
    # Text-to-speech output
    tts.say('Voice recognition completed. Thank you!')
    tts.runAndWait()