[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/X1kaM1Sj)
# COMP-1510-202530-LAB-08
Every program needs a README.md

This is written in markdown.

Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## YOUR NAME:
Harlan Bullock

## YOUR STUDENT NUMBER:
A01477069

## YOUR GITHUB NAME:
moxharley

## HOW DID THE LAB GO:
Mnemosyne - Science Fiction Horror Game: You are a **lone survivor** in a derelict starship drifting through space. The starship’s life-support and sensors are failing and the visual feed from your helmet visor has been damaged and corrupted. You can only see via uploading the starship’s AI, *“archangel”* into your visor to guide you through the wreckage and hazards to the single working escape pod.

Due to the limited weeks and time we had to complete this project, some features I had in mind were not fully integrated yet and the actual story of the game is about a third of the length that I had in mind in my head, however I still feel like I have a very good **demo** of the game. I wanted to prioritize having a clean working product rather than a story that was fully complete. I am proud of my work and I hope you enjoy this spooky scifi experience! For the sake of grading, you can ignore the sound.py file because all that really does is play .ogg files using pygame. It's just for flavor and more immersion.

ONLY READ THE NOTES BELOW ONCE YOU HAVE PLAYED THROUGH THE GAME AT LEAST ONCE (SPOILERS):

Since I chose to do something a little more unique with this project, I would like to go through the requirements in your instructions document and explain what I implemented for each requirement:

Board - The star-ship map has roughly 100+ tiles. Each of which have a description and some of which have items to interact with.

Player - The player has a name, class, HP, EP, as well as an inventory. Certain interactions require certain items.

Movement - Self-explanetory; You can move in the four cardinal directions.

Encounters - There are two kinds of encounters: The first is locational encounters which are set objects you can interact with to potentially gain an edge or suffer a penalty. You must interact with these to get the clearance key to the bridge and open the locks on the pod-bay doors. The other kind of encounters are scripted encounters, which happen when the ship hull reaches a certain amount of damage. These are similar functionally but usually are only harmful and doing well in them will make the damage a little less serious

Overcome Obstacles - When in an encounter, you will be prompted with a few choices, each of which use one of your four stats. You have a higher chance to be successful in rolls you make with your stats that are higher. Some choices will require you to have certain items in your inventory or be a certain class.

Level Up - When you fail a roll, you gain an experience point, and for every three experience points you gain, you can add an additional +1 to one stat of your choice (to a maximum of +2), your health also heals by 1-4 points.

Level 3 - So you can technically go for the end goal at whatever level you would like, but the end-game checks are very hard and typically only possible with a +2 to a stat, so it is far more possible if you are level 3.

Goal - Your final goal is to reach the escape pod bay and escape. Originally, the first escape-pod bay was going to be inaccessible, so the player would have to travel to the other side of the ship to reach the other escape-pod bay and leave, however I decided to cut that and make the game shorter so that I could focus more on the quality over the quantity. If I had more time I would absolutely make the story as full and long as I had originally concocted.


