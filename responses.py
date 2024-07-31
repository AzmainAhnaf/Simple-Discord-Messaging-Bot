from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Well, you're awfully silent there"
    elif "hello" in lowered:
        return "Hello there, Welcome to Coffee Shop, can I offer you a cup of coffee?"
    elif "yes" in lowered:
        return "What can I get for you?"
    elif "coffee" in lowered or "espresso" in lowered or "americano" in lowered or "capuchino" in lowered:
        return f"please sit at the table number {randint(1, 10)}, Your coffee will be ready in a minute"
    elif "suggest" in lowered:
        return choice(["Espresso", "Americano", "Capuchino"])
    elif "thank" in lowered or "thanks" in lowered:
        return "You are welcome"
    elif "bye" in lowered:
        return "Thanks for coming, please do come again"
    elif "help" in lowered:
        return """"Suggest" - if you want me to suggest coffee to you\n
"Coffee_name" - if you have decided which coffee you wanna take\n
                """
    elif "no" in lowered:
        return "Please feel free to sit and enjoy our ambience"