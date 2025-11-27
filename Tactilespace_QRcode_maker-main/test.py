from PIL import ImageFont, ImageDraw, Image
image = Image.open("back_template.png")
draw = ImageDraw.Draw(image)

fnt = ImageFont.truetype("comicbd.ttf", 25)
draw.text((60, 60), "hello there", font=fnt, fill="black")
image.save("bb.png")
