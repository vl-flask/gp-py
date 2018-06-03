def speak(txt):
    def whisper(t):
        return t.lower() + "..."
    return whisper(txt)
