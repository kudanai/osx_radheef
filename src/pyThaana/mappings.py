# -*- encoding: utf-8 -*-

# a mapping of ascii character to the unicode integer value
# of the corrosponding thaana character as on the Phonetic keyboard layout
AsciiToUnicode =    { 'h' : 1920, 'S' : 1921, 'n' : 1922, 'r' : 1923, 
                      'b' : 1924, 'L' : 1925, 'k' : 1926, 'a' : 1927, 
                      'v' : 1928, 'm' : 1929, 'f' : 1930, 'd' : 1931, 
                      't' : 1932, 'l' : 1933, 'g' : 1934, 'N' : 1935, 
                      's' : 1936, 'D' : 1937, 'z' : 1938, 'T' : 1939, 
                      'y' : 1940, 'p' : 1941, 'j' : 1942, 'C' : 1943, 
                      'X' : 1944, 'H' : 1945, 'K' : 1946, 'J' : 1947, 
                      'R' : 1948, 'x' : 1949, 'B' : 1950, 'F' : 1951, 
                      'Y' : 1952, 'Z' : 1953, 'A' : 1954, 'G' : 1955, 
                      'q' : 1956, 'V' : 1957, 'w' : 1958, 'W' : 1959, 
                      'i' : 1960, 'I' : 1961, 'u' : 1962, 'U' : 1963, 
                      'e' : 1964, 'E' : 1965, 'o' : 1966, 'O' : 1967, 
                      'c' : 1968, ',' : 1548, ';' : 1563, '?' : 1567, 
                      ')' : 41, '(' : 40, 'Q' : 65010 }


# generated using dict(zip(AsciiToUnicodePhonetic.value(),AsciiToUnicodePhonetic.keys()))
UnicodeToAscii =    { 1920: 'h', 1921: 'S', 1922: 'n', 1923: 'r', 
                      1924: 'b', 1925: 'L', 1926: 'k', 1927: 'a', 
                      1928: 'v', 1929: 'm', 1930: 'f', 1931: 'd', 
                      1548: ',', 1933: 'l', 1934: 'g', 1935: 'N', 
                      1936: 's', 1937: 'D', 1938: 'z', 1939: 'T', 
                      1940: 'y', 1941: 'p', 1942: 'j', 1943: 'C', 
                      1944: 'X', 1945: 'H', 1946: 'K', 1947: 'J', 
                      1948: 'R', 1949: 'x', 1950: 'B', 1951: 'F', 
                      1956: 'q', 1957: 'V', 1958: 'w', 1959: 'W', 
                      1960: 'i', 1961: 'I', 1962: 'u', 1963: 'U', 
                      1964: 'e', 1965: 'E', 1966: 'o', 1967: 'O', 
                      1968: 'c', 1567: '?', 1952: 'Y', 41: ')', 
                      1932: 't', 1955: 'G', 65010:'Q', 40: '(', 
                      1953: 'Z', 1954: 'A', 1563: ';' }



keymapPhoneticLow = [['q','w','e','r','t','y','u','i','o','p'],
                     ['a','s','d','f','g','h','j','k','l'],
                     ['z','x','c','v','b','n','m']
                    ]

keymapPhoneticHigh =[['q','w','e','r','t','y','u','i','o','p'],
                     ['a','s','d','f','g','h','j','k','l'],
                     ['z','x','c','v','b','n','m']
                    ]