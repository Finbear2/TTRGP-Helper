import random
from random import *

Character_Amount = 0

class Character:
    
    def __init__(Self, Name, Class, Level, Background, Race, Alignment, Size, Human, Stats, Armor_Class, Initiative, Speed, Hit_Points, Hit_Dice, Proficiency_Bonus, Saving_Throws, Equipment, Spells, Coins, Backstory, Traits, Features, Languages, Notes, Death_Saves):
        
        global Character_Amount
        
        Self.Name = Name
        Self.Class = Class
        Self.Level = Level
        Self.Background = Background
        Self.Race = Race
        Self.Alignment = Alignment
        Self.Size = Size
        Self.Human = Human  
        Self.Armor_Class = Armor_Class
        Self.Initiative = Initiative
        Self.Speed = Speed
        Self.Hit_Points = Hit_Points
        Self.Hit_Dice = Hit_Dice
        Self.Proficiency_Bonus = Proficiency_Bonus
        Self.Saving_Throws = Saving_Throws
        Self.Equipment = Equipment
        Self.Backstory = Backstory
        Self.Traits = Traits
        Self.Features = Features
        Self.Languages = Languages
        Self.Notes = Notes
        Self.Death_Saves = Death_Saves
        
        Self.Successes = Death_Saves["Success"]
        Self.Failures = Death_Saves["Failure"]
        
        Self.CP = Coins["CP"]
        Self.EP = Coins["EP"]
        Self.PP = Coins["PP"]
        Self.GP = Coins["GP"]
        Self.SP = Coins["SP"]
        
        Self.Strength = Stats["Strength"]
        Self.Dexterity = Stats["Dexterity"]
        Self.Constitution = Stats["Constitution"]
        Self.Intelligence = Stats["Intelligence"]
        Self.Wisdom = Stats["Wisdom"]
        Self.Charisma = Stats["Charisma"]
        
        if Spells != None:
            Self.Speed = Spells
        else:
            Self.Spells = "None"
        
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
       
def Create_Coins(CP, EP, PP, GP, SP):
    
    return {
        "Copper": CP,
        "Electrum": EP,
        "Platinum": PP,
        "Gold": GP,
        "Silver": SP
    }
    
def Create_Equipment(Items, Amounts):
    
    Equipment = {}
    
    for item in range(len(Items)):
        Equipment.append({Items[item]: Amounts[item]})
        
    return Equipment
        
        
    
def Quick_Character(Name, Class, Level, Race, Size, HP, Hit_Dice):
    
    Strength = randint(-1,3); Dexterity = randint(-1,3); Constitution = randint(-1,3); Intelligence = randint(-1,3); Wisdom = randint(-1,3); Charisma = randint(-1,3)
    
    Speed = None
    
    if any( r in Race for r in ["Human", "Elf", "Tiefling", "Tabaxi"]):
        Speed = 30
    elif any( r in Race for r in ["Dwarf", "Gnome", "Halfling"]):
        Speed = 25
    else:
        Speed = 40
    
    return Character(Name, Class, Level, "None", Race, "Neutral Good", Size, "None",
                     Create_Stats(randint(-1,3),Dexterity,randint(-1,3),randint(-1,3),randint(-1,3),randint(-1,3) ),
                     10 + ( Dexterity * 2 ), Dexterity, Speed, HP, Hit_Dice, 2 + (Level - 1) // 4,
                     Create_Saving_Rolls(Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma,Class,2 + (Level - 1) // 4),
                     "None", "None", "None", "None", "None", "None", "None", "None", "None", {"Success": 0, "Failure": 0})

def Create_Character(Name, Class, Level, Race, Size, Background, Alignment, Human, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, HP, Hit_Dice, Equipment, Spells, CP, SP, EP, GP, PP, Backstory, Traits, Features, Languages, Notes):
    
    Speed = None
    
    if any( r in Race for r in ["Human", "Elf", "Tiefling", "Tabaxi"]):
        Speed = 30
    elif any( r in Race for r in ["Dwarf", "Gnome", "Halfling"]):
        Speed = 25
    else:
        Speed = 40
        
    return Character(Name, Class, Level, Background, Race, Alignment, Size, Human, Create_Stats(Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma),
                     10 + ( Dexterity * 2 ), Dexterity, Speed, HP, Hit_Dice, 2 + (Level - 1) // 4,
                     Create_Saving_Rolls(Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma,Class,2 + (Level - 1) // 4),
                     Equipment, Spells, Create_Coins(CP, EP, PP, GP, SP), Backstory, Traits, Features, Languages, Notes, {"Success": 0, "Failure": 0})

Test_Character = Create_Character("Test", "Fighter", 1, "Human", "Medium", "Soldier", "Neutral Good", "Yes", 0, 0, 0, 0, 0, 0, 10, 1, "None", "None", 0, 0, 0, 10, 0, "Test Backstory", "Test Traits", "Test Features", "Common", "Test Notes")

print(" Live Laugh Love ")