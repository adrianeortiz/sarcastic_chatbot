import random
import re

# List of sarcastic responses
SARCASTIC_RESPONSES = [
    "Oh wow, that's *so* interesting. 🙄",
    "Sure, because that makes *total* sense. 😂",
    "Wow, tell me more. I'm *totally* fascinated. 🙃",
    "You must be *so* proud of yourself. 😏",
    "Ah yes, because that’s *exactly* how life works. 😆"
]

def get_sarcastic_response(user_input):
    # Define some sarcastic triggers
    patterns = [
        r'\b(love|hate|like)\b',
        r'\b(always|never|every time)\b',
        r'\b(really|seriously|sure)\b',
        r'\b(why|what|how)\b'
    ]
    
    for pattern in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(SARCASTIC_RESPONSES)
    
    return "Oh wow, I’m speechless. 🙃"

def main():
    print("Sarcastic Bot: Hey there, what's on your mind?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Sarcastic Bot: Finally, some peace and quiet. 😏")
            break
        response = get_sarcastic_response(user_input)
        print(f"Sarcastic Bot: {response}")

if __name__ == "__main__":
    main()
