import time
import pygame
import rich
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os

console = Console()

pygame.mixer.init()

pygame.mixer.music.load(r"C:\Users\Lívia\Downloads\My_Oh_My.mp3")

colors = ["bright_red", "bright_magenta", "bright_yellow", "bright_cyan", "bright_green"]

lyrics = [
    "...",
    "...",
    "...",
    "They say he likes a good time (my, oh, my)",
    "He comes alive at midnight (every night)",
    "My mama doesn't trust him (my, oh, my)",
    "He's only here for one thing, but (so am I)",
    "...",
    "Yeah, a little bit older, a black leather jacket",
    "A bad reputation, insatiable habits",
    "He was onto me, one look and I couldn't breathe, yeah",
    "I said, if he kissed me, I might let it happen (oh)",
    
    "I swear on my life that I've been a good girl (oh)",
    "Tonight, I don't wanna be her",

    "They say he likes a good time (my, oh, my)",
    "He comes alive at midnight (every night)",
    "My mama doesn't trust him (my, oh, my)",
    "He's only here for one thing, but (let's go; so am I)",

    "Look, I'm the type to make her turn on her daddy (oh, yeah)\nDaBaby make her forget what she learned from her daddy",
    "I don't be tripping on lil' shawty, I let her do whatever she please\nI don't be kissing on lil' shawty, she don't be kissing on me either",
    "She came with you, then left with me\nI went up a point, let's call it even (yeah, yeah)",
    "Don't like the car she in, gon' end up buyin' her a new Bimmer (let's go)\nThat girl know what she want, she make me take it off when she see me (let's go)",
    "She say I make her wet whenever my face pop up on TV\nI had to say: No disrespect, gotta do it safe or you can keep it\nPop star, I'm fresh up out the trap and I'm going Bieber",
    "She know I'm a call away, she can drop a pin and I'd come meet her\nStand next to me, you gon' end up catchin' a fever (yeah, yeah)",
    "I'm hot",
    "...",
    "I swear on my life that I've been a good girl (good girl, good girl)",
    "Tonight, I don't wanna be her",

    "They say he likes a good time (my, oh, my)",
    "He comes alive at midnight (every night)",
    "(He comes alive, oh, every night)",
    "My mama doesn't trust him (my, oh, my)",
    "He's only here for one thing, but (so am I)",

    "My, my, my, my, my, oh, my\nMy mama doesn't trust you, baby",
    "My, my, my, my, my, oh, my\nAnd my daddy doesn't know you, no",
    "My, my, my, my, my, oh, my (oh, my, my, my, oh, my)",
    "My, my, my, my, my, oh, my (my, my, my, ooh)",

    "They say he likes a good time (my, oh, my)",
    "He comes alive at midnight (every night)",
    "My mama doesn't trust him (my, oh, my)",
    "He's only here for one thing, but (so am I)"
]

pygame.mixer.music.play()

for i, line in enumerate(lyrics):
    color = colors[i % len(colors)]
    styled_text = Text(line, style=color, justify="center")
    console.print(Panel(styled_text, border_style=color, expand=False))
    time.sleep(4.0)  

