#!/usr/bin/env python
import os
import pathlib
script_location = pathlib.Path(__file__).parent.resolve()
os.environ["PATH"] += os.pathsep + str(script_location)
print('Scripts installed!')