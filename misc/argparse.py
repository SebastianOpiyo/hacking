import optparse
import math

'''
#|WORKING WITH optparse
#-----------------------
#|>>supported with version 2.7 and below

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()


#| WORKING WITH argparse
#----------------------
#|>>Supported as from python 2.7 onwards.

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
'''

#| Doing Maths with argparse
#----------------------------
#|>>Calculating the volume of a cylinder using radius and height.
#=================================================================
parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
parser.add_argument('-r', '--radius', type=int, help='Radius of a Cylinder')
parser.add_argument('-h', '--height', type=int, help='Height of a Cylinder')
args = parser.parse_args()

def cylinder_volume(radius, height):
    vol = (math.pi)*(radius ** 2) * (height)
    return vol

if __name__== '__main__':
    print cylinder_volume(args.radius, args.height)
