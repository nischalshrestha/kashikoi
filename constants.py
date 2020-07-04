"""
This module contains all things related to music as constants
"""

# Declaring all constants
OCTAVE = 8
CHROMATIC = 12
# each value is # halfsteps
SCALES = {
    'major': [0, 2, 4, 5, 7, 9, 11, 12],
    'minor': [0, 2, 3, 5, 7, 9, 10, 12],
    'natural_minor': [0, 2, 3, 5, 7, 8, 10, 12],
    'harmonic_minor': [0, 2, 3, 5, 7, 8, 11, 12]
}
# each value is # halfsteps
MODES = {
    'ionian': [0, 2, 4, 5, 7, 9, 11, 12],
    'dorian': [0, 2, 3, 5, 7, 9, 10, 12],
    'phrygian': [0, 1, 3, 5, 7, 8, 10, 12],
    'lydian': [0, 2, 4, 6, 7, 9, 11, 12],
    'mixolydian': [0, 2, 4, 5, 7, 9, 10, 12],
    'aeolian': [0, 2, 3, 5, 7, 8, 11, 12],
    'locrian': [0, 1, 3, 5, 6, 8, 10, 12],
}

ESOTERIC = {
    'super_locrian': [0, 1, 3, 4, 6, 8, 10],
    'arabic': [0, 1, 4, 5, 7, 8, 11],
    'hungarian_minor': [0, 2, 3, 6, 7, 8, 11],
    'minor_gypsy': [0, 1, 4, 5, 7, 8, 10],
    'hirojoshi': [0, 2, 3, 7, 8],
    'in_sen': [0, 1, 5, 7, 10],
    'iwato': [0, 1, 5, 6, 10],
    'kumoi': [0, 2, 3, 7, 9],
    'pelog': [0, 1, 3, 4, 7, 8],
    'spanish': [0, 1, 3, 4, 5, 6, 8, 10],
    'tritone': [0, 1, 4, 6, 7, 10],
    'enigmatic': [0, 1, 4, 6, 8, 10, 11]
}

# these are based on how many half tones needed for 3rd 5th etc.
# trick: 1, 3, 5 => 1-1 (0 meaning no interval), 3-1 (first 2 of ionian), 5-1 (first 4 of ionian) 
MAJOR_FORMULA = {
    'maj': [0, 4, 7],
    'maj6': [0, 4, 7, 9],
    'maj7': [0, 4, 7, 11],
    'maj9': [0, 4, 7, 11, 14],
    'majadd9': [0, 4, 7, 14],
    'maj6/9': [0, 4, 7, 9, 14],
    'maj7/6': [0, 4, 7, 9, 11],
    'maj13': [0, 4, 7, 11, 14, 21],
}

MINOR_FORMULA = {
    'min': [0, 3, 7],
    'min6': [0, 3, 7, 9],
    'min7': [0, 3, 7, 10],
    'min9': [0, 3, 7, 10, 14],
    'min11': [0, 3, 7, 10, 14, 17],
    'min7/11': [0, 3, 7, 10, 17],
    'minadd9': [0, 3, 7, 14],
    'min9/9': [0, 3, 7, 9, 14],
    'minmaj7': [0, 3, 7, 11],
    'minmaj9': [0, 2, 3, 7, 11],
}

DOMINANT_FORMULA = {
    '7': [0, 4, 7, 10],
    '7/6': [0, 4, 7, 10, 9],
    '7/11': [0, 4, 7, 10, 17],
    '7sus4': [0, 5, 7, 10],
    '7/6sus4': [0, 5, 7, 10, 9],
    '9': [0, 4, 7, 10, 14],
    '11': [0, 4, 5, 7, 10],
    '13': [0, 4, 7, 10, 21],
    '7/6/11': [0, 4, 10, 9, 17],
    '11/13': [0, 4, 5, 7, 9, 10],
    'dim': [0, 3, 6], 
    'dim7': [0, 3, 6, 9],
    '+': [0, 4, 8],
    '+7': [0, 4, 8, 10],
}

SHARPS = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
FLATS = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb']
SHARP_NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
FLAT_NOTES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
# these will be used to convert between the representations based
# on whether scale or chord adds accidentals (for e.g. min will use flat)
EQUIVALENTS = {
    # # to b
    'C#': 'Db', 
    'D#': 'Eb', 
    'F#': 'Gb', 
    'G#': 'Ab', 
    'A#': 'Bb',
    # b to #
    # 'Db': 'C#',
    # 'Eb': 'D#',
    # 'Gb': 'F#', 
    # 'Ab': 'G#',
    # 'Bb': 'A#',
}

# Note relative lengths and time constants
SIXTY_FOURTH = 0.0625
THIRTY_SECOND = 0.125
SIXTEENTH = 0.25
EIGHTH = 0.5
QUARTER = 1
HALF = 2
WHOLE = 4
MINUTE = 60.0
