import speech_recognition as sr
import os
import re

def listen_and_convert():
    """Listen to the user's voice and convert it into text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak the file path to delete (Example: Delete file C:/Users/YourName/Desktop/test.txt)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"📝 Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand the audio")
            return None
        except sr.RequestError:
            print("❌ Could not connect to the recognition service")
            return None
def extract_file_path(text):
    """Extract file path from the recognized text"""
    # Regex to detect Windows-style paths like C:\Users\...
    pattern = r"[A-Za-z]:\\[^\s]+"
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return None
def delete_file(file_path):
    """Delete the file from the system"""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"✅ File deleted: {file_path}")
    else:
        print(f"⚠️ File not found: {file_path}")
if __name__ == "__main__":
    spoken_text = listen_and_convert()
    if spoken_text:
        path = extract_file_path(spoken_text)
        if path:
            delete_file(path)
        else:
            print("⚠️ No valid file path found in the speech. Try typing it instead.")
            manual_path = input("✍️ Enter file path manually: ")
            delete_file(manual_path)
    else:
        manual_path = input("✍️ Enter file path manually: ")
        delete_file(manual_path)