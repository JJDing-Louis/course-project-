""" Python Character Mapping Codec generated from 'VENDORS/MICSFT/PC/CP855.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):
        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):
        return codecs.charmap_decode(input,errors,decoding_table)

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input,self.errors,encoding_map)[0]

class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():
    return codecs.CodecInfo(
        name='cp855',
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )

### Decoding Map

decoding_map = codecs
decoding_map.update({
    0x0080: 0x0452,     #  CYRILLIC SMALL LETTER DJE
    0x0081: 0x0402,     #  CYRILLIC CAPITAL LETTER DJE
    0x0082: 0x0453,     #  CYRILLIC SMALL LETTER GJE
    0x0083: 0x0403,     #  CYRILLIC CAPITAL LETTER GJE
    0x0084: 0x0451,     #  CYRILLIC SMALL LETTER IO
    0x0085: 0x0401,     #  CYRILLIC CAPITAL LETTER IO
    0x0086: 0x0454,     #  CYRILLIC SMALL LETTER UKRAINIAN IE
    0x0087: 0x0404,     #  CYRILLIC CAPITAL LETTER UKRAINIAN IE
    0x0088: 0x0455,     #  CYRILLIC SMALL LETTER DZE
    0x0089: 0x0405,     #  CYRILLIC CAPITAL LETTER DZE
    0x008a: 0x0456,     #  CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    0x008b: 0x0406,     #  CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    0x008c: 0x0457,     #  CYRILLIC SMALL LETTER YI
    0x008d: 0x0407,     #  CYRILLIC CAPITAL LETTER YI
    0x008e: 0x0458,     #  CYRILLIC SMALL LETTER JE
    0x008f: 0x0408,     #  CYRILLIC CAPITAL LETTER JE
    0x0090: 0x0459,     #  CYRILLIC SMALL LETTER LJE
    0x0091: 0x0409,     #  CYRILLIC CAPITAL LETTER LJE
    0x0092: 0x045a,     #  CYRILLIC SMALL LETTER NJE
    0x0093: 0x040a,     #  CYRILLIC CAPITAL LETTER NJE
    0x0094: 0x045b,     #  CYRILLIC SMALL LETTER TSHE
    0x0095: 0x040b,     #  CYRILLIC CAPITAL LETTER TSHE
    0x0096: 0x045c,     #  CYRILLIC SMALL LETTER KJE
    0x0097: 0x040c,     #  CYRILLIC CAPITAL LETTER KJE
    0x0098: 0x045e,     #  CYRILLIC SMALL LETTER SHORT U
    0x0099: 0x040e,     #  CYRILLIC CAPITAL LETTER SHORT U
    0x009a: 0x045f,     #  CYRILLIC SMALL LETTER DZHE
    0x009b: 0x040f,     #  CYRILLIC CAPITAL LETTER DZHE
    0x009c: 0x044e,     #  CYRILLIC SMALL LETTER YU
    0x009d: 0x042e,     #  CYRILLIC CAPITAL LETTER YU
    0x009e: 0x044a,     #  CYRILLIC SMALL LETTER HARD SIGN
    0x009f: 0x042a,     #  CYRILLIC CAPITAL LETTER HARD SIGN
    0x00a0: 0x0430,     #  CYRILLIC SMALL LETTER A
    0x00a1: 0x0410,     #  CYRILLIC CAPITAL LETTER A
    0x00a2: 0x0431,     #  CYRILLIC SMALL LETTER BE
    0x00a3: 0x0411,     #  CYRILLIC CAPITAL LETTER BE
    0x00a4: 0x0446,     #  CYRILLIC SMALL LETTER TSE
    0x00a5: 0x0426,     #  CYRILLIC CAPITAL LETTER TSE
    0x00a6: 0x0434,     #  CYRILLIC SMALL LETTER DE
    0x00a7: 0x0414,     #  CYRILLIC CAPITAL LETTER DE
    0x00a8: 0x0435,     #  CYRILLIC SMALL LETTER IE
    0x00a9: 0x0415,     #  CYRILLIC CAPITAL LETTER IE
    0x00aa: 0x0444,     #  CYRILLIC SMALL LETTER EF
    0x00ab: 0x0424,     #  CYRILLIC CAPITAL LETTER EF
    0x00ac: 0x0433,     #  CYRILLIC SMALL LETTER GHE
    0x00ad: 0x0413,     #  CYRILLIC CAPITAL LETTER GHE
    0x00ae: 0x00ab,     #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00af: 0x00bb,     #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00b0: 0x2591,     #  LIGHT SHADE
    0x00b1: 0x2592,     #  MEDIUM SHADE
    0x00b2: 0x2593,     #  DARK SHADE
    0x00b3: 0x2502,     #  BOX DRAWINGS LIGHT VERTICAL
    0x00b4: 0x2524,     #  BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x00b5: 0x0445,     #  CYRILLIC SMALL LETTER HA
    0x00b6: 0x0425,     #  CYRILLIC CAPITAL LETTER HA
    0x00b7: 0x0438,     #  CYRILLIC SMALL LETTER I
    0x00b8: 0x0418,     #  CYRILLIC CAPITAL LETTER I
    0x00b9: 0x2563,     #  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0x00ba: 0x2551,     #  BOX DRAWINGS DOUBLE VERTICAL
    0x00bb: 0x2557,     #  BOX DRAWINGS DOUBLE DOWN AND LEFT
    0x00bc: 0x255d,     #  BOX DRAWINGS DOUBLE UP AND LEFT
    0x00bd: 0x0439,     #  CYRILLIC SMALL LETTER SHORT I
    0x00be: 0x0419,     #  CYRILLIC CAPITAL LETTER SHORT I
    0x00bf: 0x2510,     #  BOX DRAWINGS LIGHT DOWN AND LEFT
    0x00c0: 0x2514,     #  BOX DRAWINGS LIGHT UP AND RIGHT
    0x00c1: 0x2534,     #  BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x00c2: 0x252c,     #  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x00c3: 0x251c,     #  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x00c4: 0x2500,     #  BOX DRAWINGS LIGHT HORIZONTAL
    0x00c5: 0x253c,     #  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x00c6: 0x043a,     #  CYRILLIC SMALL LETTER KA
    0x00c7: 0x041a,     #  CYRILLIC CAPITAL LETTER KA
    0x00c8: 0x255a,     #  BOX DRAWINGS DOUBLE UP AND RIGHT
    0x00c9: 0x2554,     #  BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0x00ca: 0x2569,     #  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0x00cb: 0x2566,     #  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0x00cc: 0x2560,     #  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0x00cd: 0x2550,     #  BOX DRAWINGS DOUBLE HORIZONTAL
    0x00ce: 0x256c,     #  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0x00cf: 0x00a4,     #  CURRENCY SIGN
    0x00d0: 0x043b,     #  CYRILLIC SMALL LETTER EL
    0x00d1: 0x041b,     #  CYRILLIC CAPITAL LETTER EL
    0x00d2: 0x043c,     #  CYRILLIC SMALL LETTER EM
    0x00d3: 0x041c,     #  CYRILLIC CAPITAL LETTER EM
    0x00d4: 0x043d,     #  CYRILLIC SMALL LETTER EN
    0x00d5: 0x041d,     #  CYRILLIC CAPITAL LETTER EN
    0x00d6: 0x043e,     #  CYRILLIC SMALL LETTER O
    0x00d7: 0x041e,     #  CYRILLIC CAPITAL LETTER O
    0x00d8: 0x043f,     #  CYRILLIC SMALL LETTER PE
    0x00d9: 0x2518,     #  BOX DRAWINGS LIGHT UP AND LEFT
    0x00da: 0x250c,     #  BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x00db: 0x2588,     #  FULL BLOCK
    0x00dc: 0x2584,     #  LOWER HALF BLOCK
    0x00dd: 0x041f,     #  CYRILLIC CAPITAL LETTER PE
    0x00de: 0x044f,     #  CYRILLIC SMALL LETTER YA
    0x00df: 0x2580,     #  UPPER HALF BLOCK
    0x00e0: 0x042f,     #  CYRILLIC CAPITAL LETTER YA
    0x00e1: 0x0440,     #  CYRILLIC SMALL LETTER ER
    0x00e2: 0x0420,     #  CYRILLIC CAPITAL LETTER ER
    0x00e3: 0x0441,     #  CYRILLIC SMALL LETTER ES
    0x00e4: 0x0421,     #  CYRILLIC CAPITAL LETTER ES
    0x00e5: 0x0442,     #  CYRILLIC SMALL LETTER TE
    0x00e6: 0x0422,     #  CYRILLIC CAPITAL LETTER TE
    0x00e7: 0x0443,     #  CYRILLIC SMALL LETTER U
    0x00e8: 0x0423,     #  CYRILLIC CAPITAL LETTER U
    0x00e9: 0x0436,     #  CYRILLIC SMALL LETTER ZHE
    0x00ea: 0x0416,     #  CYRILLIC CAPITAL LETTER ZHE
    0x00eb: 0x0432,     #  CYRILLIC SMALL LETTER VE
    0x00ec: 0x0412,     #  CYRILLIC CAPITAL LETTER VE
    0x00ed: 0x044c,     #  CYRILLIC SMALL LETTER SOFT SIGN
    0x00ee: 0x042c,     #  CYRILLIC CAPITAL LETTER SOFT SIGN
    0x00ef: 0x2116,     #  NUMERO SIGN
    0x00f0: 0x00ad,     #  SOFT HYPHEN
    0x00f1: 0x044b,     #  CYRILLIC SMALL LETTER YERU
    0x00f2: 0x042b,     #  CYRILLIC CAPITAL LETTER YERU
    0x00f3: 0x0437,     #  CYRILLIC SMALL LETTER ZE
    0x00f4: 0x0417,     #  CYRILLIC CAPITAL LETTER ZE
    0x00f5: 0x0448,     #  CYRILLIC SMALL LETTER SHA
    0x00f6: 0x0428,     #  CYRILLIC CAPITAL LETTER SHA
    0x00f7: 0x044d,     #  CYRILLIC SMALL LETTER E
    0x00f8: 0x042d,     #  CYRILLIC CAPITAL LETTER E
    0x00f9: 0x0449,     #  CYRILLIC SMALL LETTER SHCHA
    0x00fa: 0x0429,     #  CYRILLIC CAPITAL LETTER SHCHA
    0x00fb: 0x0447,     #  CYRILLIC SMALL LETTER CHE
    0x00fc: 0x0427,     #  CYRILLIC CAPITAL LETTER CHE
    0x00fd: 0x00a7,     #  SECTION SIGN
    0x00fe: 0x25a0,     #  BLACK SQUARE
    0x00ff: 0x00a0,     #  NO-BREAK SPACE
})

### Decoding Table

decoding_table = (
    '\x00'     #  0x0000 -> NULL
    '\x01'     #  0x0001 -> START OF HEADING
    '\x02'     #  0x0002 -> START OF TEXT
    '\x03'     #  0x0003 -> END OF TEXT
    '\x04'     #  0x0004 -> END OF TRANSMISSION
    '\x05'     #  0x0005 -> ENQUIRY
    '\x06'     #  0x0006 -> ACKNOWLEDGE
    '\x07'     #  0x0007 -> BELL
    '\x08'     #  0x0008 -> BACKSPACE
    '\t'       #  0x0009 -> HORIZONTAL TABULATION
    '\n'       #  0x000a -> LINE FEED
    '\x0b'     #  0x000b -> VERTICAL TABULATION
    '\x0c'     #  0x000c -> FORM FEED
    '\r'       #  0x000d -> CARRIAGE RETURN
    '\x0e'     #  0x000e -> SHIFT OUT
    '\x0f'     #  0x000f -> SHIFT IN
    '\x10'     #  0x0010 -> DATA LINK ESCAPE
    '\x11'     #  0x0011 -> DEVICE CONTROL ONE
    '\x12'     #  0x0012 -> DEVICE CONTROL TWO
    '\x13'     #  0x0013 -> DEVICE CONTROL THREE
    '\x14'     #  0x0014 -> DEVICE CONTROL FOUR
    '\x15'     #  0x0015 -> NEGATIVE ACKNOWLEDGE
    '\x16'     #  0x0016 -> SYNCHRONOUS IDLE
    '\x17'     #  0x0017 -> END OF TRANSMISSION BLOCK
    '\x18'     #  0x0018 -> CANCEL
    '\x19'     #  0x0019 -> END OF MEDIUM
    '\x1a'     #  0x001a -> SUBSTITUTE
    '\x1b'     #  0x001b -> ESCAPE
    '\x1c'     #  0x001c -> FILE SEPARATOR
    '\x1d'     #  0x001d -> GROUP SEPARATOR
    '\x1e'     #  0x001e -> RECORD SEPARATOR
    '\x1f'     #  0x001f -> UNIT SEPARATOR
    ' '        #  0x0020 -> SPACE
    '!'        #  0x0021 -> EXCLAMATION MARK
    '"'        #  0x0022 -> QUOTATION MARK
    '#'        #  0x0023 -> NUMBER SIGN
    '$'        #  0x0024 -> DOLLAR SIGN
    '%'        #  0x0025 -> PERCENT SIGN
    '&'        #  0x0026 -> AMPERSAND
    "'"        #  0x0027 -> APOSTROPHE
    '('        #  0x0028 -> LEFT PARENTHESIS
    ')'        #  0x0029 -> RIGHT PARENTHESIS
    '*'        #  0x002a -> ASTERISK
    '+'        #  0x002b -> PLUS SIGN
    ','        #  0x002c -> COMMA
    '-'        #  0x002d -> HYPHEN-MINUS
    '.'        #  0x002e -> FULL STOP
    '/'        #  0x002f -> SOLIDUS
    '0'        #  0x0030 -> DIGIT ZERO
    '1'        #  0x0031 -> DIGIT ONE
    '2'        #  0x0032 -> DIGIT TWO
    '3'        #  0x0033 -> DIGIT THREE
    '4'        #  0x0034 -> DIGIT FOUR
    '5'        #  0x0035 -> DIGIT FIVE
    '6'        #  0x0036 -> DIGIT SIX
    '7'        #  0x0037 -> DIGIT SEVEN
    '8'        #  0x0038 -> DIGIT EIGHT
    '9'        #  0x0039 -> DIGIT NINE
    ':'        #  0x003a -> COLON
    ';'        #  0x003b -> SEMICOLON
    '<'        #  0x003c -> LESS-THAN SIGN
    '='        #  0x003d -> EQUALS SIGN
    '>'        #  0x003e -> GREATER-THAN SIGN
    '?'        #  0x003f -> QUESTION MARK
    '@'        #  0x0040 -> COMMERCIAL AT
    'A'        #  0x0041 -> LATIN CAPITAL LETTER A
    'B'        #  0x0042 -> LATIN CAPITAL LETTER B
    'C'        #  0x0043 -> LATIN CAPITAL LETTER C
    'D'        #  0x0044 -> LATIN CAPITAL LETTER D
    'E'        #  0x0045 -> LATIN CAPITAL LETTER E
    'F'        #  0x0046 -> LATIN CAPITAL LETTER F
    'G'        #  0x0047 -> LATIN CAPITAL LETTER G
    'H'        #  0x0048 -> LATIN CAPITAL LETTER H
    'I'        #  0x0049 -> LATIN CAPITAL LETTER I
    'J'        #  0x004a -> LATIN CAPITAL LETTER J
    'K'        #  0x004b -> LATIN CAPITAL LETTER K
    'L'        #  0x004c -> LATIN CAPITAL LETTER L
    'M'        #  0x004d -> LATIN CAPITAL LETTER M
    'N'        #  0x004e -> LATIN CAPITAL LETTER N
    'O'        #  0x004f -> LATIN CAPITAL LETTER O
    'P'        #  0x0050 -> LATIN CAPITAL LETTER P
    'Q'        #  0x0051 -> LATIN CAPITAL LETTER Q
    'R'        #  0x0052 -> LATIN CAPITAL LETTER R
    'S'        #  0x0053 -> LATIN CAPITAL LETTER S
    'T'        #  0x0054 -> LATIN CAPITAL LETTER T
    'U'        #  0x0055 -> LATIN CAPITAL LETTER U
    'V'        #  0x0056 -> LATIN CAPITAL LETTER V
    'W'        #  0x0057 -> LATIN CAPITAL LETTER W
    'X'        #  0x0058 -> LATIN CAPITAL LETTER X
    'Y'        #  0x0059 -> LATIN CAPITAL LETTER Y
    'Z'        #  0x005a -> LATIN CAPITAL LETTER Z
    '['        #  0x005b -> LEFT SQUARE BRACKET
    '\\'       #  0x005c -> REVERSE SOLIDUS
    ']'        #  0x005d -> RIGHT SQUARE BRACKET
    '^'        #  0x005e -> CIRCUMFLEX ACCENT
    '_'        #  0x005f -> LOW LINE
    '`'        #  0x0060 -> GRAVE ACCENT
    'a'        #  0x0061 -> LATIN SMALL LETTER A
    'b'        #  0x0062 -> LATIN SMALL LETTER B
    'c'        #  0x0063 -> LATIN SMALL LETTER C
    'd'        #  0x0064 -> LATIN SMALL LETTER D
    'e'        #  0x0065 -> LATIN SMALL LETTER E
    'f'        #  0x0066 -> LATIN SMALL LETTER F
    'g'        #  0x0067 -> LATIN SMALL LETTER G
    'h'        #  0x0068 -> LATIN SMALL LETTER H
    'i'        #  0x0069 -> LATIN SMALL LETTER I
    'j'        #  0x006a -> LATIN SMALL LETTER J
    'k'        #  0x006b -> LATIN SMALL LETTER K
    'l'        #  0x006c -> LATIN SMALL LETTER L
    'm'        #  0x006d -> LATIN SMALL LETTER M
    'n'        #  0x006e -> LATIN SMALL LETTER N
    'o'        #  0x006f -> LATIN SMALL LETTER O
    'p'        #  0x0070 -> LATIN SMALL LETTER P
    'q'        #  0x0071 -> LATIN SMALL LETTER Q
    'r'        #  0x0072 -> LATIN SMALL LETTER R
    's'        #  0x0073 -> LATIN SMALL LETTER S
    't'        #  0x0074 -> LATIN SMALL LETTER T
    'u'        #  0x0075 -> LATIN SMALL LETTER U
    'v'        #  0x0076 -> LATIN SMALL LETTER V
    'w'        #  0x0077 -> LATIN SMALL LETTER W
    'x'        #  0x0078 -> LATIN SMALL LETTER X
    'y'        #  0x0079 -> LATIN SMALL LETTER Y
    'z'        #  0x007a -> LATIN SMALL LETTER Z
    '{'        #  0x007b -> LEFT CURLY BRACKET
    '|'        #  0x007c -> VERTICAL LINE
    '}'        #  0x007d -> RIGHT CURLY BRACKET
    '~'        #  0x007e -> TILDE
    '\x7f'     #  0x007f -> DELETE
    '\u0452'   #  0x0080 -> CYRILLIC SMALL LETTER DJE
    '\u0402'   #  0x0081 -> CYRILLIC CAPITAL LETTER DJE
    '\u0453'   #  0x0082 -> CYRILLIC SMALL LETTER GJE
    '\u0403'   #  0x0083 -> CYRILLIC CAPITAL LETTER GJE
    '\u0451'   #  0x0084 -> CYRILLIC SMALL LETTER IO
    '\u0401'   #  0x0085 -> CYRILLIC CAPITAL LETTER IO
    '\u0454'   #  0x0086 -> CYRILLIC SMALL LETTER UKRAINIAN IE
    '\u0404'   #  0x0087 -> CYRILLIC CAPITAL LETTER UKRAINIAN IE
    '\u0455'   #  0x0088 -> CYRILLIC SMALL LETTER DZE
    '\u0405'   #  0x0089 -> CYRILLIC CAPITAL LETTER DZE
    '\u0456'   #  0x008a -> CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    '\u0406'   #  0x008b -> CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    '\u0457'   #  0x008c -> CYRILLIC SMALL LETTER YI
    '\u0407'   #  0x008d -> CYRILLIC CAPITAL LETTER YI
    '\u0458'   #  0x008e -> CYRILLIC SMALL LETTER JE
    '\u0408'   #  0x008f -> CYRILLIC CAPITAL LETTER JE
    '\u0459'   #  0x0090 -> CYRILLIC SMALL LETTER LJE
    '\u0409'   #  0x0091 -> CYRILLIC CAPITAL LETTER LJE
    '\u045a'   #  0x0092 -> CYRILLIC SMALL LETTER NJE
    '\u040a'   #  0x0093 -> CYRILLIC CAPITAL LETTER NJE
    '\u045b'   #  0x0094 -> CYRILLIC SMALL LETTER TSHE
    '\u040b'   #  0x0095 -> CYRILLIC CAPITAL LETTER TSHE
    '\u045c'   #  0x0096 -> CYRILLIC SMALL LETTER KJE
    '\u040c'   #  0x0097 -> CYRILLIC CAPITAL LETTER KJE
    '\u045e'   #  0x0098 -> CYRILLIC SMALL LETTER SHORT U
    '\u040e'   #  0x0099 -> CYRILLIC CAPITAL LETTER SHORT U
    '\u045f'   #  0x009a -> CYRILLIC SMALL LETTER DZHE
    '\u040f'   #  0x009b -> CYRILLIC CAPITAL LETTER DZHE
    '\u044e'   #  0x009c -> CYRILLIC SMALL LETTER YU
    '\u042e'   #  0x009d -> CYRILLIC CAPITAL LETTER YU
    '\u044a'   #  0x009e -> CYRILLIC SMALL LETTER HARD SIGN
    '\u042a'   #  0x009f -> CYRILLIC CAPITAL LETTER HARD SIGN
    '\u0430'   #  0x00a0 -> CYRILLIC SMALL LETTER A
    '\u0410'   #  0x00a1 -> CYRILLIC CAPITAL LETTER A
    '\u0431'   #  0x00a2 -> CYRILLIC SMALL LETTER BE
    '\u0411'   #  0x00a3 -> CYRILLIC CAPITAL LETTER BE
    '\u0446'   #  0x00a4 -> CYRILLIC SMALL LETTER TSE
    '\u0426'   #  0x00a5 -> CYRILLIC CAPITAL LETTER TSE
    '\u0434'   #  0x00a6 -> CYRILLIC SMALL LETTER DE
    '\u0414'   #  0x00a7 -> CYRILLIC CAPITAL LETTER DE
    '\u0435'   #  0x00a8 -> CYRILLIC SMALL LETTER IE
    '\u0415'   #  0x00a9 -> CYRILLIC CAPITAL LETTER IE
    '\u0444'   #  0x00aa -> CYRILLIC SMALL LETTER EF
    '\u0424'   #  0x00ab -> CYRILLIC CAPITAL LETTER EF
    '\u0433'   #  0x00ac -> CYRILLIC SMALL LETTER GHE
    '\u0413'   #  0x00ad -> CYRILLIC CAPITAL LETTER GHE
    '\xab'     #  0x00ae -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    '\xbb'     #  0x00af -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    '\u2591'   #  0x00b0 -> LIGHT SHADE
    '\u2592'   #  0x00b1 -> MEDIUM SHADE
    '\u2593'   #  0x00b2 -> DARK SHADE
    '\u2502'   #  0x00b3 -> BOX DRAWINGS LIGHT VERTICAL
    '\u2524'   #  0x00b4 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    '\u0445'   #  0x00b5 -> CYRILLIC SMALL LETTER HA
    '\u0425'   #  0x00b6 -> CYRILLIC CAPITAL LETTER HA
    '\u0438'   #  0x00b7 -> CYRILLIC SMALL LETTER I
    '\u0418'   #  0x00b8 -> CYRILLIC CAPITAL LETTER I
    '\u2563'   #  0x00b9 -> BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    '\u2551'   #  0x00ba -> BOX DRAWINGS DOUBLE VERTICAL
    '\u2557'   #  0x00bb -> BOX DRAWINGS DOUBLE DOWN AND LEFT
    '\u255d'   #  0x00bc -> BOX DRAWINGS DOUBLE UP AND LEFT
    '\u0439'   #  0x00bd -> CYRILLIC SMALL LETTER SHORT I
    '\u0419'   #  0x00be -> CYRILLIC CAPITAL LETTER SHORT I
    '\u2510'   #  0x00bf -> BOX DRAWINGS LIGHT DOWN AND LEFT
    '\u2514'   #  0x00c0 -> BOX DRAWINGS LIGHT UP AND RIGHT
    '\u2534'   #  0x00c1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    '\u252c'   #  0x00c2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    '\u251c'   #  0x00c3 -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    '\u2500'   #  0x00c4 -> BOX DRAWINGS LIGHT HORIZONTAL
    '\u253c'   #  0x00c5 -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    '\u043a'   #  0x00c6 -> CYRILLIC SMALL LETTER KA
    '\u041a'   #  0x00c7 -> CYRILLIC CAPITAL LETTER KA
    '\u255a'   #  0x00c8 -> BOX DRAWINGS DOUBLE UP AND RIGHT
    '\u2554'   #  0x00c9 -> BOX DRAWINGS DOUBLE DOWN AND RIGHT
    '\u2569'   #  0x00ca -> BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    '\u2566'   #  0x00cb -> BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    '\u2560'   #  0x00cc -> BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    '\u2550'   #  0x00cd -> BOX DRAWINGS DOUBLE HORIZONTAL
    '\u256c'   #  0x00ce -> BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    '\xa4'     #  0x00cf -> CURRENCY SIGN
    '\u043b'   #  0x00d0 -> CYRILLIC SMALL LETTER EL
    '\u041b'   #  0x00d1 -> CYRILLIC CAPITAL LETTER EL
    '\u043c'   #  0x00d2 -> CYRILLIC SMALL LETTER EM
    '\u041c'   #  0x00d3 -> CYRILLIC CAPITAL LETTER EM
    '\u043d'   #  0x00d4 -> CYRILLIC SMALL LETTER EN
    '\u041d'   #  0x00d5 -> CYRILLIC CAPITAL LETTER EN
    '\u043e'   #  0x00d6 -> CYRILLIC SMALL LETTER O
    '\u041e'   #  0x00d7 -> CYRILLIC CAPITAL LETTER O
    '\u043f'   #  0x00d8 -> CYRILLIC SMALL LETTER PE
    '\u2518'   #  0x00d9 -> BOX DRAWINGS LIGHT UP AND LEFT
    '\u250c'   #  0x00da -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    '\u2588'   #  0x00db -> FULL BLOCK
    '\u2584'   #  0x00dc -> LOWER HALF BLOCK
    '\u041f'   #  0x00dd -> CYRILLIC CAPITAL LETTER PE
    '\u044f'   #  0x00de -> CYRILLIC SMALL LETTER YA
    '\u2580'   #  0x00df -> UPPER HALF BLOCK
    '\u042f'   #  0x00e0 -> CYRILLIC CAPITAL LETTER YA
    '\u0440'   #  0x00e1 -> CYRILLIC SMALL LETTER ER
    '\u0420'   #  0x00e2 -> CYRILLIC CAPITAL LETTER ER
    '\u0441'   #  0x00e3 -> CYRILLIC SMALL LETTER ES
    '\u0421'   #  0x00e4 -> CYRILLIC CAPITAL LETTER ES
    '\u0442'   #  0x00e5 -> CYRILLIC SMALL LETTER TE
    '\u0422'   #  0x00e6 -> CYRILLIC CAPITAL LETTER TE
    '\u0443'   #  0x00e7 -> CYRILLIC SMALL LETTER U
    '\u0423'   #  0x00e8 -> CYRILLIC CAPITAL LETTER U
    '\u0436'   #  0x00e9 -> CYRILLIC SMALL LETTER ZHE
    '\u0416'   #  0x00ea -> CYRILLIC CAPITAL LETTER ZHE
    '\u0432'   #  0x00eb -> CYRILLIC SMALL LETTER VE
    '\u0412'   #  0x00ec -> CYRILLIC CAPITAL LETTER VE
    '\u044c'   #  0x00ed -> CYRILLIC SMALL LETTER SOFT SIGN
    '\u042c'   #  0x00ee -> CYRILLIC CAPITAL LETTER SOFT SIGN
    '\u2116'   #  0x00ef -> NUMERO SIGN
    '\xad'     #  0x00f0 -> SOFT HYPHEN
    '\u044b'   #  0x00f1 -> CYRILLIC SMALL LETTER YERU
    '\u042b'   #  0x00f2 -> CYRILLIC CAPITAL LETTER YERU
    '\u0437'   #  0x00f3 -> CYRILLIC SMALL LETTER ZE
    '\u0417'   #  0x00f4 -> CYRILLIC CAPITAL LETTER ZE
    '\u0448'   #  0x00f5 -> CYRILLIC SMALL LETTER SHA
    '\u0428'   #  0x00f6 -> CYRILLIC CAPITAL LETTER SHA
    '\u044d'   #  0x00f7 -> CYRILLIC SMALL LETTER E
    '\u042d'   #  0x00f8 -> CYRILLIC CAPITAL LETTER E
    '\u0449'   #  0x00f9 -> CYRILLIC SMALL LETTER SHCHA
    '\u0429'   #  0x00fa -> CYRILLIC CAPITAL LETTER SHCHA
    '\u0447'   #  0x00fb -> CYRILLIC SMALL LETTER CHE
    '\u0427'   #  0x00fc -> CYRILLIC CAPITAL LETTER CHE
    '\xa7'     #  0x00fd -> SECTION SIGN
    '\u25a0'   #  0x00fe -> BLACK SQUARE
    '\xa0'     #  0x00ff -> NO-BREAK SPACE
)

### Encoding Map

encoding_map = {
    0x0000: 0x0000,     #  NULL
    0x0001: 0x0001,     #  START OF HEADING
    0x0002: 0x0002,     #  START OF TEXT
    0x0003: 0x0003,     #  END OF TEXT
    0x0004: 0x0004,     #  END OF TRANSMISSION
    0x0005: 0x0005,     #  ENQUIRY
    0x0006: 0x0006,     #  ACKNOWLEDGE
    0x0007: 0x0007,     #  BELL
    0x0008: 0x0008,     #  BACKSPACE
    0x0009: 0x0009,     #  HORIZONTAL TABULATION
    0x000a: 0x000a,     #  LINE FEED
    0x000b: 0x000b,     #  VERTICAL TABULATION
    0x000c: 0x000c,     #  FORM FEED
    0x000d: 0x000d,     #  CARRIAGE RETURN
    0x000e: 0x000e,     #  SHIFT OUT
    0x000f: 0x000f,     #  SHIFT IN
    0x0010: 0x0010,     #  DATA LINK ESCAPE
    0x0011: 0x0011,     #  DEVICE CONTROL ONE
    0x0012: 0x0012,     #  DEVICE CONTROL TWO
    0x0013: 0x0013,     #  DEVICE CONTROL THREE
    0x0014: 0x0014,     #  DEVICE CONTROL FOUR
    0x0015: 0x0015,     #  NEGATIVE ACKNOWLEDGE
    0x0016: 0x0016,     #  SYNCHRONOUS IDLE
    0x0017: 0x0017,     #  END OF TRANSMISSION BLOCK
    0x0018: 0x0018,     #  CANCEL
    0x0019: 0x0019,     #  END OF MEDIUM
    0x001a: 0x001a,     #  SUBSTITUTE
    0x001b: 0x001b,     #  ESCAPE
    0x001c: 0x001c,     #  FILE SEPARATOR
    0x001d: 0x001d,     #  GROUP SEPARATOR
    0x001e: 0x001e,     #  RECORD SEPARATOR
    0x001f: 0x001f,     #  UNIT SEPARATOR
    0x0020: 0x0020,     #  SPACE
    0x0021: 0x0021,     #  EXCLAMATION MARK
    0x0022: 0x0022,     #  QUOTATION MARK
    0x0023: 0x0023,     #  NUMBER SIGN
    0x0024: 0x0024,     #  DOLLAR SIGN
    0x0025: 0x0025,     #  PERCENT SIGN
    0x0026: 0x0026,     #  AMPERSAND
    0x0027: 0x0027,     #  APOSTROPHE
    0x0028: 0x0028,     #  LEFT PARENTHESIS
    0x0029: 0x0029,     #  RIGHT PARENTHESIS
    0x002a: 0x002a,     #  ASTERISK
    0x002b: 0x002b,     #  PLUS SIGN
    0x002c: 0x002c,     #  COMMA
    0x002d: 0x002d,     #  HYPHEN-MINUS
    0x002e: 0x002e,     #  FULL STOP
    0x002f: 0x002f,     #  SOLIDUS
    0x0030: 0x0030,     #  DIGIT ZERO
    0x0031: 0x0031,     #  DIGIT ONE
    0x0032: 0x0032,     #  DIGIT TWO
    0x0033: 0x0033,     #  DIGIT THREE
    0x0034: 0x0034,     #  DIGIT FOUR
    0x0035: 0x0035,     #  DIGIT FIVE
    0x0036: 0x0036,     #  DIGIT SIX
    0x0037: 0x0037,     #  DIGIT SEVEN
    0x0038: 0x0038,     #  DIGIT EIGHT
    0x0039: 0x0039,     #  DIGIT NINE
    0x003a: 0x003a,     #  COLON
    0x003b: 0x003b,     #  SEMICOLON
    0x003c: 0x003c,     #  LESS-THAN SIGN
    0x003d: 0x003d,     #  EQUALS SIGN
    0x003e: 0x003e,     #  GREATER-THAN SIGN
    0x003f: 0x003f,     #  QUESTION MARK
    0x0040: 0x0040,     #  COMMERCIAL AT
    0x0041: 0x0041,     #  LATIN CAPITAL LETTER A
    0x0042: 0x0042,     #  LATIN CAPITAL LETTER B
    0x0043: 0x0043,     #  LATIN CAPITAL LETTER C
    0x0044: 0x0044,     #  LATIN CAPITAL LETTER D
    0x0045: 0x0045,     #  LATIN CAPITAL LETTER E
    0x0046: 0x0046,     #  LATIN CAPITAL LETTER F
    0x0047: 0x0047,     #  LATIN CAPITAL LETTER G
    0x0048: 0x0048,     #  LATIN CAPITAL LETTER H
    0x0049: 0x0049,     #  LATIN CAPITAL LETTER I
    0x004a: 0x004a,     #  LATIN CAPITAL LETTER J
    0x004b: 0x004b,     #  LATIN CAPITAL LETTER K
    0x004c: 0x004c,     #  LATIN CAPITAL LETTER L
    0x004d: 0x004d,     #  LATIN CAPITAL LETTER M
    0x004e: 0x004e,     #  LATIN CAPITAL LETTER N
    0x004f: 0x004f,     #  LATIN CAPITAL LETTER O
    0x0050: 0x0050,     #  LATIN CAPITAL LETTER P
    0x0051: 0x0051,     #  LATIN CAPITAL LETTER Q
    0x0052: 0x0052,     #  LATIN CAPITAL LETTER R
    0x0053: 0x0053,     #  LATIN CAPITAL LETTER S
    0x0054: 0x0054,     #  LATIN CAPITAL LETTER T
    0x0055: 0x0055,     #  LATIN CAPITAL LETTER U
    0x0056: 0x0056,     #  LATIN CAPITAL LETTER V
    0x0057: 0x0057,     #  LATIN CAPITAL LETTER W
    0x0058: 0x0058,     #  LATIN CAPITAL LETTER X
    0x0059: 0x0059,     #  LATIN CAPITAL LETTER Y
    0x005a: 0x005a,     #  LATIN CAPITAL LETTER Z
    0x005b: 0x005b,     #  LEFT SQUARE BRACKET
    0x005c: 0x005c,     #  REVERSE SOLIDUS
    0x005d: 0x005d,     #  RIGHT SQUARE BRACKET
    0x005e: 0x005e,     #  CIRCUMFLEX ACCENT
    0x005f: 0x005f,     #  LOW LINE
    0x0060: 0x0060,     #  GRAVE ACCENT
    0x0061: 0x0061,     #  LATIN SMALL LETTER A
    0x0062: 0x0062,     #  LATIN SMALL LETTER B
    0x0063: 0x0063,     #  LATIN SMALL LETTER C
    0x0064: 0x0064,     #  LATIN SMALL LETTER D
    0x0065: 0x0065,     #  LATIN SMALL LETTER E
    0x0066: 0x0066,     #  LATIN SMALL LETTER F
    0x0067: 0x0067,     #  LATIN SMALL LETTER G
    0x0068: 0x0068,     #  LATIN SMALL LETTER H
    0x0069: 0x0069,     #  LATIN SMALL LETTER I
    0x006a: 0x006a,     #  LATIN SMALL LETTER J
    0x006b: 0x006b,     #  LATIN SMALL LETTER K
    0x006c: 0x006c,     #  LATIN SMALL LETTER L
    0x006d: 0x006d,     #  LATIN SMALL LETTER M
    0x006e: 0x006e,     #  LATIN SMALL LETTER N
    0x006f: 0x006f,     #  LATIN SMALL LETTER O
    0x0070: 0x0070,     #  LATIN SMALL LETTER P
    0x0071: 0x0071,     #  LATIN SMALL LETTER Q
    0x0072: 0x0072,     #  LATIN SMALL LETTER R
    0x0073: 0x0073,     #  LATIN SMALL LETTER S
    0x0074: 0x0074,     #  LATIN SMALL LETTER T
    0x0075: 0x0075,     #  LATIN SMALL LETTER U
    0x0076: 0x0076,     #  LATIN SMALL LETTER V
    0x0077: 0x0077,     #  LATIN SMALL LETTER W
    0x0078: 0x0078,     #  LATIN SMALL LETTER X
    0x0079: 0x0079,     #  LATIN SMALL LETTER Y
    0x007a: 0x007a,     #  LATIN SMALL LETTER Z
    0x007b: 0x007b,     #  LEFT CURLY BRACKET
    0x007c: 0x007c,     #  VERTICAL LINE
    0x007d: 0x007d,     #  RIGHT CURLY BRACKET
    0x007e: 0x007e,     #  TILDE
    0x007f: 0x007f,     #  DELETE
    0x00a0: 0x00ff,     #  NO-BREAK SPACE
    0x00a4: 0x00cf,     #  CURRENCY SIGN
    0x00a7: 0x00fd,     #  SECTION SIGN
    0x00ab: 0x00ae,     #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00ad: 0x00f0,     #  SOFT HYPHEN
    0x00bb: 0x00af,     #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x0401: 0x0085,     #  CYRILLIC CAPITAL LETTER IO
    0x0402: 0x0081,     #  CYRILLIC CAPITAL LETTER DJE
    0x0403: 0x0083,     #  CYRILLIC CAPITAL LETTER GJE
    0x0404: 0x0087,     #  CYRILLIC CAPITAL LETTER UKRAINIAN IE
    0x0405: 0x0089,     #  CYRILLIC CAPITAL LETTER DZE
    0x0406: 0x008b,     #  CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    0x0407: 0x008d,     #  CYRILLIC CAPITAL LETTER YI
    0x0408: 0x008f,     #  CYRILLIC CAPITAL LETTER JE
    0x0409: 0x0091,     #  CYRILLIC CAPITAL LETTER LJE
    0x040a: 0x0093,     #  CYRILLIC CAPITAL LETTER NJE
    0x040b: 0x0095,     #  CYRILLIC CAPITAL LETTER TSHE
    0x040c: 0x0097,     #  CYRILLIC CAPITAL LETTER KJE
    0x040e: 0x0099,     #  CYRILLIC CAPITAL LETTER SHORT U
    0x040f: 0x009b,     #  CYRILLIC CAPITAL LETTER DZHE
    0x0410: 0x00a1,     #  CYRILLIC CAPITAL LETTER A
    0x0411: 0x00a3,     #  CYRILLIC CAPITAL LETTER BE
    0x0412: 0x00ec,     #  CYRILLIC CAPITAL LETTER VE
    0x0413: 0x00ad,     #  CYRILLIC CAPITAL LETTER GHE
    0x0414: 0x00a7,     #  CYRILLIC CAPITAL LETTER DE
    0x0415: 0x00a9,     #  CYRILLIC CAPITAL LETTER IE
    0x0416: 0x00ea,     #  CYRILLIC CAPITAL LETTER ZHE
    0x0417: 0x00f4,     #  CYRILLIC CAPITAL LETTER ZE
    0x0418: 0x00b8,     #  CYRILLIC CAPITAL LETTER I
    0x0419: 0x00be,     #  CYRILLIC CAPITAL LETTER SHORT I
    0x041a: 0x00c7,     #  CYRILLIC CAPITAL LETTER KA
    0x041b: 0x00d1,     #  CYRILLIC CAPITAL LETTER EL
    0x041c: 0x00d3,     #  CYRILLIC CAPITAL LETTER EM
    0x041d: 0x00d5,     #  CYRILLIC CAPITAL LETTER EN
    0x041e: 0x00d7,     #  CYRILLIC CAPITAL LETTER O
    0x041f: 0x00dd,     #  CYRILLIC CAPITAL LETTER PE
    0x0420: 0x00e2,     #  CYRILLIC CAPITAL LETTER ER
    0x0421: 0x00e4,     #  CYRILLIC CAPITAL LETTER ES
    0x0422: 0x00e6,     #  CYRILLIC CAPITAL LETTER TE
    0x0423: 0x00e8,     #  CYRILLIC CAPITAL LETTER U
    0x0424: 0x00ab,     #  CYRILLIC CAPITAL LETTER EF
    0x0425: 0x00b6,     #  CYRILLIC CAPITAL LETTER HA
    0x0426: 0x00a5,     #  CYRILLIC CAPITAL LETTER TSE
    0x0427: 0x00fc,     #  CYRILLIC CAPITAL LETTER CHE
    0x0428: 0x00f6,     #  CYRILLIC CAPITAL LETTER SHA
    0x0429: 0x00fa,     #  CYRILLIC CAPITAL LETTER SHCHA
    0x042a: 0x009f,     #  CYRILLIC CAPITAL LETTER HARD SIGN
    0x042b: 0x00f2,     #  CYRILLIC CAPITAL LETTER YERU
    0x042c: 0x00ee,     #  CYRILLIC CAPITAL LETTER SOFT SIGN
    0x042d: 0x00f8,     #  CYRILLIC CAPITAL LETTER E
    0x042e: 0x009d,     #  CYRILLIC CAPITAL LETTER YU
    0x042f: 0x00e0,     #  CYRILLIC CAPITAL LETTER YA
    0x0430: 0x00a0,     #  CYRILLIC SMALL LETTER A
    0x0431: 0x00a2,     #  CYRILLIC SMALL LETTER BE
    0x0432: 0x00eb,     #  CYRILLIC SMALL LETTER VE
    0x0433: 0x00ac,     #  CYRILLIC SMALL LETTER GHE
    0x0434: 0x00a6,     #  CYRILLIC SMALL LETTER DE
    0x0435: 0x00a8,     #  CYRILLIC SMALL LETTER IE
    0x0436: 0x00e9,     #  CYRILLIC SMALL LETTER ZHE
    0x0437: 0x00f3,     #  CYRILLIC SMALL LETTER ZE
    0x0438: 0x00b7,     #  CYRILLIC SMALL LETTER I
    0x0439: 0x00bd,     #  CYRILLIC SMALL LETTER SHORT I
    0x043a: 0x00c6,     #  CYRILLIC SMALL LETTER KA
    0x043b: 0x00d0,     #  CYRILLIC SMALL LETTER EL
    0x043c: 0x00d2,     #  CYRILLIC SMALL LETTER EM
    0x043d: 0x00d4,     #  CYRILLIC SMALL LETTER EN
    0x043e: 0x00d6,     #  CYRILLIC SMALL LETTER O
    0x043f: 0x00d8,     #  CYRILLIC SMALL LETTER PE
    0x0440: 0x00e1,     #  CYRILLIC SMALL LETTER ER
    0x0441: 0x00e3,     #  CYRILLIC SMALL LETTER ES
    0x0442: 0x00e5,     #  CYRILLIC SMALL LETTER TE
    0x0443: 0x00e7,     #  CYRILLIC SMALL LETTER U
    0x0444: 0x00aa,     #  CYRILLIC SMALL LETTER EF
    0x0445: 0x00b5,     #  CYRILLIC SMALL LETTER HA
    0x0446: 0x00a4,     #  CYRILLIC SMALL LETTER TSE
    0x0447: 0x00fb,     #  CYRILLIC SMALL LETTER CHE
    0x0448: 0x00f5,     #  CYRILLIC SMALL LETTER SHA
    0x0449: 0x00f9,     #  CYRILLIC SMALL LETTER SHCHA
    0x044a: 0x009e,     #  CYRILLIC SMALL LETTER HARD SIGN
    0x044b: 0x00f1,     #  CYRILLIC SMALL LETTER YERU
    0x044c: 0x00ed,     #  CYRILLIC SMALL LETTER SOFT SIGN
    0x044d: 0x00f7,     #  CYRILLIC SMALL LETTER E
    0x044e: 0x009c,     #  CYRILLIC SMALL LETTER YU
    0x044f: 0x00de,     #  CYRILLIC SMALL LETTER YA
    0x0451: 0x0084,     #  CYRILLIC SMALL LETTER IO
    0x0452: 0x0080,     #  CYRILLIC SMALL LETTER DJE
    0x0453: 0x0082,     #  CYRILLIC SMALL LETTER GJE
    0x0454: 0x0086,     #  CYRILLIC SMALL LETTER UKRAINIAN IE
    0x0455: 0x0088,     #  CYRILLIC SMALL LETTER DZE
    0x0456: 0x008a,     #  CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    0x0457: 0x008c,     #  CYRILLIC SMALL LETTER YI
    0x0458: 0x008e,     #  CYRILLIC SMALL LETTER JE
    0x0459: 0x0090,     #  CYRILLIC SMALL LETTER LJE
    0x045a: 0x0092,     #  CYRILLIC SMALL LETTER NJE
    0x045b: 0x0094,     #  CYRILLIC SMALL LETTER TSHE
    0x045c: 0x0096,     #  CYRILLIC SMALL LETTER KJE
    0x045e: 0x0098,     #  CYRILLIC SMALL LETTER SHORT U
    0x045f: 0x009a,     #  CYRILLIC SMALL LETTER DZHE
    0x2116: 0x00ef,     #  NUMERO SIGN
    0x2500: 0x00c4,     #  BOX DRAWINGS LIGHT HORIZONTAL
    0x2502: 0x00b3,     #  BOX DRAWINGS LIGHT VERTICAL
    0x250c: 0x00da,     #  BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x2510: 0x00bf,     #  BOX DRAWINGS LIGHT DOWN AND LEFT
    0x2514: 0x00c0,     #  BOX DRAWINGS LIGHT UP AND RIGHT
    0x2518: 0x00d9,     #  BOX DRAWINGS LIGHT UP AND LEFT
    0x251c: 0x00c3,     #  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x2524: 0x00b4,     #  BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x252c: 0x00c2,     #  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x2534: 0x00c1,     #  BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x253c: 0x00c5,     #  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x2550: 0x00cd,     #  BOX DRAWINGS DOUBLE HORIZONTAL
    0x2551: 0x00ba,     #  BOX DRAWINGS DOUBLE VERTICAL
    0x2554: 0x00c9,     #  BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0x2557: 0x00bb,     #  BOX DRAWINGS DOUBLE DOWN AND LEFT
    0x255a: 0x00c8,     #  BOX DRAWINGS DOUBLE UP AND RIGHT
    0x255d: 0x00bc,     #  BOX DRAWINGS DOUBLE UP AND LEFT
    0x2560: 0x00cc,     #  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0x2563: 0x00b9,     #  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0x2566: 0x00cb,     #  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0x2569: 0x00ca,     #  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0x256c: 0x00ce,     #  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0x2580: 0x00df,     #  UPPER HALF BLOCK
    0x2584: 0x00dc,     #  LOWER HALF BLOCK
    0x2588: 0x00db,     #  FULL BLOCK
    0x2591: 0x00b0,     #  LIGHT SHADE
    0x2592: 0x00b1,     #  MEDIUM SHADE
    0x2593: 0x00b2,     #  DARK SHADE
    0x25a0: 0x00fe,     #  BLACK SQUARE
}
