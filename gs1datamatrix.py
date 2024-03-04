from treepoem import generate_barcode
from PIL import Image, ImageDraw, ImageFont

class Gs1datamatix():
    def __init__(self, code, textinclude=False):
        self.gs1dm = code
        self.version = '26x26'
        self.textinclude = textinclude
        self.image = self.generate()
        
    def save(self, fileName):
        self.image.save(fileName)

    def show(self):
        self.image.show()

    def generate(self):
        # Generate datamatrix
        datamatrix = generate_barcode(
            barcode_type='datamatrix',
            data=f"^FNC1{self.gs1dm}",
            options={"parsefnc": True, "parse": True, "format": "square", "version": self.version, "includetext": self.textinclude})
        
        # Resize datamatrix to desired size
        dm_size_px = (196, 196)
        datamatrix = datamatrix.resize(dm_size_px, Image.NEAREST)

        # Create white picture  
        picture_size_px = (200, 200)
        picture = Image.new('L', picture_size_px, color='white')

        # Position the datamatrix
        barcode_position_px = (2, 2)
        picture.paste(datamatrix, barcode_position_px)

        # Draw picture for placing texts on it
        draw = ImageDraw.Draw(picture)

        # Store font for the texts
        ocrb_font = ImageFont.truetype("sources/fonts/arialnb.ttf", 12)
        # Draw texts on the Picture
        #datamatrix_text_position_px = (10,15)
        #draw.text(datamatrix_text_position_px, "This is a GS1 DataMatrix", fill='black', font=ocrb_font)
        #welcome_text_position_px = (35,180)
        #draw.text(welcome_text_position_px, gs1dm[:gs1dm.find('93')], fill='black', font=ocrb_font)

        # Save the image
        #picture.save("datamatrix.png")
        #picture.show()
        return picture
