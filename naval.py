"""
Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=&ltkn&gt  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Batalla Naval 2.0')
    print(arguments)

    print "-----------------------------------"
    print "-----------------------------------"

    for name in arguments.get('<name>'):
        print "name:{}".format(name)
