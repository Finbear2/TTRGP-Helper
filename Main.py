import random
from random import *

Character_Amount = 0

class Character:
    
    def __init__(Self, Name, Class, Level, Background, Race, Alignment, Size, Human, Stats, Armor_Class, Initiative, Speed, Hit_Points, Hit_Dice, Proficiency_Bonus, Saving_Throws, Equipment, Spells, Inventory, Coin, Backstory, Traits, Features, Languages, Notes):
        
        global Character_Amount
        
        Self.Name = Name
        Self.Class = Class
        Self.Level = Level
        Self.Background = Background
        Self.Race = Race
        Self.Alignment = Alignment
        Self.Size = Size
        Self.Human = Human
        
        Self.Strength = Stats["Strength"]
        Self.Dexterity = Stats["Dexterity"]
        Self.Constitution = Stats["Constitution"]
        Self.Intelligence = Stats["Intelligence"]
        Self.Wisdom = Stats["Wisdom"]
        Self.Charisma = Stats["Charisma"]
        
        Character_Amount += 1
        Self.ID = Character_Amount
 
def Create_Stats( Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma ):
    
    return {
        "Strength": Strength + 10,
        "Dexterity": Dexterity + 10,
        "Constitution": Constitution + 10,
        "Intelligence": Intelligence + 10,
        "Wisdom": Wisdom + 10,
        "Charisma": Charisma + 10
    }
    
def Create_Saving_Rolls( Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, Class, Prof_Bonus):
    
    if any( c in Class for c in ["Barbarian","Fighter"] ):
        Strength += Prof_Bonus; Dexterity += Prof_Bonus
    elif any( c in Class for c in ["Bard", "Rogue"] ):
        Dexterity += Prof_Bonus; Charisma += Prof_Bonus
    elif any( c in Class for c in ["Cleric", "Paladin", "Warlock"] ):
        Wisdom += Prof_Bonus; Charisma += Prof_Bonus
    elif any( c in Class for c in ["Druid", "Wizard"] ):
        Intelligence += Prof_Bonus; Wisdom += Prof_Bonus
    elif any( c in Class for c in ["Monk", "Ranger"] ):
        Dexterity += Prof_Bonus; Wisdom += Prof_Bonus
    else:
        Strength += Prof_Bonus; Constitution += Prof_Bonus
        
    return {
        "Strength": Strength,
        "Dexterity": Dexterity,
        "Constitution": Constitution,
        "Intelligence": Intelligence,
        "Wisdom": Wisdom,
        "Charisma": Charisma
    }
       
def Quick_Character(Name, Class, Level, Race, Size, HP, Hit_Dice):
    
    Strength = randint(-1,3); Dexterity = randint(-1,3); Constitution = randint(-1,3); Intelligence = randint(-1,3); Wisdom = randint(-1,3); Charisma = randint(-1,3)
    
    Speed = None
    
    if any( r in Race for r in ["Human", "Elf", "Tiefling", "Tabaxi"]):
        Speed = 30
    elif any( r in Race for r in ["Dwarf", "Gnome", "Halfling"]):
        Speed = 25
    else:
        Speed = 40
    
    return Character(Name, Class, Level, "None", Race, Alignment, Size, "None",
                     Create_Stats(randint(-1,3),Dexterity,randint(-1,3),randint(-1,3),randint(-1,3),randint(-1,3) ),
                     10 + Dexterity, Dexterity, Speed, HP, Hit_Dice, 2 + (Level - 1) // 4,
                     Create_Saving_Rolls(Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma,Class,2 + (Level - 1) // 4),
                     "None", "None", "None", "None", "None", "None", "None", "None", "None")

Test_Character = Quick_Character("Test Character", "Fighter", 1, "Human", "Medium", 10, "1d10")

print(" Live Laugh Love ")