#!/usr/bin/python3
"""This module defines into a file-writing"""

def write_file(filename="", text=""):
    """Writes into a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

