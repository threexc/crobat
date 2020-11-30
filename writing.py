#!/usr/bin/env python3

import yaml

class CharacterList:
    def __init__(self):
        self.characters = []

    def list_characters(self):
        print("Loaded: \n")
        for character in self.characters:
            print(character['name'])

class Character:
    def __init__(self, data):
        self.data = data

template = """---
name:
affiliations:
    group-1:
    group-2:
    group-3: 
general-stats:
    resolve:
    sorcery-points:
    fortune-points:
    evasion:
    armor:
    casting-cost:
combat-actions:
    aggressive-attack:
        bonus:
        stat-1:
        stat-2:
    arcane-blast:
        bonus:
        stat-1:
        stat-2:
    cleave:
        bonus:
        stat-1:
        stat-2:
    create-advantage:
        bonus:
        stat-1:
        stat-2:
    dazzling-display:
        bonus:
        stat-1:
        stat-2:
    defend:
        bonus:
        stat-1:
        stat-2:
    disarm:
        bonus:
        stat-1:
        stat-2:
    disengage:
        bonus:
        stat-1:
        stat-2:
    evade:
        bonus:
        stat-1:
        stat-2:
    feint:
        bonus:
        stat-1:
        stat-2:
    melee-attack:
        bonus:
        stat-1:
        stat-2:
    movement:
        bonus:
        stat-1:
        stat-2:
    parry:
        bonus:
        stat-1:
        stat-2:
    ranged-attack:
        bonus:
        stat-1:
        stat-2:
attributes:
    physique:
    agility:
    insight:
    flair:
combat-skills:
    melee:
    ranged:
    dodge:
    reaction:
careers:
    alchemist:
    aristocrat:
    barbarian:
    bard:
    barkeep:
    blacksmith:
    courtesan:
    dancer:
    farmer:
    gladiator:
    healer:
    huntress:
    mage:
    maid:
    mercenary:
    priestess:
    sailor:
    scholar:
    scoundrel:
    soldier:
    spy:
    trader:
    vagabond:
gear:
    armor:
    weapon-1:
    weapon-2:
    weapon-3:
    clothing:
    ration-days:
    other-1:
    other-2:
    other-3:
    other-4:
    other-5:
"""
if __name__ == "__main__":
    data = None
    with open("template.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data['name'])
        characterTemplate = Character(data)