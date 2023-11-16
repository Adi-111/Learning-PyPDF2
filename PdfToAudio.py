from PyPDF2 import PdfReader
from gtts import gTTS
import os

pdf_path = '/Users/tanishjain/Desktop/Adi/DOC/Bitcoin-satoshiNakamoto.pdf'

# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:
    # Create a PdfReader object
    pdf_reader = PdfReader(pdf_file)

    # Initialize text variable to store extracted text from all pages
    all_text = ""

    # Iterate through all pages and extract text
    for page_num in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')
        all_text += clean_text

# Using gTTS to convert text to speech
speech = gTTS(text=all_text, lang='en', slow=False)

# Save the speech to an MP3 file
mp3_path = '/Users/tanishjain/Desktop/Adi/DOC/Bitcoin-satoshiNakamoto.mp3'
speech.save(mp3_path)

# Play the MP3 file (optional)
os.system("open " + mp3_path)
