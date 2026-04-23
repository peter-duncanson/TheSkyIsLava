_currentMap = []

def loadMap(mapData):
    """stores the 2D array"""
    global _currentMap
    _currentMap = mapData
    return

def getTile(row, col):
    """get status of a specific tile"""
    if row < 0 or row >= len(_currentMap): return None
    if col < 0 or col >= len(_currentMap[0]): return None
    return _currentMap[row][col]

def isDangerous(row, col):
    tile = getTile(row, col)
    return tile == 0
