#!/usr/bin/python 

"""
A small module to display *something* when a python graphics program tries to
import a GUI module and can't.  At this point it wants to tell the user what
is wrong and maybe how to correct the problem.  But in some environments just
printing something to stderr doesn't work as there is no terminal to write
the text to.

This code tries to use the web browser to display error text.
"""

import os
import time
import tempfile
import webbrowser


def notify(msg, submsg='', html=''):
    """Tell the user something using the web browser.
    
    msg     the topline message
    submsg  optional submessage
    html    optional replacement HTML page text, formatted so:
                html.format(msg=msg, submsg=submsg)
    """

    # handle an HTML change
    if not html:
        html = '''<!DOCTYPE html>                                               
<html>                                                                           
    <body>                                                                       
        <center>                                                                 
            <h2>{msg}</h2>                                                       
            <h4>{submsg}</h4>                                                    
        </center>                                                                
    </body>                                                                      
</html>'''       

    # create a temporary *.HTML file containing the user message
    (fd, filename) = tempfile.mkstemp(suffix='.html', prefix='notify_')
    with open(filename, 'wb') as fd:
        fd.write(html.format(msg=msg, submsg=submsg))

    # display the message
    webbrowser.open('file:///' + filename, new=1)

    # remove the temporary file
    time.sleep(2)       # FUDGE: give browser time to load the file
    os.remove(filename)

if __name__ == '__main__':
    notify('''Sorry, can't find wxPython, you'll have to install it.''',
            '''You can get it <a href="http://www.wxpython.org/download.php">here</a>''')
