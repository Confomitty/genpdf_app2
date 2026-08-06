from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation = "P",unit = "mm",format = "A4")
pdf.set_auto_page_break(auto=False)

df = pd.read_csv("topics.csv")
for index , row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0,h=24,txt=row["Topic"])
    #pdf.line(10,28,200,28)   not required since the first line is starting from exact header! THINK

    for i in range(28,290,10):
        pdf.line(10,i,200,i)

    #Set Footer
    pdf.ln(276)
    pdf.set_text_color(180, 180, 180)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.cell(w=0,h=10,txt=row["Topic"],align="R")


    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.set_font(family="Times", style="I", size=8)

        for y in range(28, 290, 10):
            pdf.line(10, y, 200, y)

        pdf.ln(277)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")



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