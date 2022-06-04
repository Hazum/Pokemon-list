from random import shuffle

class Pokemon:
  def __init__(self, name, type, health):
    self.name = name
    self.type = type
    self.health = health
    self.fainted = False
    self.attacks = {}

  def set_health(self, newHP):
    if newHP <= 0:
      self.health = 0
      self.fainted = True
    else:
      self.health = newHP

  #Have a maximum and minimum damage of each attack to be used in the randint function
  def add_attack(self, name, max_damage, min_damage):
      self.attacks[name] = [max_damage, min_damage]



pokemon = []
pokemon.append(Pokemon("Pikachu","Electric",78))
pokemon.append(Pokemon("Raichu","Electric",5))
pokemon.append(Pokemon("Magnemite","Electric",51))
pokemon.append(Pokemon("Magneton","Electric",42))
pokemon.append(Pokemon("Voltorb","Electric",15))
pokemon.append(Pokemon("Electrode","Electric",88))
pokemon.append(Pokemon("Electabuzz","Electric",67))
pokemon.append(Pokemon("Jolteon","Electric",142))

  
pokemon.append(Pokemon("Charmander","Fire",23))
pokemon.append(Pokemon("Charmeleon","Fire",64))
pokemon.append(Pokemon("Charizard","Fire",87))
pokemon.append(Pokemon("Vulpix","Fire",32))
pokemon.append(Pokemon("Ninetales","Fire",27))
pokemon.append(Pokemon("Growlithe","Fire",16))
pokemon.append(Pokemon("Arcanine","Fire",58))
pokemon.append(Pokemon("Ponyta","Fire",99))

#shuffle(pokemon)
  