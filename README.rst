notify
======

A (hopefully) cross-platform method of notifying some sort of problem for
python 2 and 3.

If you write a python GUI program that starts from a desktop icon or
a filemanager item you have a problem if the program cannot properly
initialise the GUI environment.  You can't raise any sort of dialog to
warn the user and you can't **print** anything as there is no terminal to
show the error text.  This often shows up in the /r/learnpython subreddit
as a problem where "I double-click, a windows flashes up and is immediately
gone" problem.  There should be some cross-platform way of indicating errors.

My first attempt to solve this problem
`used the Tkinter module <https://github.com/rzzzwilson/notify/blob/master/tkinter_notify.py>`_.
This is part of python, so should always be there, right?  Ha!  Under Ubuntu the
Tkinter module is not installed automatically, you have to do:

::

    sudo apt-get install python-tk

I believe that is also the case under Mac OSX.

This current solution has a better chance of working on more platforms.
It definitely works under OSX.  It works under Ubuntu.  Maybe it
works under other Linuxes and Windows.  I'll test all those eventually.

To use it:

::

    import notify
    
    notify.notify('''Sorry, can't find WxPython, you'll have to install it.''',         
                  '''You can get it <a href="http://www.wxpython.org/download.php">here</a>''')

The notify() function has the signature:

::

    notify(msg, submsg=None, html=None, header=None, colour=None)

The **msg** and **submsg** parameters are the error message(s).  The **html**
parameter allows the user to change the page HTML displayed in the browser.
The default HTML is:

::

    <center>
        <h2>{msg}</h2>                                                       
        <h4>{submsg}</h4>                                                    
    </center>

You may substitute any HTML you prefer remembering that the supplied HTML may
use the **msg** and **submsg** slots for formatting and no others.  Also
remember that the supplied HTML is embedded inside a ``<div>`` in the HTML
body.

The **header** parameter allows the user to change the tab header text.
The default header is "ERROR".

The **colour** parameter lets the user set the colour of the message box.
The default colour is "#ffb8b8".

Testing
-------

If you execute either of these commands:

::

    python notify.py
    python3 notify.py

you will see these two tabs appear in the default browser:

An ERROR tab:

.. image:: ERROR.png

And a WARNING tab:

.. image:: WARNING.png

