DANGEROUS_KEYWORDS = [
    "format", "delete system", "erase disk",
    "password", "credentials", "registry"
]

RISKY_KEYWORDS = [
    "close", "kill", "stop",
    "volume 100", "full volume",
    "overwrite", "replace"
]

def is_safe(command: str) -> bool:
    c = command.lower()
    for k in DANGEROUS_KEYWORDS:
        if k in c:
            return False
    return True

def is_risky(command: str) -> bool:
    c = command.lower()
    for k in RISKY_KEYWORDS:
        if k in c:
            return True
    return False