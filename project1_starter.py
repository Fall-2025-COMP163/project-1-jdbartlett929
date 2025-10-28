"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Julian Bartlett]
Date: [10/27/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
global VALID_CLASSES, RULES
import os

VALID_CLASSES = {"Warrior", "Mage", "Rogue", "Cleric"}

RULES = {
    "Warrior": {"STR_BASE": 8, "STR_GROW": 3, "MAG_BASE": 1,  "MAG_GROW": 1, "HP_BASE": 85, "HP_GROW": 12, "GOLD": 75},
    "Mage":    {"STR_BASE": 5, "STR_GROW": 1, "MAG_BASE": 15, "MAG_GROW": 3, "HP_BASE": 80, "HP_GROW": 8,  "GOLD": 100},
    "Rogue":   {"STR_BASE": 7, "STR_GROW": 2, "MAG_BASE": 7,  "MAG_GROW": 2, "HP_BASE": 65, "HP_GROW": 7,  "GOLD": 90},
    "Cleric":  {"STR_BASE": 6, "STR_GROW": 2, "MAG_BASE": 12, "MAG_GROW": 3, "HP_BASE": 85, "HP_GROW": 10, "GOLD": 110},
}

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    
    if character_class not in VALID_CLASSES:
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = RULES[character_class]["GOLD"]

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold,
    }

    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    if character_class not in VALID_CLASSES:
        return (0, 0, 0)

    r = RULES[character_class]
    strength = r["STR_BASE"] + level * r["STR_GROW"]
    magic    = r["MAG_BASE"] + level * r["MAG_GROW"]
    health   = r["HP_BASE"]  + level * r["HP_GROW"]
    return (strength, magic, health)

    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    folder = os.path.dirname(filename) or "."
    can_write_dir = os.access(folder, os.W_OK)
    can_write_file = os.path.exists(filename) and os.access(filename, os.W_OK)
    if not (can_write_dir or can_write_file):
        return False

    f = open(filename, "w")
    f.write(f"Character Name: {character['name']}\n\n")
    f.write(f"Class: {character['class']}\n\n")
    f.write(f"Level: {character['level']}\n\n")
    f.write(f"Strength: {character['strength']}\n\n")
    f.write(f"Magic: {character['magic']}\n\n")
    f.write(f"Health: {character['health']}\n\n")
    f.write(f"Gold: {character['gold']}\n")
    f.close()
    return True

    
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.isfile(filename):
        return None
    f = open(filename, "r")
    raw = f.readlines()
    f.close()
    lines = [ln.strip() for ln in raw if ln.strip() != ""]
    if len(lines) != 7:
        return None
    parts = [ln.split(": ", 1) for ln in lines]
    labels = [p[0] for p in parts]
    values = [p[1] if len(p) > 1 else "" for p in parts]
    expected = ["Character Name", "Class", "Level", "Strength", "Magic", "Health", "Gold"]
    if labels != expected:
        return None
    name = values[0]
    character_class = values[1]
    if character_class not in VALID_CLASSES:
        return None
    level    = int(values[2])
    strength = int(values[3])
    magic    = int(values[4])
    health   = int(values[5])
    gold     = int(values[6])
    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold,
    }
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character["level"] = character["level"] + 1
    s, m, h = calculate_stats(character["class"], character["level"])
    character["strength"] = s
    character["magic"] = m
    character["health"] = h

    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
