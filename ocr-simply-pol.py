from PIL import Image
import pytesseract

def ocr_to_txt(image_path, output_txt):
    # Wczytaj obraz
    image = Image.open(image_path)

    # Wykonaj OCR
    text = pytesseract.image_to_string(image, lang='eng')

    # Zapisz wyniki do pliku txt
    with open(output_txt, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    # Ścieżka do pliku zeskanowanego obrazu (JPG)
    image_path = r"C:\python-files\405751406_186548954526459_7462916965637521543_n.jpg"

    # Ścieżka do pliku wynikowego txt
    output_txt = r"C:\python-files\resultocr1.txt"

    # Wywołaj funkcję OCR i zapisz wyniki do pliku txt
    ocr_to_txt(image_path, output_txt)
