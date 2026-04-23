from engine import core, graphics, getinput, tilemap 

treeImagePath = "assets/tree.png"
backgroundImagePath = "assets/background.png"
steelBlockImagePath = "assets/steelBlock.png"
tarImagePath = "assets/tar.png"
rockImagePath = "assets/rock.png"
font = "iosevkanerdfont"


player = {
    "row": 15,
    "col": 8,
    "lives": 3,
    "score": 0
}

areaTileArray = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

areaKey = {
    0: "danger",
    1: "safe",
    2: "stuck"
}

def initGame():
    graphics.init()
    getinput.init()

    graphics.loadImage("tree", treeImagePath)
    graphics.loadImage("background", backgroundImagePath)
    graphics.loadImage("steelBlock", steelBlockImagePath)
    graphics.loadImage("tar", tarImagePath)
    graphics.loadImage("rock", rockImagePath)

    graphics.loadFont("font", font, 18)

    tilemap.loadMap(areaTileArray)

def updateGame(dt):
    global player

    getinput.update()
    targetRow = player["row"]
    targetCol = player["col"]

    if getinput.justPressed("left") and player["col"] != 0: targetCol -= 1
    if getinput.justPressed("right") and player["col"] != 15: targetCol += 1

    # targetTile = tilemap.getTile(targetRow, targetCol)

    player["row"] = targetRow
    player["col"] = targetCol

    if tilemap.isDangerous(player["row"], player["col"]):
        player["lives"] -= 1

def draw(screen):
    graphics.drawTilemap(screen, tilemap._currentMap, areaKey)

    graphics.drawImage(screen, "tree", player["row"], player["col"])

if __name__ == "__main__":
    core.init(width = 512, height = 576)
    initGame()

    core.run(updateGame, draw)
