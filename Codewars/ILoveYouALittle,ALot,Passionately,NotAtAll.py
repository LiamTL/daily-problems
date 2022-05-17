def how_much_i_love_you(torn_petals):
    petal_dict = {1:'I love you',
            2:'a little',
            3:'a lot',
            4:'passionately',
            5:'madly',
            0:'not at all'}
    return petal_dict.get(torn_petals % 6)