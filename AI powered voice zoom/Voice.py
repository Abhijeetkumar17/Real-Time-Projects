import speech_recognition as sr
import pyautogui

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def recognize_command():
    with sr.Microphone() as source:
        print("Listening for 'Zoom In' or 'Zoom Out'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Speech Recognition service unavailable.")
            return None

# Function to zoom in/out
def zoom_control(command):
    if "zoom in" in command:
        pyautogui.hotkey("ctrl", "+")  # Zoom In
        print("Zooming In...")
    elif "zoom out" in command:
        pyautogui.hotkey("ctrl", "-")  # Zoom Out
        print("Zooming Out...")
    else:
        print("No zoom command detected.")

# Run continuously
while True:
    user_command = recognize_command()
    if user_command:
        zoom_control(user_command)