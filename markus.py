#!/usr/bin/env python3
"""
Created by: Liary Ren
Created by: Sept 10 2025
This program defines the function ariana_says, which repeats a given word
four times, separated by the string ", next ". 
"""
def ariana_says(word: str) -> str:
    """Return word repeated four times with the string ', next ' between each
    occurrence.
    
    >>> ariana_says('Thank u')
    'Thank u, next Thank u, next Thank u, next Thank u'
    >>> ariana_says('Love')
    'Love, next Love, next Love, next Love'
    """
    return ", next ".join([word] * 4)
