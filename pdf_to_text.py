
import PyPDF2

def extract_text(pdf_path):
    with open(pdf_path , "rb") as f :
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages :
            text = page.extract_text() + "\n"
    print(text)
    return text

print("--- Hello Welcome to program ---")
print("\n")
file = input("enter your file name : ")
extract_text(file)