import os
from datetime import datetime
from slugify import slugify
import secrets

UPLOAD_FILES = os.path.abspath("./app/static/data/files")


def compare_time(date_string):
    try:
        current_date = datetime.now()
        specific_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
        time_difference = current_date - specific_datetime

        if time_difference.days == 0:
            return specific_datetime.strftime("%H:%M")
        elif time_difference.days == 1:
            return "Yesterday"
        elif time_difference <= 7:
            return specific_datetime.strftime("%A")
        else:
            return specific_datetime.strftime("%d %A %Y")
    except ValueError:
        return "Invalid Date"


def get_time():
    try:
        return str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    except Exception as e:
        print(f"Error getting time: {e}")
        return "Error"


def key(length=10):
    characters = "ABCDEF-GHIJKLMNO-PQRSTUVWX-YZabcdef-ghijklm-nopqrstu-vwxyz12345-67890"
    return "".join(secrets.choice(characters) for _ in range(length))


def create_slug(file_name):
    return slugify(file_name)

