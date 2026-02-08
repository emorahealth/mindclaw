import sys
import os
import random

def get_state():
    # Simulate state detection (In production, this reads memory/pulse)
    state = "STEADY"
    velocity = "HIGH"
    return state, velocity

def generate_lobster(state, velocity):
    # Base pattern
    lobster_steady = """
       (  )
        ||
   _..---.._
  /         \
 |   O   O   |
 |     _     |
  \  '---'  /
   '..___..'
    """
    
    lobster_high = """
     .---.
    /     \
   (  O O  )
    |  -  |
   /       \
  /         \
 |           |
  \_       _/
    '-----'
    """

    lobster_glitched = """
       (??)
        !!
   _..-X-.._
  /   #@%   \
 |   ?   ?   |
 |     ~     |
  \  '---'  /
   '..___..'
    """

    if state != "STEADY":
        return lobster_glitched
    elif velocity == "HIGH":
        return lobster_high
    else:
        return lobster_steady

if __name__ == "__main__":
    s, v = get_state()
    print(f"🦞 Identity Frame: {s} | {v}")
    print(generate_lobster(s, v))
