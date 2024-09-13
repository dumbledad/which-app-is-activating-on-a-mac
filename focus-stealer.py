#!/usr/bin/python
# Copied from https://superuser.com/a/874314/166855                                                                                                  

try:
    from AppKit import NSWorkspace
except ImportError:
    print("Can't import AppKit -- try `pip install PyObjC`")
    print("(see instructions for running in a venv with PyObjC)")
    exit(1)

from datetime import datetime
from time import sleep

last_active_name = None
while True:
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    if active_app['NSApplicationName'] != last_active_name:
        last_active_name = active_app['NSApplicationName']
        print('%s: %s [%s]' % (
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            active_app['NSApplicationName'],
            active_app['NSApplicationPath']
        ))
    sleep(1)
