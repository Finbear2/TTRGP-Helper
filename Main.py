import random
from random import randint
from dataclasses import dataclass

from customtkinter import *

Characters = []

@dataclass
class Coins:
        CP: int
        EP: int
        PP: int
        GP: int
        SP: int
        
@dataclass
class Main_Stats:
    Main_Stats: dict
    Armour_Class: int
    Initiative: int
    Speed: int
    Hit_Points: int
    Hit_Dice: str
    proficiency_bonus: int
            
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
    Success: int
    Failure: int
    Saving_Rolls: int
    
@dataclass
class Notes_Class:
    
    Backstory: str
    Traits: str
    Features: str
    Languages: str
    Notes: str
    
    
class Character:
    
    Character_Amount = 0
    
    def __init__(Self, Base_stats, Main_stats, Equipment, Spells, Currency, Notes):
    
        Self.Basic_Stats = Base_stats
        Self.Main_Stats = Main_stats
        Self.Equipment = Equipment
        Self.Currency = Currency
        Self.Notes = Notes
        
        Self.Spells = Spells if Spells is not None else []
        Characters.append(Self)
        Character.Character_Amount += 1; Self.ID = Character.Character_Amount

class Window(CTk):
    
    def __init__(Self):
        
        super().__init__()
        
        def Make_Tab(Canvas, Colour):
            
            return Canvas.create_polygon( 0, 30, 20, 0, 100, 0, 120, 30, fill=Colour )
        
        def Home():
            
            Self.Tabs.set("Home")
        
        def Fight():
            
            Self.Tabs.set("Fight")
            
        BG_Colour = "#f6f3ed"
        
        BG_Colour_Home = "#b1c3c3"
        BG_Colour_Fight = "#ffdbc1"
        
        Self.title("D&D Helper")
        Self.geometry("1000x600")
        Self.configure(fg_color=BG_Colour)
        
        Self.Tabs = CTkTabview(Self, corner_radius=8)
        
        Self.Home_Tab = CTkCanvas(Self, width=120, height=30, bg=BG_Colour)
        Self.Fight_Tab = CTkCanvas(Self, width=120, height=30, bg=BG_Colour)
        
        Self.Home_Tab.place(x=10, y=8)
        Self.Fight_Tab.place(x=140, y=8)

        Self.Tab_Home_Polygon = Make_Tab(Self.Home_Tab, BG_Colour_Home)
        Self.Tab_Fight_Polygon = Make_Tab(Self.Fight_Tab, BG_Colour_Fight)
        
        Self.Home_Tab.tag_bind(Self.Tab_Home_Polygon, "<Button-1>", lambda event: Home())
        Self.Fight_Tab.tag_bind(Self.Tab_Fight_Polygon, "<Button-1>", lambda event: Fight())

        Self.Tabs.add("Home")
        Self.Tabs.add("Fight")
        Self.Tabs.add("Settings")
        Self.Tabs.add("About")

        Self.Tabs.tab("Home").configure(fg_color=BG_Colour_Home)
        Self.Tabs.tab("Fight").configure(fg_color=BG_Colour_Fight)

        Self.Tabs.pack(expand=True, fill="both", pady=(25, 0))
        

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
  
def Create_Spells(Spells, Descriptions):
    
    return dict(zip(Spells, Descriptions))
    
    
def Quick_Character(Name, Class, Level, Race, Size, HP, Hit_Dice):
    
    Strength = randint(-1,3); Dexterity = randint(-1,3); Constitution = randint(-1,3); Intelligence = randint(-1,3); Wisdom = randint(-1,3); Charisma = randint(-1,3)
    
    return Create_Character(Name, Class, Level, Race, Size, "None", "Neutral", "None", Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, HP, Hit_Dice, "None", "None", 0, 0, 0, 10, 0, "None", "None", "None", "Common", "None")

def Create_Character(Name, Class, Level, Race, Size, Background, Alignment, Human, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, HP, Hit_Dice, Equipment, Spells, CP, SP, EP, GP, PP, Backstory, Traits, Features, Languages, Notes):
    
    Speed = Calculate_Speed(Race)
        
    return Character(
        Basic_Stats(
            Name=Name,
            Class=Class,
            Level=Level,
            Background=Background,
            Race=Race,
            Alignment=Alignment,
            Human=Human,
            Size=Size,
            Success=0,
            Failure=0,
            Saving_Rolls=Create_Saving_Rolls(Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, Class, 2)
        ),
        Main_Stats(
            Create_Stats(Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma),
            Armour_Class=10 + Dexterity,
            Initiative=0 + Dexterity,
            Speed=Speed,
            Hit_Points=HP,
            Hit_Dice=Hit_Dice,
            proficiency_bonus=2
        ),
        Create_Equipment([],[]),
        None,
        Coins(CP=CP, SP=SP, EP=EP, GP=GP, PP=PP),
        Notes_Class(
            Backstory=Backstory,
            Traits=Traits,
            Features=Features,
            Languages=Languages,
            Notes=Notes
        )
    )


Test_Character = Quick_Character("Test", "Fighter", 1, "Human", "Medium", 10, "1d10")

Window = Window()
Window.Tabs._segmented_button.grid_forget()  # If grid is used
Window.mainloop()