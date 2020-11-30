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

if __name__ == "__main__":
    data = None
    with open("template.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data['name'])
        characterTemplate = Character(data)
