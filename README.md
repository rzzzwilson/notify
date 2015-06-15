# notify
A (hopefully) cross-platform method of notifying some sort of problem.

If you write a python GUI program that starts from a desktop icon or
a filemanager item you have a problem if the program cannot properly
initialise the GUI environment.  You can't **print** anything as there
is no terminal to show the error text.

My first attempt to solve this problem used the Tkinter module.  This is
part of python, so should always be there, right?  Ha!  Under Ubuntu the
Tkinter module is not installed automatically, you have to do:
```bash
sudo apt-get install python-tk
```
I believe that is also true under Mac OSX.

This current solution has a better chance of working on more platforms.
It definitely works under OSX.  It _should_ work under Linux.  Maybe it
works under Windows.  I'll test all those eventually.

To use it:
```python
import notify

notify.notify('''Sorry, can't find Python, you'll have to install it.''',         
              '''You can get it <a href="http://www.wxpython.org/download.php">here</a>''')
```

The notify() function has the signature:
```python
notify(msg, submsg='', html='')
```
The **msg** and **submsg** parameters are the error message(s).  The **html**
parameter allows the user to change the page HTML displayed in the browser.
The default HTML is:
```html
<!DOCTYPE html>                                               
<html>                                                                           
    <body>                                                                       
        <center>                                                                 
            <h2>{msg}</h2>                                                       
            <h4>{submsg}</h4>                                                    
        </center>                                                                
    </body>                                                                      
</html>                                                                          
```
