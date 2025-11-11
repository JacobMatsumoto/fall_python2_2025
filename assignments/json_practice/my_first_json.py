"""
        !IMPORTANT FIND THIS
    "email": "james.brown@student.techacademy.edu",
    "room": "SH-205",
    "comment": "Excellent introduction to Python!",
    "price": 79.99
    "building": "Computer Lab",
"""

import json
import os
from pathlib import Path


def read_json_file(file_path):
    """Read and parse a JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {file_path}: {e}")
        return None
    except Exception as e:
        print(f"[ERROR] Error reading {file_path}: {e}")
        return None


def find_email_2(data, filename):
    """Expected path: school -> departments -> [0] -> courses -> [0] -> students -> [1] -> email"""
    email_2 = data['school']['departments'][0]['courses'][0]['students'][1]['email']
    print(f"email: {email_2}")


def find_room_num(data, filename):
    """Expected path: school -> departments -> [0] -> head -> office -> room"""
    room_num = data['school']['departments'][0]['head']['office']['room']
    print(f"room number: {room_num}")


def find_comment(data, filename):
    """Expected path: school -> library -> books -> [0] -> reviews -> [0] -> comment"""
    comment1 = data['school']['library']['books'][0]['reviews'][0]['comment']
    print(f"comment: {comment1}")


def find_price_book_2(data, filename):
    """Expected path: school -> library -> books -> [1] -> price"""
    book2_price = data['school']['library']['books'][1]['price']
    print(f"price: {book2_price}")


def find_event_2_building(data, filename):
    """Expected path: school -> events -> [1] -> location -> building"""
    building = data['school']['events'][1]['location']['building']
    print(f"event location: {building}")


def process_json_file(file_path):
    """Process a single JSON file and demonstrate its structure"""
    file_path = Path(__file__).parent / "examples" / "example7_assignment.json"
    filename = Path(file_path).name
    data = read_json_file(file_path)

    if data is None:
        return

    # Determine which demonstration function to use based on filename
    if 'example7' in filename:
        find_email_2(data, filename)
        find_room_num(data, filename)
        find_comment(data, filename)
        find_price_book_2(data, filename)
        find_event_2_building(data, filename)

process_json_file("example7_assignment.json")
