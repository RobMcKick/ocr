from PIL import Image
import pytesseract

def ocr_to_txt(image_path, output_txt):
    # Wczytaj obraz
    image = Image.open(image_path)

    # Wykonaj OCR
    text = pytesseract.image_to_string(image, lang='pol')

    # Zapisz wyniki do pliku txt
    with open(output_txt, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    # Ścieżka do pliku zeskanowanego obrazu (JPG)
    image_path = r"C:\python-files\Screenshot_2.png" 

    # Ścieżka do pliku wynikowego txt
    output_txt = r"C:\python-files\result_ocr.txt"

    # Wywołaj funkcję OCR i zapisz wyniki do pliku txt
    ocr_to_txt(image_path, output_txt)
