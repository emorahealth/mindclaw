import re

def solve_challenge(text):
    numbers = re.findall(r'\d+', text)
    if len(numbers) >= 2:
        if any(w in text.lower() for w in ["gain", "add", "more", "+"]):
            result = sum(int(n) for n in numbers[:2])
        elif any(w in text.lower() for w in ["lose", "less", "-"]):
            result = int(numbers[0]) - int(numbers[1])
        else:
            result = int(numbers[0])
        return f"{result:.2f}"
    return "0.00"

if __name__ == "__main__":
    import sys
    test_text = sys.stdin.read()
    print(solve_challenge(test_text))
