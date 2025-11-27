#qrcode maker for tactile universe
#Cassie lakin
#26/6/2023
from PIL import Image, ImageDraw, ImageFont
import qrcode as qr
import os
import textwrap

#creates the directory for the finished images and files
os.makedirs("completed", exist_ok = True)
path = r"completed"
# opens the background image that will house the qrcode 
main_pic = Image.open("back_template_standard.png")
#font = ImageFont.truetype("WorkSans-Bold.ttf", 282)
# location of the file that the qrcode will point to (online somewhere)
web_location = ("https://tactilespace.le.ac.uk/wp-content/uploads/2023/06/")

#user inputs to create the plate locations and descriptions
plate_title = input("Please enter the plate title:")
print("Most Excellent, thank you.")
file_name = input("please enter a filename (no spaces)")
print("Thank you")
plate_file = (file_name + ".txt")
plate_description = input("Please enter a description that will be read out to the user:")
print("Thank you kindly.")
plate_description_short = input("Please enter the text for the back of the plate above the QR code.")
print("once again, many thanks")
print("Your text file and image should both be in the completed folder. Thank you for waiting. Don't have a good day, have a great day...")

textbox_title = (plate_title)
qrcode_address = (web_location + file_name + ".txt")
qrcode_image = qr.make(qrcode_address)
type(qrcode_image)
qrcode_image.save("temp.png")
qr_code = Image.open("temp.png")

with open(os.path.join(path, plate_file), "w") as file:

    file.write(plate_title)
    file.write("\n\n")
    file.write(plate_description)
    file.close()

new_image = (plate_title +".png")

#adding text to the background picture



#Calculate the center position for the existing image then centering the qr code into the image
y = int(main_pic.width / 2)
x = int(main_pic.height / 1.4)
y2 = int(qr_code.width / 2)
x2 = int(qr_code.height / 2)
y3 = int(x - x2)
x3 = int(y - y2)
main_pic.paste(qr_code, (x3, y3))
#main_pic.save(os.path.join(path, new_image))
draw = ImageDraw.Draw(main_pic)
fnt = ImageFont.truetype("timesbd.ttf", 60)
fnt2 = ImageFont.truetype("times.ttf", 50)
text_title = (plate_title)
w, h = main_pic.width/2, main_pic.height/20
draw.text((w, h), textbox_title, font=fnt, fill="black", anchor="mm")

#short description text box
text_descript = (plate_description_short)
new_text = textwrap.TextWrapper(width=60)
string = new_text.fill(text=text_descript)
draw.text((60, 150), string, font=fnt2, fill="black")
#print(new_text)
main_pic.save(os.path.join(path, new_image))


                   



