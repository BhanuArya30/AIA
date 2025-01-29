import os
from typing import Optional, List
import fitz  # PyMuPDF
from PIL import Image
import logging

def adjust_path_for_os(image_path):    
    if os.name == 'nt':  # Windows
        # Convert the path to use backslashes for Windows
        adjusted_path = image_path.replace('/', '\\')
    else:  # Unix-based (Linux, macOS)
        # Ensure the path uses forward slashes for Unix-based OS
        adjusted_path = image_path.replace('\\', '/')
    
    return adjusted_path


def convert_page_to_image(page, output_path: str, image_format: str = "JPEG") -> None:
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img.save(output_path, image_format)


def pdf_to_images(
    pdf_path: str, output_folder: str, image_format: str = "JPEG"
) -> List[str]:
    image_paths = []
    try:
        with fitz.open(pdf_path) as pdf_document:
            pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                image_path = os.path.join(
                    output_folder,
                    f"{pdf_name}_page_{page_num + 1}.{image_format.lower()}",
                )
                convert_page_to_image(page, image_path, image_format)
                image_paths.append(image_path)
                logging.info(f"Saved: {image_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return image_paths


# if __name__ == "__main__":
#     pdf_file_path = r"data\lloyds.pdf"  # Path to your PDF file
#     output_directory = "data"  # Folder where images will be saved
#     pdf_to_images(pdf_file_path, output_directory)