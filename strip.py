#!/usr/bin/python3

#
#   strip.py
#   march 2015
#   author: noda.yoshikazu@gmail.com
#
import sys, io, re
from html.parser import HTMLParser


#
# unescape all escapted.
# 
def unescape(s):
    global skipLine
    #print('in:',s)
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&amp;", "&")
    s = s.replace("&nbsp;&#038;", ' & ')
    s = s.replace("&nbsp;", " ")
    s = s.replace("&#32;", ' ')
    s = s.replace("&#36;", '$')
    s = s.replace("&#036;", '$')
    s = s.replace("&#38;", '&')
    s = s.replace("&#038;", '&')
    s = s.replace("&#043;", '+')

    s = s.replace("&#91;", '[')
    s = s.replace("&#091;", '[')
    s = s.replace("&#93;", ']')
    s = s.replace("&#093;", ']')
    s = s.replace("&#95;", '_')
    s = s.replace("&#095;", '_')
    s = s.replace("&#111;", u'o')

    s = s.replace("&#128;", u'€')

    s = s.replace("&#134;", ' ')
    s = s.replace("&#143;", ' ')
    s = s.replace("&#145;", '\'')
    s = s.replace("&#146;", '\'')
    s = s.replace("&#147;", u'“')  # left double
    s = s.replace("&#148;", u'”')
    s = s.replace("&#149;", u'•')
    s = s.replace("&#150;", u'-')
    s = s.replace("&#151;", u'—')
    s = s.replace("&#152;", u'˜')
    s = s.replace("&#153;", u'™')  #TM
    s = s.replace("&#155;", u'›')  
    s = s.replace("&#156;", u'œ')  

    s = s.replace("&#160;", ' ')
    s = s.replace("#160;", ' ')  # sick
    s = s.replace("&#161;", u'¡')
    s = s.replace("&#162;", u'¢')  # cent
    s = s.replace("&#163;", u'#')
    s = s.replace("&#164;", u'¤')
    s = s.replace("&#165;", u'¥')
    s = s.replace("&#166;", u'|')
    s = s.replace("&#167;", u'§')  # section
    s = s.replace("&#168;", u'y')
    s = s.replace("&#169;", u'©')
    s = s.replace("&#170;", u'ª')
    s = s.replace("&#171;", u'«')
    s = s.replace("&#172;", u'¬')
    s = s.replace("&#173;", '-')
    s = s.replace("&#174;", u'®')  # registered
    s = s.replace("&#175;", u'¯')
    s = s.replace("&#176;", u'°')  # degree
    s = s.replace("&#177;", u'±')
    s = s.replace("&#178;", '[sup2]')
    s = s.replace("&#179;", '[sup3]')
    s = s.replace("&#180;", '[acute]')
    s = s.replace("&#181;", u'µ')
    s = s.replace("&#182;", u'¶')
    s = s.replace("&#183;", u'·')
    s = s.replace("&#184;", u'¸')
    s = s.replace("&#185;", '[sup1]')
    s = s.replace("&#186;", u'º')
    s = s.replace("&#187;", u'»')
    s = s.replace("&#188;", u'¼')
    s = s.replace("&#189;", u'½')
    s = s.replace("&#190;", u'¾')
    s = s.replace("&#191;", u'¿')
    s = s.replace("&#192;", u'À')
    s = s.replace("&#193;", u'Á')

    # 192 ~ latin characters
    s = s.replace("&#201;", u'É')  # latin 
    s = s.replace("&eacute;", u'É')  # latin b.s.
    s = s.replace("&#205;", u'Í')  # latin 
    s = s.replace("&#215;", u'×')  # latin 
    s = s.replace("&#220;", u'Ü')  # latin 
    s = s.replace("&#221;", u'Ý')  # latin 
    s = s.replace("&#222;", u'Þ')  # latin 
    s = s.replace("&#223;", u'ß')  # latin 
    s = s.replace("&#224;", u'à')  # latin 
    s = s.replace("&#225;", u'á')  # latin 
    s = s.replace("&#226;", u'â')  # latin 
    s = s.replace("&#227;", u'ã')  # latin 
    s = s.replace("&#228;", u'ä')  # latin 
    s = s.replace("&#229;", u'å')  # latin 
    s = s.replace("&#230;", u'æ')  # latin 
    s = s.replace("&#231;", u'ç')  # latin 
    s = s.replace("&#232;", u'è')  # latin 
    s = s.replace("&#233;", u'é')  # latin 
    s = s.replace("&#234;", u'ê')  # latin 
    s = s.replace("&#235;", u'ë')  # latin 
    s = s.replace("&#236;", u'ì')  # latin 

    s = s.replace("&#237;", u'í')  # latin 
    s = s.replace("&#238;", u'î')  # latin 
    s = s.replace("&#239;", u'ï')  # latin 
    s = s.replace("&#240;", u'ð')  # latin 
    s = s.replace("&#241;", u'ñ')  # latin 
    s = s.replace("&#242;", u'ò')  # latin 
    s = s.replace("&#243;", u'ó')  # latin 
    s = s.replace("&#244;", u'ô')  # latin 
    s = s.replace("&#245;", u'õ')  # latin 
    s = s.replace("&#246;", u'ö')  # latin 
    s = s.replace("&#247;", u'÷')
    s = s.replace("&#248;", u'ø')

    s = s.replace("&#249;", u'ù')  # latin 
    s = s.replace("&#250;", u'ú')  # latin 
    s = s.replace("&#251;", u'û')  # latin 
    s = s.replace("&#252;", u'ü')  # latin 

    s = s.replace("&#253;", u'ý')  # latin y acute
    s = s.replace("&#254;", u'þ')  # latin thorn small
    s = s.replace("&#255;", u'ÿ')  # latin thorn small

    s = s.replace("&#8209;", u'-')  # non breaking hyphen
    s = s.replace("&#8211;", u'-')  # hyphen
    s = s.replace("#8211;",  u'-')   # sick hyphen
    s = s.replace("&#8212;", u'--')  # hyphen
    s = s.replace("&#8216;", u'‘')  # apostrophe
    s = s.replace("&#8217;", u'’')  # apostrophe
    s = s.replace("&#8220;", u'\"')  # 
    s = s.replace("&#8221;", u'\"')  # 
    s = s.replace("&#8224;", u'†')  # 
    s = s.replace("&#8225;", u'‡')  # 
    s = s.replace("&#8226;", u'•')  # 
    s = s.replace("&#8230;", u'…')  # 
    s = s.replace("&#8240;", u'‰')  # 
    s = s.replace("&#8264;", u'€')  # 
    s = s.replace("&#8364;", u'€')  # 
    s = s.replace("&#8482;", u'™')  # 
    s = s.replace("&#8722;", u'-')  # 
    s = s.replace("&#8804;", u'≦')  # 
    s = s.replace("&#8805;", u'≧')  # 
    s = s.replace("&#9679;", u'●')  # 

    # this has to be last:
    s = re.sub('&#[0-9]+;', '[???]', s)  # unknow
    s = re.sub('&#xd;', '\n', s)
    s = re.sub('&#xA0;', ' ', s)
    s = re.sub('#xA0;', ' ', s)
    s = s.replace("&#x2013;", u'-') 
    s = s.replace("&#x2014;", u'-') 
    s = s.replace("&#x2019;", u'\'') 
    s = s.replace("&#x201C;", u'"') 
    s = s.replace("&#x201D;", u'"') 
    s = s.replace("&#x20AC;", u'€') 
    s = re.sub('&#x[0-9A-F]+;', '[x???]', s)  # unknow
    s = s.replace("&#150;", u'-')
    s = s.replace("&rsquo;", u'\'')
    s = s.replace("&lsquo;", u'\'')
    s = s.replace("&rdquo;", u'"')
    s = s.replace("&ldquo;", u'"')

    #print('out:',s)
    return s


#
# Removes HTML markup
#
def remove_markup(file_obj):
    tag = False
    quote = False
    amp = False
    out = ""
    skip_till_semi = False
    skip = False
    tagname = ''
    closetag = False

    for line in file_obj:
        if line.startswith('begin 644') :
            skip = True  # Binary data
        elif line.startswith('<XBRL>') :
            skip = True   # Can't handle XBRL so we remove XMRL data
        elif line.startswith('</XBRL>') :
            skip = False  # End XBRL
        elif skip :
            # line with "end" to end binary data
            if re.match('^end$', line) != None :
                skip = False
        else :
            line = unescape(line)
            ignoreall = False
            i = 0
            otmp = ''
            for c in line:
                i += 1
                #  js snippet removal
                if tagname.startswith('scri') :
                    ignoreall = True
                elif tagname.startswith('/scri') :
                    ignoreall = False
                        
                if c == '<' and not quote:
                    tag = True
                    tagname = ''  # init tagname
                elif c == '/' and prevchar == '<':
                    closetag = True
                elif c == '>' and not quote:
                    tag = False
                    #if 0 < len(otmp) and re.match('^[ \t]*$', otmp) == None :  # No need when the line is empty
                    #    print('['+otmp+']')
                    #print('tagname={}'.format(tagname))
                    #if tagname.startswith('TR') :
                    #    otmp = otmp + '\n'
                    if closetag == True :
                        otmp = otmp + '\n'
                        closetag = False
                elif (c == '"' or c == "'") and tag:
                    quote = not quote
                elif not tag:
                    if not ignoreall :
                        if c != '\n' :   # So a newline between tag content will be removed
                            otmp = otmp + c
                elif tag :
                    tagname += c
                prevchar = c

            # Skip blank lines
            #if len(otmp) > 0  and not re.match('^[ \t\r\n]*$', otmp) :
            if len(otmp) > 0 :
                out += otmp
    return out

if __name__ == "__main__":
    opt = sys.argv[1]
    print('stripping ',opt)
    with open(opt, 'rt') as f:
        dat = remove_markup(f)
        
        outfile = re.sub('\.txt$', '_raw.txt', opt)
        #print(outfile)
        of = open(outfile, 'wt')
        of.write(dat)
        of.close()
        #print(dat)

