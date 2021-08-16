class Tournament: 
    def __init__(self, id) -> None:
        self._id = id; 
        self._tournamentDay = None
        self._host = None
        self._attendingTeams = None

    def __str__(self): 
        return str(self.get_id)