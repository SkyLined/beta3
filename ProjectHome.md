

&lt;PRE&gt;


> ,sSSSs,   ,sSSSs,  BETA3 - Multi-format shellcode encoding tool.
> iS"`  XP  YS"  ,SY  (Version 0.2)
> .SP dSS"      ssS"   Copyright (C) 2003-2009 by Berend-Jan "SkyLined" Wever
> dS'   Xb  SP,  ;SP   <berendjanwever@gmail.com>
> .SP dSSP'  "YSSSY"    http://skypher.com/wiki/index.php/BETA3
> 4S:

---


Purpose:
> BETA can convert raw binary shellcode into text that can be used in exploit
> source-code. It can convert raw binary data to a large number of encodings.
> It can also do the reverse: decode encoded data into binary from the same
> types of encodings.

Usage:
> BETA3.py  [arguments|options]

Arguments:
> input file path        - Input file with data to be encoded (optional,
> > default is to read data from stdin)

> encoding               - One of the following encodings:
> > %     : %41%42%43%27%22%0D%0A%00
> > %u    : %u4241%u2743%u0D22%u000A
> > %u00  : %u0041%u0042%u0043%u0027%u0022%u000D%u000A%u0000
> > &#    : &#65;&#66;&#67;&#39;&#34;&#13;&#10;&#0;
> > &#u   : &#16961;&#10051;&#3362;&#10;
> > &#x   : &#x41;&#x42;&#x43;&#x27;&#x22;&#xD;&#xA;&#x0;
> > &#xu  : &#x4241;&#x2743;&#xD22;&#xA;
> > 0x16  : 0x4241, 0x2743, 0x0D22, 0x000A
> > 0x16u : 0x4241, 0x2743, 0x0D22, 0x000A
> > 0x32  : 0x27434241, 0x000A0D22
> > 0x32u : 0x27434241, 0x000A0D22
> > 0x8   : 0x41, 0x42, 0x43, 0x27, 0x22, 0x0D, 0x0A, 0x00
> > \"    : ABC'\"\r\n\0
> > \'    : ABC\'"\r\n\0
> > \u    : \u4241\u2743\u0D22\u000A
> > \u00  : \u0041\u0042\u0043\u0027\u0022\u000D\u000A\u0000
> > \x    : \x41\x42\x43\x27\x22\x0D\x0A\x00
> > h     : 41424327220D0A00
> > hu    : 424127430D22000A
> > none  : Do not encode or output the input.
> > u\"   : \u4241\u2743\u0D22\n
> > u\'   : \u4241\u2743\u0D22\n


> (All these samples use as input data the string [ABC'"\r\n\0]. You cannot
> use some encodings with the "--decode" option).
> The "--big-endian" switch has the following effect on the "0x" encodings:

> 0x16  : 0x4142, 0x4327, 0x220D, 0x0A00
> 0x16u : 0x4241, 0x2743, 0x0D22, 0x000A
> 0x32  : 0x41424327, 0x220D0A00
> 0x32u : 0x42412743, 0x0D22000A
> 0x8   : 0x41, 0x42, 0x43, 0x27, 0x22, 0x0D, 0x0A, 0x00

Options:
> --decode             - Decode encoded data to binary.
> > (By default BETA3 encodes binary data).

> --count              - Report the number of bytes in the output. When used
> > with "none" encoding, the data is not output, only
> > the size.

> --nullfree           - Report any NULL characters in the data.
> --big-endian         - For "0x"-encoding/decoding, select big-endian over
> > instead of the default little-endian.

> --seperator=...      - A string of characters to be inserted between values
> --badchars=XX,XX,... - Report any of the characters supplied by hex value.

> --lowercase, --uppercase, --mixedcase, or --printable
> > - Report any non-lower-, upper-, or mixedcase
> > > alphanumeric or non-printable characters in the
> > > data. These options can be combined with both of
> > > these options:

> --latin-1            - Allow alphanumeric latin-1 high ascii characters.
> --cp437              - Allow alphanumeric cp437 high ascii characters.