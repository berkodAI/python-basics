# command line
# pip install cowsay

"""
import cowsay
import sys

if len(sys.argv) == 2:
    # cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])
"""

import sys

from sayings import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])
