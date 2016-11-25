"""
Usage: 
    pep8 [options] <input>...

Options:
  --version            show program's version number and exit
  -h, --help           show this help message and exit
  -v, --verbose        print status messages, or debug with -vv
  -q, --quiet          report only file names, or nothing with -qq
  -r, --repeat         (obsolete) show all occurrences of the same error
  --first              show first occurrence of each error
  --exclude=patterns   exclude files or directories which match these comma
                       separated patterns (default:
                       .svn,CVS,.bzr,.hg,.git,__pycache__,.tox)
  --filename=patterns  when parsing directories, only check filenames matching
                       these comma separated patterns (default: *.py)
  --select=errors      select errors and warnings (e.g. E,W6)
  --ignore=errors      skip errors and warnings (e.g. E4,W) (default:
                       E121,E123,E126,E226,E24,E704)
  --show-source        show source code for each error
  --show-pep8          show text of PEP 8 for each error (implies --first)
  --statistics         count errors and warnings
  --count              print total number of errors and warnings to standard
                       error and set exit code to 1 if total is not null
  --max-line-length=n  set maximum allowed line length (default: 79)
  --hang-closing       hang closing bracket instead of matching indentation of
                       opening bracket's line
  --format=format      set the error format [default|pylint|<custom>]
  --diff               report changes only within line number ranges in the
                       unified diff received on STDIN
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    print(arguments)
