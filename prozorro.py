import sys
import os


def main(args):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    subdirs= [x[0] for x in os.walk(os.path.dirname(os.path.abspath(__file__))) if not x[0].startswith("_") and not x[0] ]
    sys.path.extend(subdirs)
    from Prozorro import ProzorroCheck
    ProzorroCheck.check(args)

if __name__ == "__main__":
     main(sys.argv[1:])