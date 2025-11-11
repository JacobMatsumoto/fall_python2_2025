"""
JSON Reader Examples
Reads JSON files and demonstrates accessing various JSON data types and nested structures.
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


def get_json_type(value):
    """Get a human-readable type name for a JSON value"""
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "number (integer)"
    elif isinstance(value, float):
        return "number (float)"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, dict):
        return "object"
    elif isinstance(value, list):
        return "array"
    else:
        return str(type(value).__name__)


def demonstrate_simple_object(data, filename):
    """Demonstrate accessing a simple object with primitive types"""
    print("\n" + "=" * 70)
    print(f"EXAMPLE 1: Simple Object - {filename}")
    print("=" * 70)
    
    print("\n[STRUCTURE] Overview:")
    print(f"   Type: {get_json_type(data)}")
    print(f"   Keys: {list(data.keys())}")
    
    print("\n[ACCESS] Accessing Different Data Types:")
    
    # String
    if 'name' in data:
        print(f"\n   String:")
        print(f"      data['name'] = {repr(data['name'])}")
        print(f"      Type: {get_json_type(data['name'])}")
    
    # Integer
    if 'age' in data:
        print(f"\n   Number (Integer):")
        print(f"      data['age'] = {data['age']}")
        print(f"      Type: {get_json_type(data['age'])}")
    
    # Float
    if 'height' in data:
        print(f"\n   Number (Float):")
        print(f"      data['height'] = {data['height']}")
        print(f"      Type: {get_json_type(data['height'])}")
    
    # Boolean
    if 'isStudent' in data:
        print(f"\n   Boolean:")
        print(f"      data['isStudent'] = {data['isStudent']}")
        print(f"      Type: {get_json_type(data['isStudent'])}")
    
    # Null
    if 'phoneNumber' in data:
        print(f"\n   Null:")
        print(f"      data['phoneNumber'] = {data['phoneNumber']}")
        print(f"      Type: {get_json_type(data['phoneNumber'])}")


def demonstrate_arrays(data, filename):
    """Demonstrate accessing arrays"""
    print("\n" + "=" * 70)
    print(f"EXAMPLE 2: Arrays - {filename}")
    print("=" * 70)
    
    print("\n[STRUCTURE] Overview:")
    print(f"   Type: {get_json_type(data)}")
    print(f"   Keys: {list(data.keys())}")
    
    print("\n[ACCESS] Accessing Array Elements:")
    
    # Array of strings
    if 'fruits' in data:
        print(f"\n   Array of Strings:")
        print(f"      data['fruits'] = {data['fruits']}")
        print(f"      Type: {get_json_type(data['fruits'])}")
        print(f"      Length: {len(data['fruits'])}")
        print(f"      First element: data['fruits'][0] = {repr(data['fruits'][0])}")
        print(f"      Last element: data['fruits'][-1] = {repr(data['fruits'][-1])}")
    
    # Array of numbers
    if 'numbers' in data:
        print(f"\n   Array of Numbers:")
        print(f"      data['numbers'] = {data['numbers']}")
        print(f"      Type: {get_json_type(data['numbers'])}")
        print(f"      First element: data['numbers'][0] = {data['numbers'][0]}")
        print(f"      Second element: data['numbers'][1] = {data['numbers'][1]}")
    
    # Mixed array
    if 'mixedArray' in data:
        print(f"\n   Mixed Type Array:")
        print(f"      data['mixedArray'] = {data['mixedArray']}")
        for i, item in enumerate(data['mixedArray']):
            print(f"      data['mixedArray'][{i}] = {repr(item)} (Type: {get_json_type(item)})")
    
    # Nested arrays
    if 'nestedArrays' in data:
        print(f"\n   Nested Arrays:")
        print(f"      data['nestedArrays'] = {data['nestedArrays']}")
        print(f"      First nested array: data['nestedArrays'][0] = {data['nestedArrays'][0]}")
        print(f"      Access nested element: data['nestedArrays'][0][1] = {data['nestedArrays'][0][1]}")


def demonstrate_nested_objects(data, filename):
    """Demonstrate accessing nested objects"""
    print("\n" + "=" * 70)
    print(f"EXAMPLE 3: Nested Objects - {filename}")
    print("=" * 70)
    
    print("\n[STRUCTURE] Overview:")
    print(f"   Type: {get_json_type(data)}")
    print(f"   Top-level keys: {list(data.keys())}")
    
    print("\n[ACCESS] Accessing Nested Properties:")
    
    # One level deep
    if 'user' in data and 'profile' in data['user']:
        print(f"\n   One Level Deep:")
        print(f"      data['user']['profile'] = {type(data['user']['profile'])}")
    
    # Two levels deep
    if 'user' in data and 'profile' in data['user'] and 'personal' in data['user']['profile']:
        print(f"\n   Two Levels Deep:")
        print(f"      data['user']['profile']['personal'] = {data['user']['profile']['personal']}")
        if 'firstName' in data['user']['profile']['personal']:
            print(f"      data['user']['profile']['personal']['firstName'] = {repr(data['user']['profile']['personal']['firstName'])}")
    
    # Three levels deep
    if 'user' in data and 'profile' in data['user'] and 'contact' in data['user']['profile']:
        if 'address' in data['user']['profile']['contact']:
            print(f"\n   Three Levels Deep:")
            print(f"      data['user']['profile']['contact']['address'] = {data['user']['profile']['contact']['address']}")
            if 'city' in data['user']['profile']['contact']['address']:
                print(f"      data['user']['profile']['contact']['address']['city'] = {repr(data['user']['profile']['contact']['address']['city'])}")
    
    # Settings access
    if 'user' in data and 'settings' in data['user']:
        print(f"\n   Settings Object:")
        print(f"      data['user']['settings'] = {data['user']['settings']}")
        if 'theme' in data['user']['settings']:
            print(f"      data['user']['settings']['theme'] = {repr(data['user']['settings']['theme'])}")


def demonstrate_array_of_objects(data, filename):
    """Demonstrate accessing arrays containing objects"""
    print("\n" + "=" * 70)
    print(f"EXAMPLE 4: Array of Objects - {filename}")
    print("=" * 70)
    
    print("\n[STRUCTURE] Overview:")
    print(f"   Type: {get_json_type(data)}")
    print(f"   Keys: {list(data.keys())}")
    
    print("\n[ACCESS] Accessing Array Elements and Their Properties:")
    
    # Students array
    if 'students' in data:
        print(f"\n   Students Array:")
        print(f"      data['students'] = Array with {len(data['students'])} items")
        print(f"      Type: {get_json_type(data['students'])}")
        
        if len(data['students']) > 0:
            print(f"\n   First Student Object:")
            first_student = data['students'][0]
            print(f"      data['students'][0] = {first_student}")
            print(f"      Access properties:")
            if 'name' in first_student:
                print(f"         data['students'][0]['name'] = {repr(first_student['name'])}")
            if 'age' in first_student:
                print(f"         data['students'][0]['age'] = {first_student['age']}")
            if 'courses' in first_student:
                print(f"         data['students'][0]['courses'] = {first_student['courses']}")
        
        if len(data['students']) > 1:
            print(f"\n   Second Student Object:")
            second_student = data['students'][1]
            if 'name' in second_student:
                print(f"      data['students'][1]['name'] = {repr(second_student['name'])}")
    
    # Products array
    if 'products' in data:
        print(f"\n   Products Array:")
        print(f"      data['products'] = Array with {len(data['products'])} items")
        if len(data['products']) > 0:
            first_product = data['products'][0]
            print(f"      First product:")
            if 'name' in first_product:
                print(f"         data['products'][0]['name'] = {repr(first_product['name'])}")
            if 'price' in first_product:
                print(f"         data['products'][0]['price'] = {first_product['price']}")


def demonstrate_complex_nested(data, filename):
    """Demonstrate accessing complex nested structures"""
    print("\n" + "=" * 70)
    print(f"EXAMPLE 5: Complex Nested Structure - {filename}")
    print("=" * 70)
    
    print("\n[STRUCTURE] Overview:")
    print(f"   Type: {get_json_type(data)}")
    print(f"   Top-level keys: {list(data.keys())}")
    
    print("\n[ACCESS] Accessing Complex Nested Data:")
    
    # Access nested array of objects
    if 'data' in data and 'users' in data['data']:
        print(f"\n   Nested Array of Objects:")
        print(f"      data['data']['users'] = Array with {len(data['data']['users'])} items")
        
        if len(data['data']['users']) > 0:
            user = data['data']['users'][0]
            print(f"      First user:")
            print(f"         data['data']['users'][0]['username'] = {repr(user.get('username', 'N/A'))}")
            
            # Nested object within array element
            if 'profile' in user:
                print(f"\n   Nested Object in Array Element:")
                print(f"         data['data']['users'][0]['profile'] = {user['profile']}")
                if 'displayName' in user['profile']:
                    print(f"         data['data']['users'][0]['profile']['displayName'] = {repr(user['profile']['displayName'])}")
            
            # Nested object with nested objects
            if 'preferences' in user and 'notifications' in user['preferences']:
                print(f"\n   Deeply Nested Object:")
                print(f"         data['data']['users'][0]['preferences']['notifications'] = {user['preferences']['notifications']}")
                if 'email' in user['preferences']['notifications']:
                    print(f"         data['data']['users'][0]['preferences']['notifications']['email'] = {user['preferences']['notifications']['email']}")
            
            # Array within object within array
            if 'posts' in user and len(user['posts']) > 0:
                print(f"\n   Array Within Object Within Array:")
                print(f"         data['data']['users'][0]['posts'] = Array with {len(user['posts'])} items")
                first_post = user['posts'][0]
                if 'title' in first_post:
                    print(f"         data['data']['users'][0]['posts'][0]['title'] = {repr(first_post['title'])}")
                
                # Array within object within array within object
                if 'comments' in first_post and len(first_post['comments']) > 0:
                    print(f"\n   Multiple Levels of Nesting:")
                    print(f"         data['data']['users'][0]['posts'][0]['comments'] = Array with {len(first_post['comments'])} items")
                    first_comment = first_post['comments'][0]
                    if 'text' in first_comment:
                        print(f"         data['data']['users'][0]['posts'][0]['comments'][0]['text'] = {repr(first_comment['text'])}")
    
    # Metadata access
    if 'data' in data and 'metadata' in data['data']:
        print(f"\n   Metadata Object:")
        print(f"      data['data']['metadata'] = {data['data']['metadata']}")


def demonstrate_mixed_types(data, filename):
    """Demonstrate accessing mixed/complex real-world structure"""
    print("\n" + "=" * 70)
    print(f"EXAMPLE 6: Mixed Types - Real-World Example - {filename}")
    print("=" * 70)
    
    print("\n[STRUCTURE] Overview:")
    print(f"   Type: {get_json_type(data)}")
    if isinstance(data, dict):
        print(f"   Top-level keys: {list(data.keys())}")
    
    print("\n[ACCESS] Accessing Mixed Structure:")
    
    # Store name
    if 'store' in data and 'name' in data['store']:
        print(f"\n   Simple String Value:")
        print(f"      data['store']['name'] = {repr(data['store']['name'])}")
    
    # Nested location with coordinates
    if 'store' in data and 'location' in data['store']:
        print(f"\n   Nested Location Object:")
        location = data['store']['location']
        if 'city' in location:
            print(f"      data['store']['location']['city'] = {repr(location['city'])}")
        if 'coordinates' in location:
            print(f"      data['store']['location']['coordinates'] = {location['coordinates']}")
            if 'latitude' in location['coordinates']:
                print(f"      data['store']['location']['coordinates']['latitude'] = {location['coordinates']['latitude']}")
    
    # Categories array
    if 'store' in data and 'categories' in data['store']:
        print(f"\n   Categories Array:")
        categories = data['store']['categories']
        print(f"      data['store']['categories'] = Array with {len(categories)} items")
        
        if len(categories) > 0:
            first_category = categories[0]
            print(f"\n   First Category:")
            if 'name' in first_category:
                print(f"      data['store']['categories'][0]['name'] = {repr(first_category['name'])}")
            
            # Products within category
            if 'products' in first_category and len(first_category['products']) > 0:
                print(f"\n   Products in First Category:")
                first_product = first_category['products'][0]
                if 'name' in first_product:
                    print(f"      data['store']['categories'][0]['products'][0]['name'] = {repr(first_product['name'])}")
                
                # Specifications nested object
                if 'specifications' in first_product:
                    print(f"\n   Product Specifications:")
                    specs = first_product['specifications']
                    print(f"      data['store']['categories'][0]['products'][0]['specifications'] = {specs}")
                    if 'processor' in specs:
                        print(f"      data['store']['categories'][0]['products'][0]['specifications']['processor'] = {repr(specs['processor'])}")
                
                # Reviews array within product
                if 'reviews' in first_product:
                    print(f"\n   Product Reviews Array:")
                    reviews = first_product['reviews']
                    print(f"      data['store']['categories'][0]['products'][0]['reviews'] = Array with {len(reviews)} items")
                    if len(reviews) > 0:
                        first_review = reviews[0]
                        if 'rating' in first_review:
                            print(f"      data['store']['categories'][0]['products'][0]['reviews'][0]['rating'] = {first_review['rating']}")
                        if 'comment' in first_review:
                            print(f"      data['store']['categories'][0]['products'][0]['reviews'][0]['comment'] = {repr(first_review['comment'])}")
    
    # Hours object with null value
    if 'store' in data and 'hours' in data['store']:
        print(f"\n   Hours Object (with null value):")
        hours = data['store']['hours']
        print(f"      data['store']['hours'] = {hours}")
        if 'sunday' in hours:
            print(f"      data['store']['hours']['sunday'] = {hours['sunday']} (Type: {get_json_type(hours['sunday'])})")
    
    # Stats object
    if 'store' in data and 'stats' in data['store']:
        print(f"\n   Stats Object:")
        stats = data['store']['stats']
        print(f"      data['store']['stats'] = {stats}")
        if 'averageRating' in stats:
            print(f"      data['store']['stats']['averageRating'] = {stats['averageRating']} (Type: {get_json_type(stats['averageRating'])})")
        if 'isOpen' in stats:
            print(f"      data['store']['stats']['isOpen'] = {stats['isOpen']} (Type: {get_json_type(stats['isOpen'])})")


def process_json_file(file_path):
    """Process a single JSON file and demonstrate its structure"""
    filename = os.path.basename(file_path)
    data = read_json_file(file_path)
    
    if data is None:
        return
    
    # Determine which demonstration function to use based on filename
    if 'example1' in filename:
        demonstrate_simple_object(data, filename)
    elif 'example2' in filename:
        demonstrate_arrays(data, filename)
    elif 'example3' in filename:
        demonstrate_nested_objects(data, filename)
    elif 'example4' in filename:
        demonstrate_array_of_objects(data, filename)
    elif 'example5' in filename:
        demonstrate_complex_nested(data, filename)
    elif 'example6' in filename:
        demonstrate_mixed_types(data, filename)
    else:
        # Generic demonstration for unknown files
        print(f"\n{'=' * 70}")
        print(f"Processing: {filename}")
        print("=" * 70)
        print(f"\nJSON Structure:")
        print(json.dumps(data, indent=2))


def main():
    """Main function to process all JSON example files"""
    print("=" * 70)
    print("JSON Reader Examples")
    print("Demonstrating JSON Data Types and Nested Structures")
    print("=" * 70)
    
    # Get the examples directory path
    examples_dir = Path(__file__).parent / "examples"
    
    if not examples_dir.exists():
        print(f"\n[ERROR] Examples directory not found: {examples_dir}")
        print("   Please create the 'examples' directory with JSON files.")
        return
    
    # Find all JSON files in the examples directory
    json_files = sorted(examples_dir.glob("*.json"))
    
    if not json_files:
        print(f"\n[ERROR] No JSON files found in {examples_dir}")
        return
    
    print(f"\n[OK] Found {len(json_files)} JSON file(s) in examples directory")
    print("\nProcessing files...")
    
    # Process each JSON file
    for json_file in json_files:
        process_json_file(json_file)
    
    print("\n" + "=" * 70)
    print("[OK] All files processed!")
    print("=" * 70)


if __name__ == "__main__":
    main()

