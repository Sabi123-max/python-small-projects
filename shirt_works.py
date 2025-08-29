from fpdf import FPDF, XPos,YPos,Align
from PIL import Image

pdf = FPDF(orientation='portrait')
pdf.add_page(format='A4')
name = input("What is your name? ").capitalize()
pdf.set_font('helvetica', size=40)
pdf.cell(90, 30, "CS50 Shirtificate", center=True,align="C")
pdf.image("shirtificate.png", x=0,y=50)
pdf.set_text_color(255,255,255)
pdf.cell(0,230,f"{name} took CS50",align="C",center=True)
# img = Image.open("shirtificate.png")
# # img = img.resize((400,400))
# pdf.image(img, x=28, y=60)
# # pdf.cell(text="hello bro")
pdf.output("shirt.pdf")