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
import string
from xml.etree.ElementTree import ElementTree,Element,SubElement,Comment,tostring
from pyThaana.conversions import ThaanaConversions

SQLITE_DB = "radheef.sqlite3"
XML_OUTPUT = "output.xml"


# init the Thaana conversion library as a global object
convert = ThaanaConversions()

# init translation table for later use..not sure if we need this
# this will fix brackts in the revstring routine
tTable = string.maketrans('()[]{}',')(][}{')


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
        hitList = []                # an empty list to hold the headwords already parsed
        
        # THOUGHT: should I group by headword and concat the defs?
        # that might simplify a few things
        dbCur.execute('SELECT * FROM radheef')
        
        # start creating entries.
        for row in dbCur:
            
            headWord = row[0]                   # the headword
            headWordr = stringReverse(headWord) # safe-reversed headword
            headBas = asciiUTF(headWord)        # thaana headword
            
            
            # find out if the definition already exists
            # XPATH ".//d:entry[@id='%s']" % cleanupID(headwordR)
            # Using find on each row is going to be ridiculously slow
            # using the hitList as a temporary stepAround until a solution can be found
            
            if headWord in hitList:
                dictEntry=radheef.find(".//*[@id='%s']" % cleanupID(headWordr))
                defn=dictEntry.find("div")
                
                #debug:
                print "found %s so reusing the node" % headWord
            
            # <d:entry id="unique_id" d:title="display">
            else:
                dictEntry = SubElement(radheef,"d:entry",{'id':cleanupID(headWordr),'d:title':headBas})
                
                # we want it on the hitlist
                hitList.append(headWord)
            
                # <d:index d:value="indexVal" d:title="displayTitle" />
                # we create two here, for thaana and also, ascii search
                
                SubElement(dictEntry,"d:index",{'d:value':headWordr,'d:title':headBas})
                SubElement(dictEntry,"d:index",{'d:value':headBas,'d:title':headBas})

                # Top Level align-right container
                defn = SubElement(dictEntry,"div",{'class':'align_right'})
                SubElement(defn,"h1").text=headBas

        
                    
            defn.append(makeDef(headBas,row[1],row[2]))
            
    

    # debug
    # print tostring(radheef)
    writeToFile(radheef)

def makeDef(headBas,wordType,definition):
    em = Element("div",{'class':'definition'})

    if wordType:
        SubElement(em,"span",{'class':'word_class'}).text=asciiUTF(wordType)
    
    SubElement(em,"p").text=asciiUTF(definition)

    return em


def asciiUTF(ascString):
    # writeup some number-safe string reversal routine
    revString = stringReverse(ascString)
    return convert.ConvertAsciiToUtf8(revString)


def cleanupID(idString):
    return idString.replace(" ","_")


def stringReverse(rString):
    # TODO: make it number safe and other do-hickeys
    # re /([\d+\.,:]+)/
    
    # blind reverse and translate brackets
    rString = rString.encode('ascii')
    rev = rString[::-1].translate(tTable)
    
    #oof! reverse numbers and spit it out
    return re.sub(r"([0-9\,.:]+)",lambda m:m.group(0)[::-1],rev)


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