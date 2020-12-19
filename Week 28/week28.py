# python script to read pdf file

import pyttsx3, PyPDF2   # importing the necessary modules

pdfReader = PyPDF2.PdfFileReader(open('sample.pdf', 'rb')) #opening the pdf file in read mode

speaker = pyttsx3.init()    # initialising the pdf reader

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)                                          #Itirating through each word of each page
    speaker.runAndWait()
speaker.stop()
