import ctypes
from errors import *

SHORT = ctypes.c_short
WORD  = ctypes.c_ushort
DWORD = ctypes.c_ulong
def TCHAR_ARRAY(size):
  return ctypes.create_string_buffer(size)

class SMALL_RECT(ctypes.Structure):
  _fields_ = [
    ("Left", SHORT),
    ("Top", SHORT),
    ("Right", SHORT),
    ("Bottom", SHORT)
  ]

class COORD(ctypes.Structure):
  _fields_ = [
    ("X", SHORT),
    ("Y", SHORT)
  ]

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
  _fields_ = [
    ("dwSize", COORD),
    ("dwCursorPosition", COORD),
    ("wAttributes", WORD),
    ("srWindow", SMALL_RECT),
   ( "dwMaximumWindowSize", COORD)
  ]
