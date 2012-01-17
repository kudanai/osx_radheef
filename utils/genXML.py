#!/usr/bin/env python

#######################################################
#
# This script will generate the required radheef XML
# file from the sqlite library.
#
# this version is meant to replace the 
# initial php version.
#
# 2012 kudanai (http://kudanai.com)
#
#######################################################

import sqlite3
import re
from xml.etree.ElementTree import ElementTree,Element,SubElement,Comment,tostring
from pyThaana.conversions import ThaanaConversions

SQLITE_DB = "radheef.sqlite3"
XML_OUTPUT = "output.xml"


# init the Thaana conversion library as a global object
convert = ThaanaConversions()


def main():

    
    # create the top-level dictionary Element
    # dictionary defs need to be valid xhtml
    # and the overall document conform to apples relaxNG schema
    # THOUGHT: should we be using TreeBuilder instead?
    radheef = Element("d:dictionary", 
                      { 'xmlns':'http://www.w3.org/1999/xhtml',
                        'xmlns:d':'http://www.apple.com/DTDs/DictionaryService-1.0.rng'
                      })
    
    # import a disclaimer or something TODO: uncomment if needed
    #radheef.append(Comment("Lorem Ipsum Dolor Sit Amet"))
    
    
    # connect to the database
    with sqlite3.connect(SQLITE_DB) as dbConn:
        dbCur = dbConn.cursor()
        
        # THOUGHT: should I group by headword and concat the defs?
        # that might simplify a few things
        dbCur.execute('SELECT * FROM radheef LIMIT 20')
        
        # start creating entries.
        # REF etree XPath: root.findall("//target[@name='a']"):
        for row in dbCur:
            
            headWord = row[0]                   # the headword
            headWordr = stringReverse(headWord) # safe-reversed headword
            headBas = asciiUTF(headWord)        # thaana headword
            
            
            # <d:entry id="unique_id" d:title="display">
            dictEntry = SubElement(radheef,"d:entry",{'id':cleanupID(headWordr),'d:title':headBas})
            
            # <d:index d:value="indexVal" d:title="displayTitle" />
            # we create two here, for thaana and also, ascii search
              
              # entry one: TODO safe string reverse d:value
            SubElement(dictEntry,"d:index",{'d:value':headWordr,'d:title':headBas})
    
              # entry two: thaana thaana
            SubElement(dictEntry,"d:index",{'d:value':headBas,'d:title':headBas})

    
    print tostring(radheef)
    writeToFile(radheef)


def asciiUTF(ascString):
    # writeup some number-safe string reversal routine
    revString = stringReverse(ascString)
    return convert.ConvertAsciiToUtf8(revString)


def cleanupID(idString):
    return idString.replace(" ","_")


def stringReverse(rString):
    # TODO: make it number safe and other do-hickeys
    return rString[::-1]


def writeToFile(rootElement):
    """
        write out the generated XML tree to file
        @params: (Element) rootElement
    """
    
    ET = ElementTree(rootElement)
    
    # what the hell happened to the prettyprint?
    # screw it, we'll just run `xmllint --format` on the output afterwards
    # gotta validate it anyway
    
    with open(XML_OUTPUT,"wb") as output:
        
        # note, this will escape the thaana to entities. this won't affect
        # performance, but it's a bitch to read
        ET.write(output,xml_declaration=True,method='xml',encoding='UTF-8')



if __name__ == "__main__":
    main()