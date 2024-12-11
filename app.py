import os
from PIL import Image
import easyocr

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "1"

def image_to_text(image_path: str, reader) -> str:
    """
    Convert an image to text using OCR (Optical Character Recognition).

    :param image_path: Path to the image file.
    :param reader: EasyOCR Reader object.
    :return: Extracted text as a string.
    """
    try:
        # Read image text with the reader
        results = reader.readtext(image_path, detail=0)
        return '\n'.join(results)
    except Exception as e:
        return f"Error processing {image_path}: {str(e)}"

def process_images_in_directory(directory_path: str) -> None:
    """
    Process all images in a directory, converting them to text and saving each result to a separate .txt file.

    :param directory_path: Path to the directory containing image files.
    """
    reader = easyocr.Reader(['ch_sim', 'en'])  # Initialize EasyOCR reader with Chinese and English models
    try:
        image_files = [f for f in os.listdir(directory_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        total_files = len(image_files)
        
        for idx, filename in enumerate(image_files, start=1):
            print(f"Processing the {idx}/{total_files} file: {filename}")
            image_path = os.path.join(directory_path, filename)
            try:
                text = image_to_text(image_path, reader)
                output_file = os.path.splitext(image_path)[0] + '.txt'
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
            except PermissionError:
                print(f"Permission denied for file: {filename}. Skipping.")
            except Exception as e:
                print(f"Error processing file {filename}: {str(e)}")
        print(f"Text extracted from images and saved as .txt files in {directory_path}")
    except Exception as e:
        print(f"Error processing directory {directory_path}: {str(e)}")

def main():
    """
    Main function to run the image-to-text conversion.
    """
    directory_path = input("Enter the path to the directory containing images: ").strip()
    process_images_in_directory(directory_path)

if __name__ == "__main__":
    main()
