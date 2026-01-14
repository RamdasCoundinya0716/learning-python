import random

def generate_rand_int(start, end):
    '''Generates a random integer between start and end (inclusive).'''
    return random.randint(start, end)

def generate_rand_float(start, end):
    '''Generates a random float between start and end.'''
    return random.uniform(start, end)