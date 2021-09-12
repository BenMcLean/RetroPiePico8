# import pico8.tool
# print(pico8.tool.main(orig_args=['listlua','poom_1.7.p8.png']))
import argparse, os, lxml
from lxml.etree import ElementTree
from lxml.etree import Element
from lxml.etree import SubElement
from glob import glob
parser = argparse.ArgumentParser(description='Input XML file')
parser.add_argument('file', metavar='file', type=str, nargs='+', help='Input XML file')
filename = parser.parse_args().file[0]
path = os.path.dirname(os.path.abspath(filename))
et = ElementTree.parse(filename).getroot() if os.path.exists(filename) else ElementTree(Element('gameList'))
files = glob(os.path.join(path, '*.png')) + glob(os.path.join(path, '*.p8')) + glob(os.path.join(path, '*.p8.png'))
for file in files:
    relativeFile = os.path.join('.', os.path.basename(file))
    foundit = False
    for game in et.getroot().iter('game'):
        if (game.find('path').text == relativeFile):
            foundit = True
            break
    if (not foundit):
        game = SubElement(et.getroot(), 'game')
        gamePath = SubElement(game, 'path')
        gamePath.text = relativeFile
        gameName = SubElement(game, 'name')
        gameName.text = os.path.basename(file).removesuffix('.png').removesuffix('.p8')
        gameImage = SubElement(game, 'image')
        gameImage.text = relativeFile
lxml.etree.indent(et.getroot(), space='\t')
text_file = open(filename, 'wt')
n = text_file.write(lxml.etree.tostring(et, encoding='unicode', pretty_print=True))
text_file.close()
