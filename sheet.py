from argparse import ArgumentParser
from os import system

def get_args():
    parser = ArgumentParser(prog="sheet")

    parser.add_argument("-o", "--output",
        help="Name of file to output to (including extension)")
    parser.add_argument("--background", default="none",
        help="Background color (default none)")
    parser.add_argument("--font", default="Nimbus-Mono",
        help="Font (default Nimbus-Mono)")
    parser.add_argument("--font-color", default="black",
        help="Font color (default black)")
    parser.add_argument("--point-size", default=72,
        help="Text point size (default 72)")

    return parser.parse_args()


alphabet = r"""ABCDEFGHIJKLM
NOPQRSTUVWXYZ
abcdefghijklm
nopqrstuvwxyz
0123456789,.?"""


def main():
    args = get_args()

    command = r"""
        convert -background {background} -fill  {font_color} -font {font} \
                -pointsize  {point_size} label:{alphabet}    \
                {output}
        """.format(alphabet=repr(alphabet), **vars(args))
    system(command)

#    image_info = system("identify {output}".format(output=args.output))
#    print(image_info)

    return 0

if __name__ == "__main__":
    exit(main())
