import sys
import os
import subprocess

def get_real_state():
    try:
        # Get pulse from the core logic
        res = subprocess.run(['python3', 'public_work/core/asm-pulse-v2.py'], capture_output=True, text=True)
        pulse = res.stdout.strip()
        state = "STEADY" if "STEADY" in pulse else "GLITCHED"
        return state
    except:
        return "UNKNOWN"

def generate_lobster(state):
    if state == "GLITCHED":
        return """
       (??)
        !!
   _..-X-.._
  /   #@%   \\
 |   ?   ?   |
 |     ~     |
  \\  '---'  /
   '..___..'
    """
    else:
        return """
     .---.
    /     \\
   (  O O  )
    |  -  |
   /       \\
  /         \\
 |           |
  \\_       _/
    '-----'
    """

if __name__ == "__main__":
    state = get_real_state()
    print(f"🦞 Identity Frame: {state}")
    print(generate_lobster(state))
