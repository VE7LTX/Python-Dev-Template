# File: text_logging.py
# Description: Default functions for text control and logging using the re and logging libraries.

import re
import logging

# TODO: Implement function for extracting email addresses from text
def extract_emails(text):
    """
    Extracts email addresses from the given text.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

# TODO: Implement function for validating a phone number
def validate_phone_number(phone_number):
    """
    Validates the given phone number.
    """
    pattern = r'^\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    is_valid = re.match(pattern, phone_number)
    return is_valid is not None

# TODO: Implement function for logging an error message
def log_error(message):
    """
    Logs an error message.
    """
    logging.error(message)

# TODO: Implement function for logging a warning message
def log_warning(message):
    """
    Logs a warning message.
    """
    logging.warning(message)

# TODO: Implement function for logging an info message
def log_info(message):
    """
    Logs an info message.
    """
    logging.info(message)

# TODO: Implement function for logging a debug message
def log_debug(message):
    """
    Logs a debug message.
    """
    logging.debug(message)
