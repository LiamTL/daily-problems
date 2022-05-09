dir = {"N": {"W":"left", "E":"right"},
      "S": {"E":"left", "W":"right"},
      "E": {"N":"left", "S":"right"},
      "W": {"S":"left", "N":"right"}}

def turn(current, target):
    return dir[current][target]