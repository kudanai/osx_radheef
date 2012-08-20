# -*- encoding: utf-8 -*-
#---------------------------------------------------------------------
#    Thaana Conversions library,
#    provides methods to convert between various representations of 
#    thaana text. This is a port of the original PHP class by
#    Jawish Hameed (http://jawish.org)
#    
#    Currently Provides the following methods.
#        ConvertAsciiToUtf8()
#        ConvertUtf8ToUnicode()
#    
#    
#    Written by Naail Abdul Rahaman (http://kudanai.com)
#    
#    Version: 0.1a
#    Updated: 2011/12/11
#
#-----------------------------------------------------------------------


from mappings import *

class ThaanaConversions():
    """
        A Thaana Conversions class, defines methods to convert between different
        representations of thaana. use with caution.
    """
        
    def ConvertAsciiToUtf8(self,text):
        """
            Converts Ascii thaana (left to right) to Utf8.
            
            accepts byte-string returns unicode-string
        """
        spam = u""
        for c in text:
            spam += unichr(AsciiToUnicode[c]) if c in AsciiToUnicode else c

        return spam
        
    
    def ConvertUtf8ToAscii(self,text):
        """
            converts a unicode string to the ascii equivalent 
            returns non-reversed representation.
            
            accepts byte-string or unicode-string. returns byte-string
        """
        spam=""
    
        if type(text) is str:               # are we dealing with a byte string or unicode?
            text = text.decode('utf-8')     # make sure it's unicode
            
        for c in text:
            spam += UnicodeToAscii[ord(c)] if ord(c) in UnicodeToAscii else c
                
        return spam
        
        
    def test(self):
        """
            debut:small test function to run through the routines.
        """
        print self.ConvertAsciiToUtf8('divehi bwsc aWlWkurumwkI fwsEhwkwmeactOaeve?')
        print self.ConvertUtf8ToAscii(u"ދިވެހިބަސް‮ ‬އާލާކުރުން‮ ‬މީ‮ ‬ފަސޭހަކަމެއްތަ؟")        # unicode string
        print self.ConvertUtf8ToAscii("ދިވެހިބަސް‮ ‬އާލާކުރުން‮ ‬މީ‮ ‬ފަސޭހަކަމެއްތަ؟")         # regular bytestring
        