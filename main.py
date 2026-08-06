from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation = "P",unit = "mm",format = "A4")

df = pd.read_csv("topics.csv")
for index , row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0,h=24,txt=row["Topic"])
    pdf.line(10,28,200,28)

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)

pdf.output("output.pdf")





"""
total_pages = 0

with open("topics.csv","r") as myfile :
    topreader = csv.reader(myfile)
    next(myfile)
    for i in topreader:
        if int(i[2]) > 1 :
            count = 0
            while count != int(i[2]):
                pdf.add_page()
                pdf.cell(w=0,h=0,txt=i[1],border=0,ln=0,align="L")
                pdf.header(i )
                count+=1
        else :
            pdf.add_page()
            pdf.cell(w=0, h=0, txt=i[1], border=0, ln=0, align="L")


pdf.output("output.pdf")

"""

"""
pdf.cell(w=0,h=24,txt="Hello there!",align="L",
         ln=1,border=1)

pdf.set_font(family = "Times", size = 12)
pdf.cell(w=0,h=24,txt="Time to work!",align="L",
         ln=1,border=1)

pdf.add_page()
pdf.set_font(family = "Times", style ="B", size = 24)
pdf.cell(w=0,h=24,txt="Hello there!",align="L",
         ln=1,)
pdf.set_font(family = "Times", size = 12)
pdf.cell(w=0,h=24,txt="Time to work!",align="L",
         ln=1)



pdf.output("output.pdf")
"""