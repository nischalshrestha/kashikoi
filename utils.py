"""
This module contains useful functions for music.
"""

import random as rand
import time
from constants import *

def key_note_list(key, scale):
    """Returns a note list for a given key and scale"""
    # get the scale and cutoff the octave (12) interval
    major_columns = [MODES[scale][i] for i in range(8)][:-1]
    # get the notelist for the particular key
    key_idx = SHARP_NOTES.index(key)
    note_list = np.array(SHARP_NOTES[key_idx:] + SHARP_NOTES[:key_idx])
    return note_list[major_columns]

def note_list():
    """Returns a notelist for all octaves (for e.g. C0-C8)"""
    note_list = []
    for i in range(9):
        # for semi tones like C # or Db we'll go with the sharp representation
        # tone can play either format
        for n in SHARP_NOTES:
            note_list.append(n+str(i))
    return note_list

def halfsteps_from_to(notelist, a, b):
    """Returns distance in number of half steps from note a to b"""
    a_idx = notelist.index(a)
    b_idx = notelist.index(b)
    return (b_idx - a_idx)

def frequency_table():
    """Returns a frequency table for all notes for 8 octaves"""
    # Frequency table stuff
    base = 440
    a = 2**(1/12)
    frequency_table = {}
    f_0 = base; # we'll chose A4 as f0
    for i in range(len(NOTELIST)):
        f = f_0 * a** halfsteps_from_to(NOTELIST, "A4", NOTELIST[i])
        frequency_table[NOTELIST[i]] = round(f, 2)
    return frequency_table

def major(root, formula):
    return MAJOR_FORMULA[formula]

def minor(root, formula):
    return MINOR_FORMULA[formula]

def dominant(root, formula):
    return DOMINANT_FORMULA[formula]

def get_note_list(root, halfsteps):
    """
    Given the root and the halfsteps, returns a list of strings representing
    notes of some sequence such as chords or scales. 

    Parameters
    ----------
    root : a string
        in the letter and octave form (C#)
    halfsteps : a list of ints
        represents the halfsteps in the sequence
    """
    note_list = []
    start_idx = SHARP_NOTES.index(root)
    note_list.append(SHARP_NOTES[start_idx])
    for h in halfsteps[1:]:
        target_idx = (start_idx + h) 
        note_list.append(SHARP_NOTES[target_idx % len(SHARP_NOTES)])
    return note_list

def get_random_chord(key):
    """
    Returns a random chord as a list of notes, given a key.
    
    Parameters
    ----------
    key : a string
        in the letter and octave form (e.g. C#2)
    """
    possible_families = ['maj', 'min', 'dom']
    family = rand.choices(possible_families, [0.33, 0.33, 0.33], k = 1)[0]
    if family == 'maj':
        formulas = list(MAJOR_FORMULA.keys())
        formula = formulas[rand.randint(0, len(formulas) - 1)]
        chord = major(key, formula)
    elif family == 'min':
        formulas = list(MINOR_FORMULA.keys())
        formula = formulas[rand.randint(0, len(formulas) - 1)]
        chord = minor(key, formula)
    elif family == 'dom':
        formulas = list(DOMINANT_FORMULA.keys())
        formula = formulas[rand.randint(0, len(formulas) - 1)]
        chord = dominant(key, formula)
    return get_note_list(key, chord)

