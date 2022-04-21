import random
import re
import pygame as pg
import requests
import textwrap
import time

while 1:
    # fetch the quote
    # url = 'https://type.fit/api/quotes'
    # r = requests.get(url)
    # body = (r.json()) # if response type was set to JSON, then you'll automatically have a JSON response here...
    

    import json
    print("HERE")

    import glob, random
    filename = random.choice(glob.glob("sources/*.json")) #change dir name to whatever
    print("chose filename = ", filename)
    # # filename = 'sources/startup_quotes.json'
    with open(filename, 'r') as f:
        body = json.load(f)
    max_size = len(body)-1

    # get a random index
    index = random.randint(0, max_size)
    quote = body[index]['quote']

    # split every 35 chars over new line
    max_line_len = 28
    quote = textwrap.fill(quote, max_line_len)

    # quote = re.sub("(.{30})", "\\1\n", quote, 0, re.DOTALL)

    pg.init()
    # use a (r, g, b) tuple for color
    yellow = (255, 255, 0)

    # create the basic window/screen and a title/caption
    # default is a black background
    screen = pg.display.set_mode((1028, 800))
    # screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("GET OFF THE COUCH")
    # pick a font you have and set its size
    original_font_size = 80

    myfont = pg.font.SysFont("Comic Sans MS", 80)

    lines = quote.splitlines()
    # pad a line at the top
    if len(quote) <= 125: lines.insert(0,'')
    if len(quote) <= 70: lines.insert(0,'')
    if len(quote) <= 35: lines.insert(0,'')
    myfont = pg.font.SysFont("Comic Sans MS", 90)
    yellow = (255, 255, 0)
    x= 55 #max(15, len(quote) * 0.5)
    y= 0 # max(5, len(quote) * 5)
    fsize= 80
    for i, l in enumerate(lines):
        screen.blit(myfont.render(l, 0, yellow), (x, y + fsize*i))
    # rotate screen round
    # screen.blit(pg.transform.rotate(screen, 180), (0, 0))
    # put the label object on the screen at point x=100, y=100

    # show the whole thing
    pg.display.flip()
    
    # exit ability
    for event in pg.event.get():
        # exit conditions --> windows titlebar x click
        if event.type == pg.QUIT:
            raise SystemExit

    # time.sleep(20)
