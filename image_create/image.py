from email.policy import default

from PIL import Image,ImageOps
import os
import PIL
ls=[]
import sys
try:
    if len(sys.argv) == 3:
        la = os.path.splitext(sys.argv[1])[1]
        lb = os.path.splitext(sys.argv[2])[1]
        if la == lb:
            imag = Image.open(sys.argv[1])
            shirt = Image.open("myshirt.png")
            size = shirt.size
            new = ImageOps.fit(imag, size)
            sad = ImageOps.fit(shirt, size)

            new.paste(shirt, shirt)
            new.save(sys.argv[2])
        else:
            sys.exit("Input and Output has different extensions")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Ivalid input")
except FileNotFoundError:
    sys.exit(f"file could not be found")




    # with Image.open("myshirt.png")as imga:
        # new.paste(imga,imga)
        # new.show()
