# -*- coding: latin1 -*-
import sys

#_______________________________________________________________________________________________________________________
#                                                                                                                       
#                      ,sSSSs,   ,sSSSs,   : BETA3 - Multi-format shellcode encoding tool.                              
#                     iS"`  XP  YS"  ,SY   :                                                                            
#                    .SP dSS"      ssS"    : Copyright (C) 2003-2009 by SkyLined.                                       
#                    dS'   Xb  SP,  ;SP    : <berendjanwever@gmail.com>                                                 
#                   .SP dSSP'  "YSSSY"     : http://skypher.com/wiki/index.php/BETA3                                    
#__________________ 4S:_________________________________________________________________________________________________
#                                                                                                                       


# http://en.wikipedia.org/wiki/Ascii
# http://en.wikipedia.org/wiki/Code_page_437
# http://en.wikipedia.org/wiki/ISO/IEC_8859-1
numbers            = "0123456789"
uppercase          = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uppercase_cp437    = "€Ž’š¥âãäèêíî"
uppercase_latin_1  = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞ"
lowercase          = "abcdefghijklmnopqrstuvwxyz"
lowercase_cp437    = "‚ƒ„…†‡ˆ‰Š‹Œ‘“”•–—˜Ÿ ¡¢£¤àáåæçéë"
lowercase_latin_1  = "ßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"
mixedcase          = uppercase + lowercase
mixedcase_cp437    = uppercase_cp437 + lowercase_cp437
mixedcase_latin_1  = uppercase_latin_1 + lowercase_latin_1

output_screen_width = 119
output_header_size = int(output_screen_width / 3)

def EncodeNone(format, data, badchars, switches):
  errors = False
  for i in range(0, len(data)):
    char = data[i]
    errors |= CheckChar(i, char, badchars, switches, "%02X")
  return None, len(data), errors

def EncodeAscii(format, data, badchars, switches):
  result = ""
  errors = False
  for i in range(0, len(data)):
    char = data[i]
    errors |= CheckChar(i, char, badchars, switches, "%02X")
    result += format % ord(char)
  return result, len(data), errors

def EncodeUnicode(format, data, badchars, switches):
  result = ""
  errors = False
  for i in range(0, len(data), 2):
    char_code = ord(data[i]) + ord(data[i + 1]) * 256;
    errors |= CheckChar(i, chr(char_code), badchars, switches, "%04X")
    result += format % char_code
  return result, len(data) * 2, errors

def CheckChar(i, char, badchars, switches, char_hex_fmtstr):
  errors = False
  char_hex = char_hex_fmtstr % ord(char)
  if char in badchars:
    print >>sys.stderr, "Char %d @0x%02X = bad (%s)" % (i, i, char_hex)
    errors = True
  if switches["--nullfree"] and char == '\0':
    print >>sys.stderr, "Char %d @0x%02X = bad (NULL)" % (i, i)
    errors = True
  if switches["--uppercase"] and char not in uppercase:
    if not switches["--latin-1"] or char not in uppercase_latin_1:
      if not switches["--cp437"] or char not in uppercase_cp437:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-uppercase '%s' %s)" % (i, i, char, char_hex)
        errors = True
  if switches["--lowercase"] and char not in lowercase:
    if not switches["--latin-1"] or char not in lowercase_latin_1:
      if not switches["--cp437"] or char not in lowercase_cp437:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-lowercase '%s' %s)" % (i, i, char, char_hex)
        errors = True
  if switches["--mixedcase"] and char not in mixedcase:
    if not switches["--latin-1"] or char not in mixedcase_latin_1:
      if not switches["--cp437"] or char not in mixedcase_cp437:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-alphanumeric '%s' %s)" % (i, i, char, char_hex)
        errors = True
  return errors

encoders = {
  "none":  (None,        EncodeNone),
  "h":     ("%02X",      EncodeAscii),
  "hu":    ("%04X",      EncodeUnicode),
  "\\x":   ("\\x%02X",   EncodeAscii),
  "\\u":   ("\\u%02X",   EncodeUnicode),
  "\\u00": ("\\u00%02X", EncodeAscii),
  "%":     ("%%%02X",    EncodeAscii),
  "%u":    ("%%u%02X",   EncodeUnicode),
  "%u00":  ("%%u00%02X", EncodeAscii),
  "&#":    ("&#%d;",     EncodeAscii),
  "&#u":   ("&#%d;",     EncodeUnicode),
  "&#x":   ("&#x%X;",    EncodeAscii),
  "&#xu":  ("&#x%X;",    EncodeUnicode)
}
switches = {
    "--nullfree": False, 
    "--lowercase": False, 
    "--uppercase": False,
    "--mixedcase": False,
    "--cp437": False,
    "--latin-1": False,
    "--count": False,
    "--badchars": ""
}

def Help():
  print "".center(output_screen_width, "_")
  print
  print """    ,sSSSs,   ,sSSSs,  BETA3 - Multi-format shellcode encoding tool.         """.center(output_screen_width)
  print """   iS"`  XP  YS"  ,SY  (Version 0.2)                                         """.center(output_screen_width)
  print """  .SP dSS"      ssS"   Copyright (C) 2003-2009 by Berend-Jan "SkyLined" Wever""".center(output_screen_width)
  print """  dS'   Xb  SP,  ;SP   <berendjanwever@gmail.com>                            """.center(output_screen_width)
  print """ .SP dSSP'  "YSSSY"    http://skypher.com/wiki/index.php/BETA3               """.center(output_screen_width)
  print """ 4S:_________________________________________________________________________""".center(output_screen_width, "_")
  print
  print "Purpose:"
  print "  BETA can convert raw binary shellcode into text that can be used in exploit"
  print "  source-code. It can convert raw binary data to a large number of encodings."
  print
  print "Usage:"
  print "  BETA3.py  [arguments|options]"
  print ""
  print "Arguments:"
  print "  input file path        - Input file with data to be encoded (optional,"
  print "                           default is to read data from stdin)"
  print "  encoder                - One of the following encodings:"
  sorted_encoder_keys = encoders.keys()
  sorted_encoder_keys.sort()
  for i in sorted_encoder_keys:
    print "    %-5s : %s" % (i, encoders[i][1](encoders[i][0], "ABCD"))
  print "    (All these samples use as input data the string \"ABCD\")"
  print
  print "Options:"
  print "    --count              - Report the number of bytes in the output."
  print "    --nullfree           - Report any NULL characters in the data."
  print "    --badchars=XX,XX,... - Report any of the characters supplied by hex value."
  print ""
  print "    --lowercase, --uppercase, or --mixedcase"
  print "                         - Report any non-lower-, upper-, or mixedcase"
  print "                           alphanumeric characters in the data. These options"
  print "                           can be combined with both of these options:"
  print "    --latin-1            - Allow alphanumeric latin-1 high ascii characters."
  print "    --cp437              - Allow alphanumeric cp437 high ascii characters."

def Main():
  global switches, encoders
  encoder_info = None
  file_name = None
  for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    if arg in encoders:
      encoder_info = encoders[arg]
    elif arg in switches:
      switches[arg] = True
    elif arg.find("=") != -1 and arg[:arg.find("=")] in switches:
      switches[arg[:arg.find("=")]] = arg[arg.find("=")+1:]
    elif not file_name:
      file_name = arg
    else:
      print >>sys.stderr, "Two file names or unknown encoder: '%s' and '%s'" % (file_name, arg)
      Help()
      return False
  if not encoder_info:
    encoder_info = encoders["none"]
  if not file_name:
    data = sys.stdin.read()
  else:
    data_stream = open(file_name, "rb")
    try:
      data = data_stream.read()
    finally:
      data_stream.close()
  badchars = ""
  if switches is not None and switches["--badchars"] != "":
    for i in switches["--badchars"].split(","):
      badchars += chr(int(i, 16))
  encoded_shellcode, byte_count, errors = encoder_info[1](encoder_info[0], data, badchars, switches)
  if encoded_shellcode is not None:
    print encoded_shellcode
  if switches["--count"]:
    print "Size: %d (0x%X) bytes." % (byte_count, byte_count)
  return not errors

if __name__ == "__main__":
  success = Main()
  exit_code = {True: 0, False: 1}[success]
  exit(exit_code)