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

__version__ = '0.3'


def notify(msg, submsg='', html='', header=None):
    """Tell the user something using the web browser.

    msg     the topline message
    submsg  optional submessage
    html    optional replacement HTML page text, formatted so:
                html.format(msg=msg, submsg=submsg)
    """

    # create the user content
    if not html:
        html = '''<center><h2>{msg}</h2><h4>{submsg}</h4></center>'''
    html = html.format(msg=msg, submsg=submsg)

    if not header:
        header = 'ERROR'

    # construct the page contents
    body_top = '''<!DOCTYPE html>
<html>
    <title>{header}</title>
    <style>
        div {lcurly}
             border-radius: 5px 20px;
             background: #99FFEE;
             padding: 15px 30px 2px 30px;
             width: 800px;
            {rcurly}
        footer {lcurly}
                   font-size: 5px;
               {rcurly}
    </style>
    <body>
        <div>
'''.format(header=header, lcurly='{', rcurly='}') 

    body_bot = '''
            <footer>
            <p align="right"><font size="1">{progname} v{version}</font></p>
            </footer>
        </div>
    </body>
</html>'''.format(progname=notify.__name__, version=__version__)

    # create a temporary *.HTML file containing the user message
    (fd, filename) = tempfile.mkstemp(suffix='.html', prefix='notify_')
    with open(filename, 'wb') as fd:
        fd.write(body_top + html + body_bot)

    # display the message
    webbrowser.open_new('file:///' + filename)

    # remove the temporary file
    time.sleep(2)       # FUDGE: give browser time to load the file
    os.remove(filename) #        before we delete it!


if __name__ == '__main__':
    try:
        import not_found
    except ImportError:
        notify('''Sorry, can't find the 'not_found' module, '''
                '''you'll have to install it.''',
                '''You can get it <a href="http://www.example.com">here</a>''',
                header='WARNING', html='<h2>{msg}</h2><h4>{submsg}</h4>')
