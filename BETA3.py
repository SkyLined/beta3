# -*- coding: latin1 -*-
import re, sys

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
    errors |= CheckChar(i, char, badchars, switches, char_as_string = "%02X" % ord(char))
  return None, len(data), errors

def EncodeAscii(format, data, badchars, switches):
  result = ""
  errors = False
  for i in range(0, len(data)):
    char = data[i]
    errors |= CheckChar(i, char, badchars, switches, char_as_string = "%02X" % ord(char))
    result += format % ord(char)
  return result, len(data), errors

def EncodeUnicode(format, data, badchars, switches):
  result = ""
  errors = False
  for i in range(0, len(data), 2):
    char_code = ord(data[i]) + ord(data[i + 1]) * 256;
    errors |= CheckChar(i, unichr(char_code), badchars, switches, char_as_string = "%04X" % char_code)
    result += format % char_code
  return result, len(data) * 2, errors

def CheckChar(i, char, badchars, switches, char_as_string):
  errors = False
  if char in badchars:
    print >>sys.stderr, "Char %d @0x%02X = bad (%s)" % (i, i, char_as_string)
    errors = True
  if switches["--nullfree"] and char == '\0':
    print >>sys.stderr, "Char %d @0x%02X = bad (NULL)" % (i, i)
    errors = True
  if switches["--uppercase"] and char not in uppercase:
    if not switches["--latin-1"] or char not in uppercase_latin_1:
      if not switches["--cp437"] or char not in uppercase_cp437:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-uppercase '%s' %s)" % (i, i, char, char_as_string)
        errors = True
  if switches["--lowercase"] and char not in lowercase:
    if not switches["--latin-1"] or char not in lowercase_latin_1:
      if not switches["--cp437"] or char not in lowercase_cp437:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-lowercase '%s' %s)" % (i, i, char, char_as_string)
        errors = True
  if switches["--mixedcase"] and char not in mixedcase:
    if not switches["--latin-1"] or char not in mixedcase_latin_1:
      if not switches["--cp437"] or char not in mixedcase_cp437:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-alphanumeric '%s' %s)" % (i, i, char, char_as_string)
        errors = True
  return errors

def Decode(decoder_re, decode_base, data, badchars, switches):
  result = ""
  errors = False
  i = 0
  while i < len(data):
    char_re_match = re.match("^" + decoder_re, data[i:], re.IGNORECASE)
    if not char_re_match:
      print >>sys.stderr, "Char %d @0x%02X does not match encoding: %s." % (i, i, repr(data[i]))
      i += 1
    else:
      char_encoded_string = char_re_match.group(0)
      char_code_string = char_re_match.group(1)
      try:
        char_code = int(char_code_string, decode_base)
      except ValueError, e:
        print >>sys.stderr, "Char %d @0x%02X has bad character code: %s" % (i, i, e.args[0])
        errors = True
      if char_code < 0x100:
        char = chr(char_code)
      else:
        char = unichr(char_code)
      errors |= CheckChar(i, char, badchars, switches, char_encoded_string)
      result += char
      i += len(char_encoded_string)
  return result, len(result), errors

encodings = {
  "none":  {"enc": EncodeNone,    "fmt": None,        "re": None,                  "base": None},
  "h":     {"enc": EncodeAscii,   "fmt": "%02X",      "re": r"([0-9A-F]{2})",      "base": 16},
  "hu":    {"enc": EncodeUnicode, "fmt": "%04X",      "re": r"([0-9A-F]{4})",      "base": 16},
  "\\x":   {"enc": EncodeAscii,   "fmt": "\\x%02X",   "re": r"\\x([0-9A-F]{2})",   "base": 16},
  "\\u":   {"enc": EncodeUnicode, "fmt": "\\u%04X",   "re": r"\\u([0-9A-F]{4})",   "base": 16},
  "\\u00": {"enc": EncodeAscii,   "fmt": "\\u00%02X", "re": r"\\u00([0-9A-F]{2})", "base": 16},
  "%":     {"enc": EncodeAscii,   "fmt": "%%%02X",    "re": r"%([0-9A-F]{2})",     "base": 16},
  "%u":    {"enc": EncodeUnicode, "fmt": "%%u%04X",   "re": r"%u([0-9A-F]{4})",    "base": 16},
  "%u00":  {"enc": EncodeAscii,   "fmt": "%%u00%02X", "re": r"%u00([0-9A-F]{2})",  "base": 16},
  "&#":    {"enc": EncodeAscii,   "fmt": "&#%d;",     "re": r"&#([0-9]{1,3})",     "base": 10},
  "&#u":   {"enc": EncodeUnicode, "fmt": "&#%d;",     "re": r"&#([0-9]{1,5})",     "base": 10},
  "&#x":   {"enc": EncodeAscii,   "fmt": "&#x%X;",    "re": r"&#x([0-9A-F]{1,2})", "base": 16},
  "&#xu":  {"enc": EncodeUnicode, "fmt": "&#x%X;",    "re": r"&#x([0-9A-F]{1,4})", "base": 16}
}
switches = {
    "--nullfree": False, 
    "--lowercase": False, 
    "--uppercase": False,
    "--mixedcase": False,
    "--cp437": False,
    "--latin-1": False,
    "--count": False,
    "--decode": False,
    "--badchars": ""
}

def Help():
  print "".center(output_screen_width, "_")
  print
  print """    ,sSSSs,   ,sSSSs,  BETA3 - Multi-format shellcode encoding tool.         """.center(output_screen_width)
  print """   iS"`  XP  YS"  ,SY  (Version 1.0)                                         """.center(output_screen_width)
  print """  .SP dSS"      ssS"   Copyright (C) 2003-2009 by Berend-Jan "SkyLined" Wever""".center(output_screen_width)
  print """  dS'   Xb  SP,  ;SP   <berendjanwever@gmail.com>                            """.center(output_screen_width)
  print """ .SP dSSP'  "YSSSY"    http://skypher.com/wiki/index.php/BETA3               """.center(output_screen_width)
  print """ 4S:_________________________________________________________________________""".center(output_screen_width, "_")
  print
  print "Purpose:"
  print "  BETA can convert raw binary shellcode into text that can be used in exploit"
  print "  source-code. It can convert raw binary data to a large number of encodings."
  print "  It can also do the revers: decode encoded data into binary from the same"
  print "  types of encodings."
  print
  print "Usage:"
  print "  BETA3.py  [arguments|options]"
  print ""
  print "Arguments:"
  print "  input file path        - Input file with data to be encoded (optional,"
  print "                           default is to read data from stdin)"
  print "  encoding               - One of the following encodings:"
  sorted_encoder_keys = encodings.keys()
  sorted_encoder_keys.sort()
  for name in sorted_encoder_keys:
    if name != "none":
      encoder_function = encodings[name]["enc"]
      encoder_fmt = encodings[name]["fmt"]
      print "    %-5s : %s" % (name, encoder_function(encoder_fmt, "ABCD", "", switches)[0])
    else:
      print "    %-5s : Do not encode or output the input." % name
  print "    (All these samples use as input data the string \"ABCD\". You cannot use"
  print "    \"none\" encoding with the \"--decode\" option)."
  print
  print "Options:"
  print "    --decode             - Decode encoded data to binary."
  print "                           (By default BETA3 encodes binary data)."
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
  global switches, encodings
  encoding_info = None
  file_name = None
  if len(sys.argv) == 1:
    Help()
    return True
  for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    if arg in encodings:
      encoding_info = encodings[arg]
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
  if not encoding_info:
    encoding_info = encodings["none"]
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
      badchars += unichr(int(i, 16))
  if not switches["--decode"]:
    encoder_function = encoding_info["enc"]
    encoder_fmt = encoding_info["fmt"]
    encoded_shellcode, byte_count, errors = encoder_function(encoder_fmt, data, badchars, switches)
    if switches["--count"]:
      print "Size: %d (0x%X) bytes." % (byte_count, byte_count)
    if encoded_shellcode is not None:
      sys.stdout.write(encoded_shellcode)
  else:
    decoder_re = encoding_info["re"]
    decoder_base = encoding_info["base"]
    if encoding_info == encodings["none"]:
      print >>sys.stderr, "Cannot decode without an encoding."
      return False
    decoded_shellcode, byte_count, errors = Decode(decoder_re, decoder_base, data, badchars, switches)
    if switches["--count"]:
      print "Size: %d (0x%X) bytes." % (byte_count, byte_count)
    if decoded_shellcode is not None:
      sys.stdout.write(decoded_shellcode)
  return not errors

if __name__ == "__main__":
  success = Main()
  exit_code = {True: 0, False: 1}[success]
  exit(exit_code)