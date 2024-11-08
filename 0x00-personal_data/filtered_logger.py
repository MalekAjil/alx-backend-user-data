#!/usr/bin/env python3
"""filtered_logger"""
from typing import List
import logging
import re


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
    pattern = f"({'|'.join(fields)})=([^\\{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
