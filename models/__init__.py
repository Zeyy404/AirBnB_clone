#!/usr/bin/python3
"""Python Package initializing file"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
