init python:
    class item:
        value = 0
        name = "null"
        def __init__(self, name, value):
            self.item = "Item"
            self.name = name
            self.value = value

    class trait:

        name = "null"
        playerHave = True
        def __init__(self, name, playerHave):
            self.item = "Item"
            self.name = name
            self.playerHave = playerHave

##$ playerPronounPart1 = "null"
##$ playerPronounPart2 = "null"
$ playerTraits = []
$ inventory = []
$ officeCoin = 0
$ bonzi_quest_stage = 0  # Setting the value of 'first_visit' to 0
$ bonzi_quest_update = false