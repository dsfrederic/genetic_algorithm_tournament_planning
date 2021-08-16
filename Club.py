class Club: 
    def __init__(self, name, nrOfTerrains, blockedDates, canHostMultipleCategories) -> None:
        self._name = name
        self._nrOfTerrains = nrOfTerrains
        self._blockedDates = blockedDates
        self._name = name
        self._canHostMultipleCategories = canHostMultipleCategories

CLUBS = [
    ["DRC", 2,[1, 2], True ],
    ["GENT", 2,[5], False ],
    ["OUDENAARDE", 1,[3, 4, 5], True ],
    ["ANTWERPEN", 1,[], True ]
]