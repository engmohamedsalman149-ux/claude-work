"""Builds the slide files of the book deck into ../deck/project. Run: python3 make_deck.py"""
import sys
import lib
for m in sys.argv[1:] or ["part1", "part2", "part3", "part4"]:
    __import__(m)
lib.write(lib.HERE.parent / "deck" / "project")
print(len(lib.order), "slides")
