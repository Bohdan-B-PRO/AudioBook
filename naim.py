# import PyPDF2
# import pyttsx4
# from tkinter import *
# from tkinter import filedialog
#
# # Создание графического интрефейса
# root = Tk()
# root.title("")
# root.geometry("400x200")
#
# # Создание функции для открытия PDF-файла
# def open_file():
#     file = filedialog.askopenfilename(filetypes=[("PDF Files", "*pdf")])
#     return file
#
# # Создание функции для конвертирования PDF-файла в аудиофайл
# def convert_to_audio():
#     file_path = open_file()
#     pdf_file = open(file_path, 'rb')
#     read_pdf = PyPDF2.PdfFileReader(pdf_file)
#     engine = pyttsx4.init()
#     voices = engine.getProperty('voice'.id)
#     engine.setProperty('voice', voices[1].id)
#     for page in range(read_pdf.getNumPages()):
#         text = read_pdf.getPage(page).extractText()
#         engine.say(text)
#         engine.runAndWait()
#
# # Создание кнопки "Открыть файл"
# open_button = Button(root, text="Открыть файл", command=open_file)
# open_button.pack()
#
# # Создаём кнопку "Конвертировать в аудио"
# convert_button = Button(root,text="Конвектировать в аудио", command=convert_to_audio())
# convert_button.pack()
#
#



