#!/usr/bin/env python3
"""filtered_logger"""
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """returns the log message obfuscated
    Arguments:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all
    fields in the log line (message)
    """
    #logging.basicConfig(filename='myfile', level=logging.INFO)
    loger.info()
