from safety import is_safe, is_risky

def handle(text):
    global pending_action
    t = text.lower()

    # 👇 confirmation reply
    if pending_action["command"]:
        if t in ["haan", "yes", "ok", "kar do"]:
            cmd = pending_action["command"]
            pending_action["command"] = None
            return handle(cmd)   # execute original command
        else:
            pending_action["command"] = None
            return "Theek hai 👍 action cancel kar diya."

    # ❌ fully blocked
    if not is_safe(text):
        return "Ye action risky hai ❌ main allow nahi karta."

    # ⚠️ risky but allowed
    if is_risky(text):
        pending_action["command"] = text
        return "Ye thoda risky hai 😅 confirm karo: haan / nahi"

    # ---- existing logic below ----