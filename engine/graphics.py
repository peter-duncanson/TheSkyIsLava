import pygame

_textures = {}
_fonts = {}
_tileSize = 32

def init():
    pygame.font.init()

def loadImage(textureID, path, alphaConvert = True):
    try:
        image = pygame.image.load(path)
        if alphaConvert:
            _textures[textureID] = image.convert_alpha()
        else:
            _textures[textureID] = image.convert()
    except FileNotFoundError:
        print("ERROR: could not find image at {}.".format(path))

def loadFont(fontID, fontName, size):
    try:
        _fonts[fontID] = pygame.font.SysFont(fontName, size)
    except Exception:
        print("ERROR: could not load font {}: {}".format(Exception))

def drawTilemap(screen, mapArray, tileMapping):
    for rowNumber, row in enumerate(mapArray):
        for colNumber, tileID in enumerate(row):
            pixelX = colNumber * _tileSize
            pixelY = rowNumber * _tileSize
            
            textureID = tileMapping.get(tileID)
            # make sure .get() returns something and that the texture is loaded
            if textureID and textureID in _textures:
                screen.blit(_textures[textureID], (pixelX, pixelY))

def drawImage(screen, textureID, row, col):
    """Draws something on the grid based on its column and row."""
    if textureID in _textures:
        pixelY = row * _tileSize
        pixelX = col * _tileSize
        screen.blit(_textures[textureID], (pixelX, pixelY))
    else:
        print("ERROR: Tried to draw unloaded texture {}".format(textureID))

def drawText(screen, text, fontID, x, y, color):
    """accepts raw x, y; more freedom to place things"""
    if fontID in _fonts:
        textSurface = _fonts[fontID].render(str(text), True, color)
        screen.blit(textSurface, (x, y))
    else:
        print("ERROR: Tried to use unloaded font {}".format(fontID))

def getTextureSize(textureID):
    if textureID in _textures:
        return _textures[textureID].get_size()
    return (0, 0)
