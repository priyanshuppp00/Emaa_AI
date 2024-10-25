memory = {}

def save_to_memory(key, value):
    memory[key] = value

def get_from_memory(key):
    return memory.get(key, "")
