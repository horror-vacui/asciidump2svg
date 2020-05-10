import argparse
import csv

def zti_dec_rgb2hex_str(red, green, blue):
    """ generate a hex string - without 0x prefix - from three colorintegers
    for red, green and blue
    """
    # return hex((red<<16) + (green<<8) + blue)[2:]
    return "%.2x%.2x%.2x" % (red, green, blue)


cds_color = {
    "green":        (0,204,102),
    "red":          (255,0,0),
    "yellow":       (255,255,0),
    "tan":          (255,230,191),
    "blue":         (0,0,255),
    "gold":         (217,204,0),
    "magenta":      (255,0,255),
    "orange":       (255,128,0),
    "lilac":        (255,180,250),
    "purple":       (153,0,230),
    "turquoise":    (43,206,231),
    "pink":         (255,191,242),
    "maroon":       (230,31,13),
    "lightBlue":    (51,179,255),
    "violet":       (94,0,230),
    "white":        (240,240,240), # little cheating to increase contrast on white background
        }

def zti_color(color_key):
    r,g,b = cds_color.get(color_key)
    return zti_dec_rgb2hex_str(red=r, green=g, blue=b)


parser = argparse.ArgumentParser(description=""" change any string found in the input, which is also in the keys of cds_colos to its hex counterpart """)
parser.add_argument("-i", help="input file", type=str)
parser.add_argument("-o", help="output file", type=str)
args = parser.parse_args()

with open(args.i,'r') as f:
    # reader = csv.DictReader(techfile)
    r_in = csv.reader(f)
    with open(args.o,'w') as fo: 
        r_out = csv.writer(fo)
        for row in r_in:
            r_out.writerow([zti_color(x) if x in cds_color.keys() else x for x in row ])

