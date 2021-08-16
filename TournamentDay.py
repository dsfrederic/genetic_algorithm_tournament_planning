class TournamentDay: 
    def __init__(self, id, date) -> None:
        self._id = id; 
        self._date = date
        self._tournaments = None

    def get_id(self): return self._id
    def get_date(self): return self._date    
    def get_tournaments(self): return self._tournaments

    def __str__(self): 
        return str(self.get_id)