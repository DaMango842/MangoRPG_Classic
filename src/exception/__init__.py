
class GameError(Exception):
    def __init__(self, einfo):
        super().__init__(self)
        self.einfo = einfo
    def __str__(self):
        return self.einfo

class BattleError(Exception):
    def __init__(self, einfo):
        super().__init__(self)
        self.einfo = einfo
    def __str__(self):
        return self.einfo

class TextError(Exception):
    def __init__(self, einfo):
        super().__init__(self)
        self.einfo = einfo
    def __str__(self):
        return self.einfo