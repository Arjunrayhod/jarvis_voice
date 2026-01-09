from safety import is_safe, is_risky

pending_action = {"command": None}

def handle(text):
    global pending_action
    t = text.lower()

    # confirmation reply
    if pending_action["command"]:
        if t in ["haan", "yes", "ok", "kar do"]:
            cmd = pending_action["command"]
            pending_action["command"] = None
            return f"✅ Confirmed: {cmd}"
        else:
            pending_action["command"] = None
            return "❌ Action cancel kar diya."

    # blocked
    if not is_safe(text):
        return "❌ Ye action allowed nahi hai."

    # risky but allowed
    if is_risky(text):
        pending_action["command"] = text
        return "⚠️ Ye thoda risky hai, confirm karo: haan / nahi"

    return f"🙂 Command received: {text}"