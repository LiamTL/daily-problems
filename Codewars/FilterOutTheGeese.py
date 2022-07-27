geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    non_geese = []
    for bird in birds:
        if not bird in geese:
            non_geese.append(bird)
    return non_geese