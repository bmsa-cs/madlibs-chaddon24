"""
MadLibs
Author: Clare Haddon
Period/Core: 7
this story is about a road trip and some struggles they have along the way.
"""
width = 60
from textwrap import wrap
#All of the inputs go here. 
noun = input("Enter a noun: ")
verb1 = input("Enter a verb ending in ing: ")
food = input("Enter a food: ")
name = input("Enter a name: ")
name_of_animal = input("enter an animal: ")
adverb = input("Enter an adverb: ")
adjective = input("Enter an adejctive: ")
verb = input("Enter a past tense verb: ")
adjectivetwo =  input("Enter another adjective: ")
nountwo = input("Enter a place: ") 
action_word = input("Enter a weather conditon: ")
adjectivethree = input("Enter a description of your dream weather: ")
month = input("Enter a month: ")
num = input("Enter a number: ")
kind = input("Enter your favorite genre of movies: ")
#This is where my story will be starting. It will be helpful to read this code down below so you have an idea of how the story is laid out.


paragraph = wrap("\nI couldn't wait to leave for the trip to "+ noun + ". We were done packing the car \nand all we had to do was eat and then get on the road. " + verb1 + " out of bed, I \ngot dressed and headed down for breakfast. I ate my " + food + " as fast as I could, and told my family to hurry up.\n \"Sorry " + name +" we have to wait for the " + name_of_animal + " sitter to come first, and then we can go. They should be here soon.\" I " + adverb + " stomped to the couch and waited. Finally I heard a knock at my " + adjective + " door and " + verb + " to it. \"Mom! the sitter is here!\" I yelled. Oh my gosh, the sitter looked so " + adjectivetwo + "! \"Don't look like that! Everything is going to be fine! After all, you are in " + nountwo + " where it is safe and we only have one animal for you to take care of.\" \n \"Thank you, I think once I get used to the place I will take great care of your " + name_of_animal + "\" Then, we kissed our " + name_of_animal + " on the head and got in the car.",width)

for line in paragraph:
    print(line)
#This is the second half of the story. 
paragraph = wrap(f"\n\nWe had finally made it to {noun}. We had rented out this cabin in the mountains. The whole way up the mountain, it was {action_word}. It was getting dark but we made it. I was dreaming of {adjectivethree} and Christmas time, after all it was {month}. \"Lets make cookies\" I said. \"I think that it is the perfect thing to do in this cabin!\" We made cookies and sat in the living room together the rest of the night and watched " + num +  kind + " movies.", width)

for line in paragraph:
    print(line)