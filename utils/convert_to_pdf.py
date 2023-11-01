import io
import img2pdf
from aiogram.types import InputFile
from loader import bot
from PIL import Image
from fpdf import FPDF


# Bu funksiya rasmni PDF-ga o'tkazadi
def convert_image_to_pdf(image_path, output_pdf_path):
    image = Image.open(image_path)
    pdf = FPDF()
    pdf.add_page()
    pdf.image(image_path, 0, 0)
    pdf.output(output_pdf_path)