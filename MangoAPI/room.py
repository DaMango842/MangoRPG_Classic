

class Room(object):
    
    def __init__(
        self,
        _roomname,
        _name,
        _desc="",
        _north="",
        _east="",
        _south="",
        _west=""
        ):
        self.RoomName = _roomname
        self.Name = _name
        self.Desc = _desc
        self.North = _north
        self.East = _east
        self.South = _south
        self.West = _west       