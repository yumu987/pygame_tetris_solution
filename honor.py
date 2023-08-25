import pygame, sys
from pygame.locals import *
from blockGroup import *
import const

HONOR_LIST = [(1, 4), (1, 11), (1, 19), (1, 23), (1, 26), (1, 37), (2, 4), (2, 11), (2, 15), (2, 20), (2, 23), (2, 26), (2, 30), (2, 33), (2, 38), (3, 4), (3, 5), (3, 6), (3, 7), (3, 11), (3, 15), (3, 21), (3, 23), (3, 26), (3, 30), (3, 33), (3, 34), (3, 35), (3, 36), (3, 37), (4, 4), (4, 11), (4, 15), (4, 22), (4, 23), (4, 26), (4, 30), (4, 33), (4, 37), (5, 4), (5, 8), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (5, 18), (5, 23), (5, 26), (5, 27), (5, 28), (5, 29), (5, 30), (5, 33), (5, 38), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (6, 16), (6, 17), (6, 18), (6, 19), (6, 20), (6, 21), (6, 22), (6, 23), (6, 24), (6, 25), (6, 26), (6, 27), (6, 28), (6, 29), (6, 30), (6, 31), (6, 32), (6, 33), (6, 34), (6, 35), (6, 36), (6, 37), (6, 38), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), (7, 17), (7, 18), (7, 19), (7, 20), (7, 21), (7, 22), (7, 23), (7, 24), (7, 25), (7, 26), (7, 27), (7, 28), (7, 29), (7, 30), (7, 31), (7, 32), (7, 33), (7, 34), (7, 35), (7, 36), (7, 37), (7, 38), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (8, 19), (8, 20), (8, 21), (8, 22), (8, 23), (8, 24), (8, 25), (8, 26), (8, 27), (8, 28), (8, 29), (8, 30), (8, 31), (8, 32), (8, 33), (8, 34), (8, 35), (8, 36), (8, 37), (8, 38), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17), (9, 18), (9, 19), (9, 20), (9, 21), (9, 22), (9, 23), (9, 24), (9, 25), (9, 26), (9, 27), (9, 28), (9, 29), (9, 30), (9, 31), (9, 32), (9, 33), (9, 34), (9, 35), (9, 36), (9, 37), (9, 38), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (10, 17), (10, 18), (10, 19), (10, 20), (10, 21), (10, 22), (10, 23), (10, 24), (10, 25), (10, 26), (10, 27), (10, 28), (10, 29), (10, 30), (10, 31), (10, 32), (10, 33), (10, 34), (10, 35), (10, 36), (10, 37), (10, 38), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15), (11, 16), (11, 17), (11, 18), (11, 19), (11, 20), (11, 21), (11, 22), (11, 23), (11, 24), (11, 25), (11, 26), (11, 27), (11, 28), (11, 29), (11, 30), (11, 31), (11, 32), (11, 33), (11, 34), (11, 35), (11, 36), (11, 37), (11, 38), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15), (12, 16), (12, 17), (12, 18), (12, 19), (12, 20), (12, 21), (12, 22), (12, 23), (12, 24), (12, 25), (12, 26), (12, 27), (12, 28), (12, 29), (12, 30), (12, 31), (12, 32), (12, 33), (12, 34), (12, 35), (12, 36), (12, 37), (12, 38), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (13, 14), (13, 15), (13, 16), (13, 17), (13, 18), (13, 19), (13, 20), (13, 21), (13, 22), (13, 23), (13, 24), (13, 25), (13, 26), (13, 27), (13, 28), (13, 29), (13, 30), (13, 31), (13, 32), (13, 33), (13, 34), (13, 35), (13, 36), (13, 37), (13, 38), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19), (14, 20), (14, 21), (14, 22), (14, 23), (14, 24), (14, 25), (14, 26), (14, 27), (14, 28), (14, 29), (14, 30), (14, 31), (14, 32), (14, 33), (14, 34), (14, 35), (14, 36), (14, 37), (14, 38), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (15, 16), (15, 17), (15, 18), (15, 19), (15, 20), (15, 21), (15, 22), (15, 23), (15, 24), (15, 25), (15, 26), (15, 27), (15, 28), (15, 29), (15, 30), (15, 31), (15, 32), (15, 33), (15, 34), (15, 35), (15, 36), (15, 37), (15, 38)]

def generateHonorList():
    x = '''
    X      X       X   X  X          X 
    X      X   X    X  X  X   X  X    X
    XXXX   X   X     X X  X   X  XXXXX
    X      X   X      XX  X   X  X   X
    X   X  XXXXX  X    X  XXXXX  X    X
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''
    xsplit = x.split('\n')
    ans = []
    for row, v in enumerate(xsplit):
        for col, c in enumerate(v):
            if c == 'X':
                ans.append(  (row, col) )
    print(ans)
generateHonorList()


const.BLOCK_SIZE_W = 24
const.BLOCK_SIZE_H = 24
const.GAME_WIDTH_SIZE = 1280
const.GAME_HEIGHT_SIZE = 800
const.GAME_ROW = 300
const.GAME_COL = 200

class Game(pygame.sprite.Sprite):
    def getRelPos(self):
        return (100, 50)

    def __init__(self, surface):
        self.font = pygame.font.Font(None, 60)
        self.score = 0
        self.surface = surface
        self.gameOverImage = pygame.image.load( "../pic/lose.png" )
        self.isGameOver = False
        self.fixedBlockGroup = BlockGroup(const.BlockGroupType.FIXED, const.BLOCK_SIZE_W, const.BLOCK_SIZE_H, [], self.getRelPos())
        self.dropBlockGroup = None
        self.nextBlockGroup = None
        self.generateNextBlockGroup()

        for x in HONOR_LIST:
            color = const.BlockType.YELLOW
            if x[0] >= 6:
                color = const.BlockType.RED
            b = Block(color, 15+x[0], 1+x[1], 0, 0, 0, const.BLOCK_SIZE_W, const.BLOCK_SIZE_H, self.getRelPos())
            self.fixedBlockGroup.addBlocks(b)

    def generateDropBlockGroup(self):
        self.dropBlockGroup = self.nextBlockGroup
        self.dropBlockGroup.setBaseIndexes(0, 20)
        self.generateNextBlockGroup()
    
    def generateNextBlockGroup(self):
        conf = BlockGroup.GenerateBlockGroupConfig(0, const.GAME_COL + 3, 1)
        self.nextBlockGroup = BlockGroup(const.BlockGroupType.DROP, const.BLOCK_SIZE_W, const.BLOCK_SIZE_H, conf, self.getRelPos())

    def willCollide(self):
        hash = {}
        allIndexes = self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            hash[idx] = 1
        dropIndexes = self.dropBlockGroup.getNextBlockIndexes()

        for dropIdex in dropIndexes:
            if hash.get(dropIdex):
                return True
            if dropIdex[0] >= const.GAME_ROW:
                return True
        return False


    def update(self):
        if self.isGameOver:
            return 
        
        self.fixedBlockGroup.update()

        if self.fixedBlockGroup.IsEliminating():
            return

        if self.dropBlockGroup:
            self.dropBlockGroup.update()
        else:
            self.generateDropBlockGroup()
        
        if self.willCollide():
            blocks = self.dropBlockGroup.getBlocks()
            for blk in blocks:
                self.fixedBlockGroup.addBlocks(blk)
            self.dropBlockGroup.clearBlocks()
            self.dropBlockGroup = None
            if self.fixedBlockGroup.processEliminate():
                self.score += 1
        
        self.checkGameOver()

    def checkGameOver(self):
        allIndexes = self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            if idx[0] < 2:
                self.isGameOver = True


    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
        self.nextBlockGroup.draw(self.surface)
        
        if self.isGameOver:
            rect = self.gameOverImage.get_rect()
            rect.centerx = const.GAME_WIDTH_SIZE/2
            rect.centery = const.GAME_HEIGHT_SIZE/2
            self.surface.blit(self.gameOverImage, rect)

        # textImage = self.font.render('Score: ' + str(self.score), True, (255,255,255))
        # self.surface.blit(textImage, (10, 20))
