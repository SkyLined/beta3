import windows_h
import math, ctypes

stdin = ctypes.windll.kernel32.GetStdHandle(-10)
stdout = ctypes.windll.kernel32.GetStdHandle(-11)
stderr = ctypes.windll.kernel32.GetStdHandle(-12)
std_handles_default_buffer_size = 0x1000;

console_info = windows_h.CONSOLE_SCREEN_BUFFER_INFO()
if ctypes.windll.kernel32.GetConsoleScreenBufferInfo(stdout, ctypes.byref(console_info)) == 0:
  output_screen_width = 80
else:
  output_screen_width = console_info.dwSize.X - 1

output_header_size = int(output_screen_width / 3)

output_verbosity_level = 0

def SetColor(handle, fg = None, bg = None):
  table = {
    "BLACK":    0x00,
    "BLUE":     0x01,
    "GREEN":    0x02,
    "CYAN":     0x03,
    "RED":      0x04,
    "PURPLE":   0x05,
    "BROWN":    0x06,
    "LGREY":    0x07,
    "GREY":     0x08,
    "LBLUE":    0x09,
    "LGREEN":   0x0A,
    "LCYAN":    0x0B,
    "PINK":     0x0C,
    "LPURPLE":  0x0D,
    "YELLOW":   0x0E,
    "WHITE":    0x0F
  }
  if isinstance(fg, int):
    color = fg
  else:
    if fg is None or bg is None:
      console_info = windows_h.CONSOLE_SCREEN_BUFFER_INFO()
      if ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, ctypes.byref(console_info)) == 0:
        raise WindowsError("GetConsoleScreenBufferInfo call failed");
    color = 0
    if fg is None:
      color |= console_info.wAttributes & 0x0F
    else:
      color |= table[fg]
    if bg is None:
      color |= console_info.wAttributes & 0xF0
    else:
      color |= table[bg] << 4
  if ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color) == 0:
    raise WindowsError("SetConsoleTextAttribute call failed");
  return 

def GetColor(handle):
  console_info = windows_h.CONSOLE_SCREEN_BUFFER_INFO()
  if ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, ctypes.byref(console_info)) == 0:
    raise WindowsError("GetConsoleScreenBufferInfo call failed");
  return int(console_info.wAttributes) & 0xFF

def GetBufferDimensions(handle):
  console_info = windows_h.CONSOLE_SCREEN_BUFFER_INFO()
  if ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, ctypes.byref(console_info)) == 0:
    raise WindowsError("GetConsoleScreenBufferInfo call failed");
  return (console_info.dwSize.X, console_info.dwSize.Y)

def Write(handle, message, color = None):
  if color != None:
    default_color = GetColor(handle)
    SetColor(handle, color)
  try:
    lpBuffer = windows_h.TCHAR_ARRAY(len(message));
    lpBuffer.value = message;
    chars_written = windows_h.DWORD();
    if not ctypes.windll.kernel32.WriteFile(handle, lpBuffer, len(message), ctypes.byref(chars_written), 0):
      return -1
    return chars_written
  finally:
    if color != None:
      SetColor(handle, default_color)

def Read(handle, size = None):
  result = "";
  while (1):
    if size == None:
      block_size = std_handles_default_buffer_size;
    else:
      block_size = size;
    lpBuffer = windows_h.TCHAR_ARRAY(block_size);
    chars_read = windows_h.DWORD();
    if not ctypes.windll.kernel32.ReadFile(handle, lpBuffer, block_size, ctypes.byref(chars_read), 0):
      error = ctypes.windll.kernel32.GetLastError();
      return None;
    result += lpBuffer.raw[:chars_read.value];
    if chars_read != block_size or size == len(result):
      break;
  return result;

def PrintVerboseStatus(header=None, message=""):
  if output_verbosity_level > 1:
    PrintStatus(header, message)
def PrintStatus(header=None, message=""):
  if header is None:
    print "".ljust(output_screen_width) + "\r",
  status = ("%%%ds : %%s" % output_header_size) % (header, message)
  if len(status) >= output_screen_width:
    print status[:output_screen_width - 3] + "...\r",
  else:
    print status.ljust(output_screen_width) + "\r",

def PrintVerboseStatusLine(header=None, message=""):
  if output_verbosity_level:
    PrintStatusLine(header, message)
def PrintStatusLine(header=None, message=""):
  header = header.rjust(output_header_size) + " : "
  if message == "":
    print header
    return
  output_footer_size = output_screen_width - (output_header_size + 3)
  blocks = int(math.ceil(1.0 * (len(message) - len(header)) / (output_footer_size))) + 1
  block_size = int(math.ceil(len(message) / blocks))
  output_footer_size = output_screen_width - len(header)
  while len(message) > output_footer_size:
    for cut_index in range(block_size, output_footer_size):
      if message[cut_index] == " ":
        print header + message[:cut_index]
        message = message[cut_index + 1:]
        break
    else:
      print header + message[:output_footer_size - 1] + "-"
      message = message[output_footer_size - 1:]
    header = "".rjust(output_header_size + 3)
    output_footer_size = output_screen_width - (output_header_size + 3)
  if len(message) > 0:
    print (header + message).ljust(output_screen_width)

def PrintVerboseSeparator():
  if output_verbosity_level:
    PrintSeparator()
def PrintSeparator():
  print "".center(output_screen_width, "_")
  print

def PrintVerboseCenteredLine(message="", pad_char=" "):
  if output_verbosity_level:
    PrintCenteredLine(message)
def PrintCenteredLine(message="", pad_char=" "):
  if message == "":
    print
    return
  blocks = int(math.ceil(1.0 * len(message) / output_screen_width))
  block_size = int(math.ceil(len(message) / blocks))
  while len(message) > output_screen_width:
    for cut_index in range(block_size, output_screen_width):
      if message[cut_index] == " ":
        print message[:cut_index].center(output_header_size * 2 + 3, pad_char)
        message = message[cut_index + 1:]
        break
    else:
      print message[:output_screen_width - 1] + "-"
      message = message[output_screen_width - 1:]
  if len(message) > 0:
    print message.center(output_header_size * 2 + 3, pad_char)

def PrintVerboseLine(message = ""):
  if output_verbosity_level:
    PrintLine(message)
def PrintLine(message = ""):
  if output_verbosity_level == 0 or message == "":
    print message
  else:
    PrintWrappedLine(message);

def PrintVerboseWrappedLine(message = ""):
  if output_verbosity_level:
    PrintWrappedLine(message)
def PrintWrappedLine(message = ""):
  while len(message) > output_screen_width:
    for cut_index in range(output_screen_width, output_header_size * 2 + 3, -1):
      if message[cut_index] == " ":
        print message[:cut_index]
        message = message[cut_index:]
        break
    else:
        print message[:output_screen_width - 1] + "-"
        message = message[output_screen_width - 1:]
  if len(message) > 0:
    print message

