import sys

MIXEDCASE_ASCII_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

output_screen_width = 119
output_header_size = int(output_screen_width / 3)

def ascii_encoder(format, data, switches = None):
  result = ""
  errors = False
  badchars = []
  if switches is not None and switches["--badchars"] != "":
    for i in switches["--badchars"].split(","):
      badchars.append(int(i, 16))
  for i in range(0, len(data)):
    char = ord(data[i]);
    if switches is not None:
      if char in badchars:
        print >>sys.stderr, "Char %d @0x%02X = bad (%02X)" % (i, i, char)
        errors = True
      if switches["--nullfree"] and char == 0:
        print >>sys.stderr, "Char %d @0x%02X = bad (NULL)" % (i, i)
        errors = True
      if switches["--uppercase"] and char >= ord('a') and char <= ord('z'):
        print >>sys.stderr, "Char %d @0x%02X = bad (lowercase '%s' %02X)" % (i, i, data[i], char)
        errors = True
      if switches["--lowercase"] and char >= ord('A') and char <= ord('Z'):
        print >>sys.stderr, "Char %d @0x%02X = bad (uppercase '%s' %02X)" % (i, i, data[i], char)
        errors = True
      if switches["--alphanumeric"] and char not in MIXEDCASE_ASCII_CHARS:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-alphanumeric '%s' %02X)" % (i, i, data[i], char)
        errors = True
    result += format % char
  return result, errors

def unicode_encoder(format, data, switches = None):
  result = ""
  errors = False
  badchars = []
  if switches is not None and switches["--badchars"] != "":
    for i in switches["--badchars"].split(","):
      badchars.append(int(i, 16))
  for i in range(0, len(data), 2):
    char = ord(data[i]) + ord(data[i + 1]) * 256;
    if switches is not None:
      if char in badchars:
        print >>sys.stderr, "Char %d @0x%02X = bad (%04X)" % (i, i, char)
        errors = True
      if switches["--nullfree"] and char == 0:
        print >>sys.stderr, "Char %d @0x%02X = bad (NULL)" % (i, i)
        errors = True
      if switches["--uppercase"] and char >= ord('a') and char <= ord('z'):
        print >>sys.stderr, "Char %d @0x%02X = bad (lowercase '%s' %04X)" % (i, i, data[i], char)
        errors = True
      if switches["--lowercase"] and char >= ord('A') and char <= ord('Z'):
        print >>sys.stderr, "Char %d @0x%02X = bad (uppercase '%s' %04X)" % (i, i, data[i], char)
        errors = True
      if switches["--alphanumeric"] and char not in MIXEDCASE_ASCII_CHARS:
        print >>sys.stderr, "Char %d @0x%02X = bad (non-alphanumeric '%s' %04X)" % (i, i, data[i], char)
        errors = True
    result += format % char
  return result, errors

encoders = {
  "h":     ("%02X",      ascii_encoder),
  "hu":    ("%04X",      unicode_encoder),
  "\\x":   ("\\x%02X",   ascii_encoder),
  "\\u":   ("\\u%02X",   unicode_encoder),
  "\\u00": ("\\u00%02X", ascii_encoder),
  "%":     ("%%%02X",    ascii_encoder),
  "%u":    ("%%u%02X",   unicode_encoder),
  "%u00":  ("%%u00%02X", ascii_encoder),
  "&#":    ("&#%d;",     ascii_encoder),
  "&#u":   ("&#%d;",     unicode_encoder),
  "&#x":   ("&#x%X;",    ascii_encoder),
  "&#xu":  ("&#x%X;",    unicode_encoder)
}
switches = {
    "--nullfree": False, 
    "--lowercase": False, 
    "--uppercase": False,
    "--alphanumeric": False,
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
  print "  BETA3.py  [file name] [encoder] [options]"
  print ""
  print "Where:"
  print "  file name = File with data to encode"
  print "  encoder = One of the following encodings (example input = 'ABCD'):"
  sorted_encoder_keys = encoders.keys()
  sorted_encoder_keys.sort()
  for i in sorted_encoder_keys:
    print "    %-5s : %s" % (i, encoders[i][1](encoders[i][0], "ABCD"))
  print "  options = One of the following switches:"
  print "    --nullfree            Report any NULL characters in the data."
  print "    --lowercase           Report any uppercase characters in the data."
  print "    --uppercase           Report any lowercase characters in the data."
  print "    --alphanumeric        Report any non-alphanumeric characters in the data."
  print "    --badchars=XX,XX,...  Report any of the characters supplied by hex value."

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
      return 1
  if not file_name:
    print >>sys.stderr, "Missing file name."
    Help()
    return 1
  if not encoder_info:
    print >>sys.stderr, "Missing/unknown encoder"
    Help()
    return 1
  data_stream = open(file_name, "rb")
  data = data_stream.read()
  encoded_shellcode, errors = encoder_info[1](encoder_info[0], data, switches)
  print encoded_shellcode
  if errors:
    return 1
  return 0

if __name__ == "__main__":
  exit(Main())