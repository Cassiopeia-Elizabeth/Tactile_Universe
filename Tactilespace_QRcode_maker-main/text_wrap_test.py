from PIL import Image, ImageDraw, ImageFont
import textwrap
text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

image = Image.open("back_template.png")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("timesbd.ttf", 50)
draw.text(textwrap.fill(text), (100, 100), font=font, fill="#aa0000")
image.save("image.jpg")