#!/usr/bin/python

import xml.dom.minidom
import os

infile = open('AWS16509.xml', 'r')
outfile = open('paths.txt.tmp', 'w')


def parseXML():
    doc = xml.dom.minidom.parse(infile)

    destinations = doc.getElementsByTagName("rt-destination")
    aspaths = doc.getElementsByTagName("as-path")

    for dest  in destinations:
        # outfile.write(dest.childNodes[0].nodeValue)
        print >> outfile, dest.childNodes[0].nodeValue

    print "There are", destinations.length, "destinations reachable through ", aspaths.length, 'paths.'
    infile.close()
    outfile.close()


def sortanduniq():
    '''
    the first generation of this process generates an AS path graph of deduplicated
    paths from source to the specified AS.  In order to do this, the cleaned file must
    be sorted, and then run through 'uniq'
    :return:
    '''
    # is there a python way to do this?
    os.system('cat paths.txt.tmp | sort | uniq > final.txt')


def cleanup():
    # delete working temp files
    return


def main():
    parseXML()
    sortanduniq()


main()

