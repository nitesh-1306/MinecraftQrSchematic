import os
import qrcode
import mcschematic
from PIL import Image


class QrSchematic:
    def __init__(self):
        self.schem = mcschematic.MCSchematic()
        self.crop_box = (40, 40, 290, 290)
        self.qr_img = None
    
    def __save_schematic_file(self):
        self.schem.save("", "rickroll", mcschematic.Version.JE_1_20_1)
    
    def __generate_qr_code(self, url):
        self.qr_img = qrcode.make(url)
        self.qr_img = self.qr_img.crop(self.crop_box)
        self.qr_img = self.qr_img.resize((25, 25), Image.Resampling.LANCZOS)
    
    def __add_blocks_to_schema(self):
        pixels = self.qr_img.load()
        width, height = self.qr_img.size
        for x in range(width - 1, -1, -1):
            for y in range(height - 1, -1, -1):
                pixel = pixels[x, y]
                if pixel == 255:
                    self.schem.setBlock(((24-x), (24-y), 0),"minecraft:white_concrete")
                else:
                    self.schem.setBlock(((24-x), (24-y), 0),"minecraft:black_concrete")
    
    def generate_qr_structure(self, url):
        self.__generate_qr_code(url)
        self.__add_blocks_to_schema()
        self.__save_schematic_file()
        with open("rickroll.schem", "rb") as f:
            schematic_data = f.read()
        os.remove("rickroll.schem")
        return schematic_data


if __name__ == '__main__':
    qr = QrSchematic()
    url = input('Enter url to generate the qr: ')
    qr.generate_qr_structure(url)