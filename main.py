from engine import core, graphics, getinput, tilemap 

treeImagePath = "assets/tree.png"
backgroundImagePath = "assets/background.png"
steelBlockImagePath = "assets/steelBlock.png"
tarImagePath = "assets/tar.png"
rockImagePath = "assets/rock.png"
font = "iosevkanerdfont"
keydownmoveleft = 0
keydownmoveright = 0

player = {
    "row": 12,
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

def updateGame(dt, tracktime):
    global player
    global keydownmoveleft
    global keydownmoveright
    
    getinput.update()
    targetRow = player["row"]
    targetCol = player["col"]

    if getinput.justPressed("left") or keydownmoveleft == 5:
        targetCol -= 1
        keydownmoveleft = 0
    if getinput.justPressed("right") or keydownmoveright == 5: 
        targetCol += 1
        keydownmoveright = 0
    elif getinput.keyDown("left"):
        keydownmoveleft += 1 
    elif getinput.keyDown("right"):
        keydownmoveright += 1

    if targetCol < 0:
        targetCol = 15
    elif targetCol > 15:
        targetCol = 0

    player["row"] = targetRow
    player["col"] = targetCol

    if tilemap.isDangerous(player["row"], player["col"]):
        player["lives"] -= 1

    print(dt)
    print(tracktime)

def draw(screen):
    graphics.drawTilemap(screen, tilemap._currentMap, areaKey)
    graphics.drawImage(screen, "background", 0, 0)
    graphics.drawImage(screen, "tree", player["row"], player["col"])

if __name__ == "__main__":
    core.init(width = 512, height = 576)
    initGame()

    core.run(updateGame, draw)
