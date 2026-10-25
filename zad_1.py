def welcome(name: str, surname: str) -> str:
    message = f"Cześć {name} {surname}"
    return message


message = welcome("marek", "kleszcz")
print(message)
