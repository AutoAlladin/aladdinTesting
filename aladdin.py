import sys
import os


def mn(args):
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    subdirs= [x[0] for x in os.walk(os.path.dirname(os.path.abspath(__file__)))
                   if not x[0].startswith("_")
                        and not x[0].startswith(".")
                        and x[0].find(".git")==-1
              ]
    sys.path.extend(subdirs)
    from OnPublish import tests
    tests.runner(args)


if __name__ == "__main__":
     mn(sys.argv[1:])

