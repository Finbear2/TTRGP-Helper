import random
from random import randint
from dataclasses import dataclass

class Character:
    
    Character_Amount = 0
    @dataclass
    class Coins:
        CP: int
        EP: int
        PP: int
        GP: int
        SP: int
          
    @dataclass
    class All_Stats:
        
        @dataclass  
        class Main_Stats:
            Strength: int
            Dexterity: int
            Constitution: int
            Intelligence: int
            Wisdom: int
            Charisma: int
            
        @dataclass
        class Basic_Stats:
            Name: str
            Class: str
            Level: int
            Background: str
            Race: str
            Alignment: str
            Size: str
            Human: str
        
    @dataclass
    class Death_Saves:
        Success: int
        Failure: int
    
    def __init__(Self, Name, Class, Level, Background, Race, Alignment, Size, Human, Stats, Armor_Class, Initiative, Speed, Hit_Points, Hit_Dice, Proficiency_Bonus, Saving_Throws, Equipment, Spells, Currency, Backstory, Traits, Features, Languages, Notes, Death_Saves):
    
        Self.Currency = Self.Coins( Currency["Copper"], Currency["Electrum"], Currency["Platinum"], Currency["Gold"], Currency["Silver"] )
        
        Self.Stats = Self.All_Stats()
        Self.Stats.Main_Stats = Self.All_Stats.Main_Stats( Stats["Strength"], Stats["Dexterity"], Stats["Constitution"], Stats["Intelligence"], Stats["Wisdom"], Stats["Charisma"] )
        Self.Stats.Base_Stats = Self.All_Stats.Basic_Stats( Name, Class, Level, Background, Race, Alignment, Size, Human )

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
        
        Self.Spells = Spells if Spells is not None else "None"
        
        Self.Character_Amount += 1
        Self.ID = Self.Character_Amount


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
    
    return dict(zip(Items, Amounts))
    
def Calculate_Speed(Race):
    
    if any( r in Race for r in ["Human", "Elf", "Tiefling", "Tabaxi"]):
        Speed = 30
    elif any( r in Race for r in ["Dwarf", "Gnome", "Halfling"]):
        Speed = 25
    else:
        Speed = 40
        
    return Speed
  
    
def Quick_Character(Name, Class, Level, Race, Size, HP, Hit_Dice):
    
    Strength = randint(-1,3); Dexterity = randint(-1,3); Constitution = randint(-1,3); Intelligence = randint(-1,3); Wisdom = randint(-1,3); Charisma = randint(-1,3)
    
    return Create_Character(Name, Class, Level, Race, Size, "None", "Neutral", "None", Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, HP, Hit_Dice, "None", "None", 0, 0, 0, 10, 0, "None", "None", "None", "Common", "None")

def Create_Character(Name, Class, Level, Race, Size, Background, Alignment, Human, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, HP, Hit_Dice, Equipment, Spells, CP, SP, EP, GP, PP, Backstory, Traits, Features, Languages, Notes):
    
    Speed = Calculate_Speed(Race)
        
    return Character(Name, Class, Level, Background, Race, Alignment, Size, Human, Create_Stats(Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma),
                     10 + ( Dexterity * 2 ), Dexterity, Speed, HP, Hit_Dice, 2 + (Level - 1) // 4,
                     Create_Saving_Rolls(Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma,Class,2 + (Level - 1) // 4),
                     Equipment, Spells, Create_Coins(CP, EP, PP, GP, SP), Backstory, Traits, Features, Languages, Notes, {"Success": 0, "Failure": 0})


Test_Character = Quick_Character("Test", "Fighter", 1, "Human", "Medium", 10, "1d10")

print("D&D Helper")