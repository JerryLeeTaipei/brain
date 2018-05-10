#!/usr/local/bin/python3

import platform
# private modules
import eye

PYTHON_REQUIRED = '3.6'

class body:
    'platform dependent routines'
    dbg = 0
    info = {}
    parts = {}
    def __init__(self, dbg=0):
        self.info['machine'] = platform.machine()
        self.info['platform'] = platform.platform()
        self.info['system'] = platform.system()
        self.info['python'] = platform.python_version()
        self.dbg = dbg       
        if ( self.info['python'] < PYTHON_REQUIRED ):
            raise NameError("Not supported python" )
        return
    def attatchPart(self, name, part):
        self.parts[name] = part
        return
        
            
            

dbg = 1

# init everything    
try:
    body = body(dbg)
    # parts
    eyes = eye.eyes(dbg)
    body.attatchPart("EYE", eyes)    
    #brain = brain
except NameError:
    print("My defined exceptions!")
    raise
finally:
    print("Initialized")
