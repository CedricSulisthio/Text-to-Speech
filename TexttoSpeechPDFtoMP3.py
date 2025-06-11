# Text to Speech PDF to MP3

import pyttsx3
import PyPDF2

def extract_text_from_pdf(pdf_path, page_num):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        if page_num < len(pdf_reader.pages):
            page_object = pdf_reader.pages[page_num]
            text = page_object.extract_text()
            return text
        else:
            print("Page number out of range.")
            return ""

def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    engine.stop()

def save_text_to_audio(text, f_name='test.mp3'):
    engine = pyttsx3.init()
    engine.save_to_file(text, f_name)
    engine.runAndWait()
    
if __name__ == "__main__":
    pdf_path = r"C:\Users\Cedric Sulisthio\Documents\IBEProjectsandTutor\Artificial Intelligence for Business\AIPDFTest.pdf"
    page_num = 0  # Page number to extract text from

    text = extract_text_from_pdf(pdf_path, page_num)
    
    if text:
        print(text)
        speak_text(text[:500])  # Speak only the first 200 characters
        save_text_to_audio(text, "output.mp3")  # Save full text to an audio file