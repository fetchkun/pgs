# coding: utf-8

import sys
from math import sin, cos, radians, degrees, hypot, acos
import pygame
from pygame.locals import Rect, QUIT, KEYDOWN, K_w, K_e, K_r, K_v, KEYUP,\
                          K_UP, K_DOWN, K_RIGHT, K_LEFT, K_u, K_p, K_i, K_k,\
                          K_l, K_SPACE, K_j, K_1, K_2, K_n

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((1000, 660))
FPSCLOCK = pygame.time.Clock()

POLYGON = []
MOVE = [0, 0]
HERO = []
HEROP = []
HEROD = 0
HRAD = [0, 0]
DSC = []
eye_c = ()
eyevi = False
COUNTW = 0
yup = False
ydown = False
xleft = False
xright = False
qslo = False
ku = False
kd = False
kl = False
kr = False
KSPA = False
KEN = False
space = 1
u = 0
KMOVE = [0, 0]
BLO = [0, 0, 0, 0]
CLEAR = False
ENMO = []
ENMOFA = []
SOUND = []
SOEF = []
AT = []
REACO = []
DSCFA = []
DSCFA2 = []
COUNT = []
COUNT2 = []
COUNT3 = []
FOUND = []
vecboe = []
ENAMO = []
DSCAM = []
COUNTAM = []
MOVEHE = []
MOHIT = 0
VACAD2 = []
degs2 = []
for k in range(9):
    ENMO.append([0, 0])
    ENMOFA.append([0, 0])
    SOUND.append([0, 0])
    SOEF.append([0, 0, 0])
    AT.append(0)
    REACO.append(0)
    DSCFA.append(0)
    DSCFA2.append(500)
    COUNT.append(0)
    COUNT2.append(0)
    COUNT3.append(0)
    FOUND.append(0)
    vecboe.append([])
    ENAMO.append([])
    MOVEHE.append([])
    DSCAM.append([])
    for i in range(3):
        ENAMO[k].append([0, 0])
        MOVEHE[k].append([0, 0])
        DSCAM[k].append(0)
    COUNTAM.append([0, 0, 0])
    VACAD2.append([0, 0])
    degs2.append(0)
BLOC = []
OBC = []
i = 0
enter = False
TIMER = 0
TIMER2 = 0
TIMER3 = 0
ALERT = 0
STOP = True
blocg = []
FINISH = False
ALCOUNT = 0
ALTIMER = 60
COAL = 0
POR = []
DIS = []
SCOPE = False
SHOOT = False
STONE = []
STONUM = 2
HERO_POR = []
STCO = 0
STPO = []
STMO = []
STMOMAI = []
MOVEAD = []
COUREA = []
SHOCA = [0, 0]
GAMEOVER = False
LIME = 2
LIFECO = 3
EQUIP = 1
DACOU = 0
DAMAGE = False
EYE_SETl = []
EYE_SETr = []
MUSIC = True
MUSTART = True

def dot(vec1, vec2):
    return vec1[0]*vec2[0] + vec1[1]*vec2[1]

def rotate(pos, theta):
    cos_v = cos(radians(theta))
    sin_v = sin(radians(theta))
    return (cos_v*pos[0]-sin_v*pos[1], sin_v*pos[0]+cos_v*pos[1])

def degree(vec1, vec2, len12):
    if vec1[1] <= 0:
        if degrees(acos(dot(vec1, vec2)/len12)) == 360:
            return 0
        else:
            return degrees(acos(dot(vec1, vec2)/len12))
    elif vec1[1] > 0:
        if degrees(acos(dot(vec1, vec2)/len12))+180 == 360:
            return 0
        else:
            return degrees(acos(dot(vec1, vec2)/len12))+180

def degreex(vec1, vec2, len12, vecx):
    y = degrees(acos(dot(vec1, vec2)/len12))
    r = 360-degrees(acos(dot(vec1, vec2)/len12))
    if vecx[1] > 0:
        return r
    elif vecx[1] <= 0:
        return y

def deg_x(x, s, dsc):
    return x*cos(radians(s+dsc))

def deg_y(y, c, dsc):
    return -y*sin(radians(c+dsc))

class Back_ground:
    def block(self):
        global BLOC, BLO, blocg
        BLOC = []
        BLO = [0, 0, 0, 0]
        blocg = []
        for x in range(0, 30):
            BLOC.append([0, 0, 0, 0])

        """中腹部"""
        if 0 <= MOVE[1] and -300 <= MOVE[0]:
            x = True
        else:
            x = False
        blocim2(0, -300, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 0)

        if 0 <= MOVE[1] and -600 <= MOVE[0] <= 900:
            x = True
        else:
            x = False
        blocim2(200, -300, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 1)

        if 0 <= MOVE[1] and -700 <= MOVE[0] <= 700:
            x = True
        else:
            x = False
        blocim2(400, -300, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 2)

        if 0 <= MOVE[1] and -500 <= MOVE[0] <= 500:
            x = True
        else:
            x = False
        blocim2(600, -300, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 3)

        if -700 <= MOVE[0] <= 500:
            x = True
        else:
            x = False
        blocim2(600, -100, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 4)

        if MOVE[1] <= 660 and -300 <= MOVE[0]:
            x = True
        else:
            x = False
        blocim2(0, 100, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 5)

        if MOVE[1] <= 660 and -600 <= MOVE[0] <= 900:
            x = True
        else:
            x = False
        blocim2(200, 100, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 6)

        if MOVE[1] <= 660 and -700 <= MOVE[0] <= 700:
            x = True
        else:
            x = False
        blocim2(400, 50, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 7)

        if MOVE[1] <= 660 and -700 <= MOVE[0] <= 500:
            x = True
        else:
            x = False
        blocim2(600, 100, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 8)

        """下部"""
        if MOVE[1] <= 460 and -100 <= MOVE[0]:
            x = True
        else:
            x = False
        blocim2(-200, 300, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 9)

        if MOVE[1] <= 460 and -400 <= MOVE[0]:
            x = True
        else:
            x = False
        blocim2(0, 500, 300, 300,
                0, 150, 150, 0, 300, 150, 150, 300, 150, 150,
                320, 160, 160, 25, x, 10)

        if MOVE[1] <= 460 and -700 <= MOVE[0]:
            x = True
        else:
            x = False
        blocim2(300, 500, 300, 300,
                0, 150, 150, 0, 300, 150, 150, 300, 150, 150,
                320, 160, 160, 25, x, 11)

        if MOVE[1] <= 460 and -700 <= MOVE[0] <= 510:
            x = True
        else:
            x = False
        blocim2(600, 500, 300, 300,
                0, 150, 150, 0, 300, 150, 150, 300, 150, 150,
                320, 160, 160, 25, x, 12)

        if MOVE[1] <= 460 and -700 <= MOVE[0] <= 200:
            x = True
        else:
            x = False
        blocim2(900, 500, 300, 300,
                0, 150, 150, 0, 300, 150, 150, 300, 150, 150,
                320, 160, 160, 25, x, 13)

        if MOVE[1] <= 460 and -700 <= MOVE[0] <= -90:
            x = True
        else:
            x = False
        blocim2(1200, 300, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 14)

        """上の階"""
        if 190 <= MOVE[1] and -700 <= MOVE[0] <= 510:
            x = True
        else:
            x = False
        blocim2(1000, -500, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 15)

        if 3 <= MOVE[1] and -700 <= MOVE[0] <= 510:
            x = True
        else:
            x = False
        blocim2(1000, -300, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 16)

        if MOVE[1] <= 860 and -700 <= MOVE[0] <= 510:
            x = True
        else:
            x = False
        blocim2(1000, -100, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 17)

        if MOVE[1] <= 660 and -700 <= MOVE[0] <= 510:
            x = True
        else:
            x = False
        blocim2(1000, 100, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 18)

        """最上部"""
        if 390 <= MOVE[1] <= 1100 and -300 <= MOVE[0]:
            x = True
        else:
            x = False
        blocim2(0, -700, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 19)

        if 390 <= MOVE[1] <= 1100 and -600 <= MOVE[0] <= 900:
            x = True
        else:
            x = False
        blocim2(200, -700, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 20)

        if 390 <= MOVE[1] <= 1100 and -700 <= MOVE[0] <= 700:
            x = True
        else:
            x = False
        blocim2(400, -700, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 21)

        if 390 <= MOVE[1] <= 1100 and -500 <= MOVE[0] <= 500:
            x = True
        else:
            x = False
        blocim2(600, -700, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 22)

        if 390 <= MOVE[1] <= 1100 and -500 <= MOVE[0] <= 300:
            x = True
        else:
            x = False
        blocim2(800, -900, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 23)

        if 390 <= MOVE[1] <= 1100 and -500 <= MOVE[0] <= 300:
            x = True
        else:
            x = False
        blocim2(1000, -700, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 24)

        """最上奥"""
        if 390 <= MOVE[1] <= 1100 and -98 <= MOVE[0]:
            x = True
        else:
            x = False
        blocim2(-200, -500, 200, 200,
                0, 100, 100, 0, 200, 100, 100, 200, 100, 100,
                220, 110, 110, 25, x, 25)

        """障害物"""
        if MOVE[1] <= 660 and -700 <= MOVE[0] <= 500:
            x = True
        else:
            x = False
        blocim2(600, 300, 60, 60,
                0, 30, 30, 0, 60, 30, 30, 60, 50, 50,
                80, 40, 40, 10, x, 26)

        for a in BLOC:
            if BLO[0] != 1:
                BLO[0] += a[0]
            if BLO[1] != 1:
                BLO[1] += a[1]
            if BLO[2] != 1:
                BLO[2] += a[2]
            if BLO[3] != 1:
                BLO[3] += a[3]

def blocim2(x, y, w_c, h_c, cegy1, cegy2, cegy3, cegy4, cegy5, cegy6,
            cegy7, cegy8, cegy9, cegy10, gya1, gya2, gya3, gya4, r, num):
    global BLOC, blocg
    w = w_c
    h = h_c
    bloc = (x+MOVE[0]+KMOVE[0], y+MOVE[1]+KMOVE[1], w, h)
    if r == True:
        pygame.draw.rect(SURFACE, (0, 0, 0), bloc)
    """ブロックの各辺中央部の座標"""
    bloce = ([bloc[0]+cegy1, bloc[1]+cegy2], [bloc[0]+cegy3, bloc[1]+cegy4],
            [bloc[0]+cegy5, bloc[1]+cegy6], [bloc[0]+cegy7, bloc[1]+cegy8],
            [bloc[0]+cegy9, bloc[1]+cegy10])
    """ブロック四隅の座標"""
    blocg.append(((bloce[0][0], bloce[0][1]), (bloce[1][0], bloce[1][1]),
                  (bloc[0], bloc[1]), (bloc[0], bloc[1]+h),
                  (bloc[0]+w, bloc[1]), (bloc[0]+w, bloc[1]+h),
            (bloce[2][0], bloce[2][1]), (bloce[3][0], bloce[3][1]),
            (bloce[4][0], bloce[4][1])))
    vechc = []
    lenhb = []
    for i, k in blocg[num]:
        vechc.append((HERO[0]-i, HERO[1]-k))
    for i, k in vechc:
        lenhb.append(hypot(i, k))
    """HERO進行右への制御"""
    if (lenhb[6] <= gya1 or lenhb[1] <= gya3 or lenhb[7] <= gya3 or \
        lenhb[2] <= gya4 or lenhb[3] <= gya4) and\
       blocg[num][2][1] <= HERO[1] <= blocg[num][3][1] and HERO[0]-12 < blocg[num][2][0]:
       BLOC[num][0] = 1
    else:
        BLOC[num][0] = 0
    """HERO進行下への制御"""
    if (lenhb[7] <= gya1 or lenhb[0] <= gya2 or lenhb[6] <= gya2 or \
        lenhb[2] <= gya4 or lenhb[4] <= gya4) and \
       blocg[num][2][0] <= HERO[0] <= blocg[num][4][0] and HERO[1]-12 < blocg[num][2][1]:
       BLOC[num][1] = 1
    else:
        BLOC[num][1] = 0
    """HERO進行左への制御"""
    if (lenhb[0] <= gya1 or lenhb[1] <= gya3 or lenhb[7] <= gya3 or \
        lenhb[5] <= gya4 or lenhb[4] <= gya4) and \
       blocg[num][4][1] <= HERO[1] <= blocg[num][5][1] and blocg[num][4][0] < HERO[0]+12:
       BLOC[num][2] = 1
    else:
        BLOC[num][2] = 0
    """HERO進行上への制御"""
    if (lenhb[1] <= gya1 or lenhb[0] <= gya2 or lenhb[6] <= gya2 or \
        lenhb[5] <= gya4 or lenhb[3] <= gya4) and \
       blocg[num][3][0] <= HERO[0] <= blocg[num][5][0] and blocg[num][3][1] < HERO[1]+12:
       BLOC[num][3] = 1
    else:
        BLOC[num][3] = 0

def goll():
    global CLEAR, TIMER, TIMER2, TIMER3
    x = (100+round(MOVE[0]+KMOVE[0]), -400+round(MOVE[1]+KMOVE[1]))
    pygame.draw.circle(SURFACE, (250, 0, 0), x, 30)
    lenxc = hypot(HERO[0]-x[0], HERO[1]-x[1])
    if lenxc <= 35:
        CLEAR = True
    else:
        CLEAR = False

    """クリアタイムのカウント"""
    if CLEAR == False and GAMEOVER == False and KEN == False:
        if TIMER < 10:
            TIMER += 1
        elif TIMER == 10:
            TIMER = 0
            if TIMER2 < 59:
                TIMER2 += 1
            elif TIMER2 == 59:
                TIMER2 = 0
                TIMER3 += 1

    """クリアタイム表示"""
    pygame.draw.rect(SURFACE, (255, 255, 255), (8, 7, 83, 40))
    sysfont = pygame.font.SysFont(None, 50)
    if 1 <= TIMER3:
        if TIMER2 <= 9:
            mi = sysfont.render("{}'0{}\"".format(TIMER3, TIMER2), True, (250, 0, 0))
        else:
            mi = sysfont.render("{}'{}\"".format(TIMER3, TIMER2), True, (250, 0, 0))
    else:
        if TIMER2 <= 9:
            mi = sysfont.render("0'0{}\"".format(TIMER2), True, (250, 0, 0))
        else:
            mi = sysfont.render("0'{}\"".format(TIMER2), True, (250, 0, 0))
    mi_rect = mi.get_rect()
    mi_rect.center = (50, 30)
    SURFACE.blit(mi, mi_rect)

def rank():
    """敵の視野表示とクリアランク"""
    if eyevi == True:
        x = -6000
    else:
        x = 0
    y = (TIMER3 * 60 + TIMER2) * (-30)
    z = ALERT * (-2000)
    if u == 1 or u == 2:
        m = (1-LIME) * (-800)
    elif u == 0:
        m = (2-LIME) * (-800)
    total = 20000+x+y+z+m

    if u == 2:
        if 17780 <= total:
            k = "S"
        elif 16580 <= total < 17780:
            k = "A"
        elif 10530 <= total < 16580:
            k = "B"
        elif total < 10530:
            k = "C"
    elif u == 1:
        if 18770 <= total:
            k = "S"
        elif 17670 <= total < 18770:
            k = "A"
        elif 11640 <= total < 17670:
            k = "B"
        elif total < 11640:
            k = "C"
    elif u == 0:
        if 18890 <= total:
            k = "S"
        elif 17020 <= total < 18890:
            k = "A"
        elif 11020 <= total < 17020:
            k = "B"
        elif total < 11020:
            k = "C"

    if CLEAR == True:
        sysfont = pygame.font.SysFont(None, 100)
        mf = sysfont.render("{}".format("clear"), True, (0, 0, 250))
        mf_rect = mf.get_rect()
        mf_rect.center = (420, 280)
        SURFACE.blit(mf, mf_rect)
        mi = sysfont.render("{}".format("rank"), True, (0, 0, 250))
        mi_rect = mi.get_rect()
        mi_rect.center = (420, 350)
        SURFACE.blit(mi, mi_rect)

        sysfont = pygame.font.SysFont(None, 300)
        me = sysfont.render("{}".format(k), True, (0, 0, 250))
        me_rect = me.get_rect()
        me_rect.center = (580, 330)
        SURFACE.blit(me, me_rect)

def alert():
    global ALTIMER, ALCOUNT, FINISH, MUSIC, MUSTART
    if FINISH == True and KEN == False and u != 2 :
        if ALCOUNT == 0:
            ALCOUNT += 1
            if MUSTART == True:
                MUSIC = True
                MUSTART = False
        elif 0 < ALCOUNT < 10:
            ALCOUNT += 1
        elif ALCOUNT == 10:
            ALCOUNT = 0
            ALTIMER -= 1
            if ALTIMER == 0:
                FINISH = False
                MUSIC = True
                MUSTART = True
                ALTIMER = 60
    if FINISH == True and u != 2:
        pygame.draw.rect(SURFACE, (255, 0, 0), (448, 6, 104, 64), 5)
        pygame.draw.rect(SURFACE, (255, 255, 0), (450, 8, 100, 60))
        sysfont = pygame.font.SysFont(None, 90)
        mi = sysfont.render("{}".format(ALTIMER), True, (255, 0, 0))
        mi_rect = mi.get_rect()
        mi_rect.center = (500, 40)
        SURFACE.blit(mi, mi_rect)

    if u == 2:
        pygame.draw.rect(SURFACE, (255, 0, 0), (448, 6, 104, 64), 5)
        pygame.draw.rect(SURFACE, (255, 255, 0), (450, 8, 100, 60))
        sysfont = pygame.font.SysFont(None, 90)
        mi = sysfont.render("{}".format("60"), True, (255, 0, 0))
        mi_rect = mi.get_rect()
        mi_rect.center = (500, 40)
        SURFACE.blit(mi, mi_rect)

class Hero:
    def __init__(self, posx, posy):
        global HERO
        self.pos_x = posx+KMOVE[0]
        self.pos_y = posy+KMOVE[1]
        self.dsc = 270
        HERO = [self.pos_x, self.pos_y]
        self.vecsc = (100, 0)
        self.lensc = 100

    def hero_rad(self):
        global HRAD
        if KEN == False and CLEAR == False:
            if yup == True:
                if xleft == True:
                    HRAD = [-1, 1]
                elif xright == True:
                    HRAD = [1, 1]
                else:
                    HRAD = [0, 1]
            if ydown == True:
                if xleft == True:
                    HRAD = [-1, -1]
                elif xright == True:
                    HRAD = [1, -1]
                else:
                    HRAD = [0, -1]
            if xleft == True:
                if yup == True:
                    HRAD = [-1, 1]
                elif ydown == True:
                    HRAD = [-1, -1]
                else:
                    HRAD = [-1, 0]
            if xright == True:
                if yup == True:
                    HRAD = [1, 1]
                elif ydown == True:
                    HRAD = [1, -1]
                else:
                    HRAD = [1, 0]

        if HRAD[0] == 0:
            if HRAD[1] == 0:
                self.dsc = 270
            elif HRAD[1] == 1:
                self.dsc = 270 + 90
            elif HRAD[1] == -1:
                self.dsc = 270 + 270
        elif HRAD[0] == 1:
            if HRAD[1] == 0:
                self.dsc = 270
            elif HRAD[1] == 1:
                self.dsc = 270 + 45
            elif HRAD[1] == -1:
                self.dsc = 270 + 315
        elif HRAD[0] == -1:
            if HRAD[1] == 0:
                self.dsc = 270 + 180
            elif HRAD[1] == 1:
                self.dsc = 270 + 135
            elif HRAD[1] == -1:
                self.dsc = 270 + 225

    def figure(self):
        global HERO, HEROP, DACOU, DAMAGE
        vec = [(0, -15), (-15, 10), (-15, 25), (15, 25), (15, 10)]
        for i in vec:
            lene = (hypot(i[0], i[1]))
            lenes = (lene*self.lensc)
            degs = (degree(i, self.vecsc, lenes))
            HEROP.append((self.pos_x+deg_x(lene, degs, self.dsc),
                       self.pos_y+deg_y(lene, degs, self.dsc)))
            lene = 0
            lenes = 0
            degs = 0
        if DAMAGE == True:
            DACOU += 1
            if DACOU == 15:
                DAMAGE = False
                DACOU = 0
        if 0 <= DACOU < 3 or 8 <= DACOU < 11:
            pygame.draw.polygon(SURFACE, (0, 225, 0), HEROP)

    def shoot(self):
        global HERO_POR, STONUM, STONE, STCO, STMO, STPO, STMOMAI, MOVEAD
        if SCOPE == True and KEN == False:
            pygame.draw.circle(SURFACE, (245, 186, 0), (round(500+SHOCA[0]), round(330+SHOCA[1])),
                               20, 5)
        if SCOPE == True and SHOOT == True and KEN == False:
            if STCO == 0:
                pygame.draw.circle(SURFACE, (245, 186, 0), (round(500+SHOCA[0]), round(330+SHOCA[1])),
                               20, 5)
                if 0 < STONUM <= 2:
                    STONUM -= 1
                    STPO.append((round(500+SHOCA[0]), round(330+SHOCA[1])))
                    STMO.append((500, 330))
                    STMOMAI.append([0, 0])
                    MOVEAD.append([MOVE[0], MOVE[1]])
                    STCO += 1
        else:
            STCO = 0

        if 0 <= STONUM < 2:
            STONE = []
            HERO_POR = []
            for h in range(2-STONUM):
                HERO_POR.append((round(STPO[h][0]+MOVE[0]-MOVEAD[h][0]+KMOVE[0]), \
                                 round(STPO[h][1]+MOVE[1]-MOVEAD[h][1]+KMOVE[1])))
                STONE.append([round(STMO[h][0]+MOVE[0]-MOVEAD[h][0]+KMOVE[0]+STMOMAI[h][0]), \
                              round(STMO[h][1]+MOVE[1]-MOVEAD[h][1]+KMOVE[1]+STMOMAI[h][1])])
                stpr = (HERO[0]-HERO_POR[h][0], HERO[1]-HERO_POR[h][1])
                stce = (100, 0)
                lenpr = hypot(stpr[0], stpr[1])
                lence = 100
                lenprce = lenpr * lence
                if lenprce == 0:
                    lenprce = 0.01
                deg = acos(dot(stpr, stce)/lenprce)
                if HERO_POR[h][0]-10 <= STONE[h][0] <= HERO_POR[h][0]+10:
                    STMOMAI[h][0] = STMOMAI[h][0]
                elif STONE[h][0] < HERO_POR[h][0]:
                    STMOMAI[h][0] -= 19*cos(deg)
                elif STONE[h][0] > HERO_POR[h][0]:
                    STMOMAI[h][0] -= 19*cos(deg)

                if HERO_POR[h][1]-10 <= STONE[h][1] <= HERO_POR[h][1]+10:
                    STMOMAI[h][1] = STMOMAI[h][1]
                elif STONE[h][1] < HERO_POR[h][1]:
                    STMOMAI[h][1] += 19*sin(deg)
                elif STONE[h][1] > HERO_POR[h][1]:
                    STMOMAI[h][1] -= 19*sin(deg)
                pygame.draw.circle(SURFACE, (207, 186, 120), \
                                   (STONE[h][0], STONE[h][1]), \
                                   10)

        if EQUIP == 1:
            k = 0
            l = 0
            m = 0
        elif EQUIP == 2:
            k = 60
            l = 59
            m = 60
        if EQUIP == 1 or KEN == True:
            pygame.draw.rect(SURFACE, (100, 190, 255), (808, 600-k, 184, 52), 5)
            pygame.draw.rect(SURFACE, (0, 0, 0), (810, 602-l, 180, 48))
            sysfont = pygame.font.SysFont(None, 60)
            me = sysfont.render("decoy×{}".format(STONUM), True, (0, 120, 255))
            me_rect = me.get_rect()
            me_rect.center = (900, 627-m)
            SURFACE.blit(me, me_rect)

    def medicine(self):
        global LIME, LIFECO
        if KSPA == True and KEN == True:
            if LIME != 0:
                LIME -= 1
                if u == 1 or u == 2:
                    LIFECO = 3
                elif u == 0:
                    LIFECO = 5

        if EQUIP == 2:
            k = 0
            l = 0
            m = 0
        elif EQUIP == 1:
            k = 60
            l = 59
            m = 60
        if EQUIP == 2 or KEN == True:
            pygame.draw.rect(SURFACE, (100, 190, 255), (808, 600-k, 184, 52), 5)
            pygame.draw.rect(SURFACE, (0, 0, 0), (810, 602-l, 180, 48))
            sysfont = pygame.font.SysFont(None, 46)
            me = sysfont.render("medicine×{}".format(LIME), True, (0, 120, 255))
            me_rect = me.get_rect()
            me_rect.center = (900, 627-m)
            SURFACE.blit(me, me_rect)

    def life(self):
        global GAMEOVER, LIFECO, MOHIT, EQUIP, LIME, DAMAGE
        sysfont = pygame.font.SysFont(None, 30)
        mi = sysfont.render("{}".format("LIFE"), True, (120, 120, 120))
        mi_rect = mi.get_rect()
        mi_rect.center = (30, 610)
        SURFACE.blit(mi, mi_rect)
        if u == 1 or u == 2:
            pygame.draw.rect(SURFACE, (120, 120, 120), (2, 620, 180, 30))
            if 1 <= MOHIT:
                if LIFECO != 0:
                    LIFECO -= MOHIT
                DAMAGE = True
            if LIFECO <= 0:
                if LIME == 0:
                    GAMEOVER = True
                elif EQUIP != 2:
                    GAMEOVER = True
                elif LIME != 0 and EQUIP == 2:
                    LIME -= 1
                    LIFECO = 3
            for k in range(LIFECO):
                pygame.draw.rect(SURFACE, (255, 255, 255), (7+57*k, 623, 53, 24))
        elif u == 0:
            pygame.draw.rect(SURFACE, (120, 120, 120), (2, 620, 180, 30))
            if 1 <= MOHIT:
                if LIFECO != 0:
                    LIFECO -= MOHIT
                DAMAGE = True
            if LIFECO <= 0:
                if LIME == 0:
                    GAMEOVER = True
                elif EQUIP != 2:
                    GAMEOVER = True
                elif LIME != 0 and EQUIP == 2:
                    LIME -= 1
                    LIFECO = 5

            for k in range(LIFECO):
                pygame.draw.rect(SURFACE, (255, 255, 255), (7+34*k, 623, 30, 24))

        if GAMEOVER == True:
            sysfont = pygame.font.SysFont(None, 200)
            me = sysfont.render("{}".format("GAME OVER"), True, (225, 0, 0))
            me_rect = me.get_rect()
            me_rect.center = (500, 330)
            SURFACE.blit(me, me_rect)

        MOHIT = 0

class Enemy:
    def __init__(self, obc, num, n):
        global vecboe, OBC, DSC
        OBC.append((obc[0]+MOVE[0]+ENMO[num][0]+KMOVE[0], obc[1]+MOVE[1]+ENMO[num][1]+KMOVE[1]))
        self.num = num
        self.vecfc = (200, 0)
        self.lenfc = 200
        self.vecsc = (100, 0)
        self.lensc = 100
        for k in n:
            vecboe[self.num].append((blocg[k][8][0]-OBC[self.num][0], blocg[k][8][1]-OBC[self.num][1]))

    def figure(self, fig):
        global POLYGON
        vec = [(0, -15), (-15, 10), (-15, 25), (15, 25), (15, 10)]
        polygon_c = []
        for i in vec:
            lene = (hypot(i[0], i[1]))
            lenes = (lene * self.lensc)
            degs = (degree(i, self.vecsc, lenes))
            polygon_c.append((OBC[self.num][0]+deg_x(lene, degs, DSC[self.num]),
                       OBC[self.num][1]+deg_y(lene, degs, DSC[self.num])))
            lene = 0
            lenes = 0
            degs = 0
        POLYGON.append(polygon_c)
        if fig == True:
            pygame.draw.polygon(SURFACE, (150, 0, 150), POLYGON[self.num])

    def shoot_ene(self, num, bl_n):
        global ENAMO, DSCAM, COUNTAM, MOVEHE, MOHIT
        amo = 5
        amsp = 20
        """第一弾"""
        if bl_n[0] != 50:
            for j in bl_n:
                if blocg[j][3][0] <= ENAMO[num][0][0] <= blocg[j][5][0] and \
                   blocg[j][2][1] <= ENAMO[num][0][1] <= blocg[j][3][1]:
                   ENAMO[num][0] = [0, 0]
                   COUNTAM[num][0] = 0

        if COUNTAM[num][0] == 0:
            MOVEHE[num][0][0] = MOVE[0]
            MOVEHE[num][0][1] = MOVE[1]
            ENAMO[num][0] = [round(OBC[num][0]), round(OBC[num][1])]
            DSCAM[num][0] = DSC[num]+90
            pygame.draw.circle(SURFACE, (245, 186, 0), ENAMO[num][0], amo)
            COUNTAM[num][0] += 1

        elif 0 < COUNTAM[num][0] < 14:
            if HERO[0]-15 < ENAMO[num][0][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][0][1] < HERO[1]+15:
                MOHIT += 1
                ENAMO[num][0] = [0, 0]
                COUNTAM[num][0] = 0
            else:
                if KEN == False:
                    ENAMO[num][0][0] += amsp*cos(radians(DSCAM[num][0]))
                    ENAMO[num][0][1] -= amsp*sin(radians(DSCAM[num][0]))
                    COUNTAM[num][0] += 1
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                  (round(ENAMO[num][0][0]+MOVE[0]-MOVEHE[num][0][0]+KMOVE[0]),\
                                   round(ENAMO[num][0][1]+MOVE[1]-MOVEHE[num][0][1]+KMOVE[1])), amo)


        elif COUNTAM[num][0] == 14:
            if HERO[0]-15 < ENAMO[num][0][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][0][1] < HERO[1]+15:
                MOHIT += 1
            else:
                if KEN == False:
                    ENAMO[num][0][0] += amsp*cos(radians(DSCAM[num][0]))
                    ENAMO[num][0][1] -= amsp*sin(radians(DSCAM[num][0]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                  (round(ENAMO[num][0][0]+MOVE[0]-MOVEHE[num][0][0]+KMOVE[0]),\
                                   round(ENAMO[num][0][1]+MOVE[1]-MOVEHE[num][0][1]+KMOVE[1])), amo)
                if KEN == False:
                    ENAMO[num][0] = [0, 0]
                    COUNTAM[num][0] = 0

        """第二弾"""
        if bl_n[0] != 50:
            for j in bl_n:
                if blocg[j][3][0] <= ENAMO[num][1][0] <= blocg[j][5][0] and \
                   blocg[j][2][1] <= ENAMO[num][1][1] <= blocg[j][3][1]:
                   ENAMO[num][1] = [0, 0]
                   COUNTAM[num][1] = 0

        if 0 <= COUNTAM[num][1] < 5:
            COUNTAM[num][1] += 1

        elif COUNTAM[num][1] == 5:
            MOVEHE[num][1][0] = MOVE[0]
            MOVEHE[num][1][1] = MOVE[1]
            ENAMO[num][1] = [round(OBC[num][0]), round(OBC[num][1])]
            DSCAM[num][1] = DSC[num]+90
            pygame.draw.circle(SURFACE, (245, 186, 0), ENAMO[num][1], amo)
            COUNTAM[num][1] += 1

        elif 5 < COUNTAM[num][1] < 20:
            if HERO[0]-15 < ENAMO[num][1][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][1][1] < HERO[1]+15:
                MOHIT += 1
                ENAMO[num][1] = [0, 0]
                COUNTAM[num][1] = 0
            else:
                if KEN == False:
                    ENAMO[num][1][0] += amsp*cos(radians(DSCAM[num][1]))
                    ENAMO[num][1][1] -= amsp*sin(radians(DSCAM[num][1]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                              (round(ENAMO[num][1][0]+MOVE[0]-MOVEHE[num][1][0]+KMOVE[0]), \
                               round(ENAMO[num][1][1]+MOVE[1]-MOVEHE[num][1][1]+KMOVE[1])), amo)
                if KEN == False:
                    COUNTAM[num][1] += 1

        elif COUNTAM[num][1] == 20:
            if HERO[0]-15 < ENAMO[num][0][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][0][1] < HERO[0]+15:
                MOHIT += 1
            else:
                if KEN == False:
                    ENAMO[num][1][0] += amsp*cos(radians(DSCAM[num][1]))
                    ENAMO[num][1][1] -= amsp*sin(radians(DSCAM[num][1]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][1][0]+MOVE[0]-MOVEHE[num][1][0]+KMOVE[0]), \
                                 round(ENAMO[num][1][1]+MOVE[1]-MOVEHE[num][1][1]+KMOVE[1])), amo)
            if KEN == False:
                ENAMO[num][1] = [0, 0]
                COUNTAM[num][1] = 0

        """第三弾"""
        if bl_n[0] != 50:
            for j in bl_n:
                if blocg[j][3][0] <= ENAMO[num][2][0] <= blocg[j][5][0] and \
                   blocg[j][2][1] <= ENAMO[num][2][1] <= blocg[j][3][1]:
                   ENAMO[num][2] = [0, 0]
                   COUNTAM[num][2] = 0

        if 0 <= COUNTAM[num][2] < 10:
            COUNTAM[num][2] += 1

        elif COUNTAM[num][2] == 10:
            MOVEHE[num][2][0] = MOVE[0]
            MOVEHE[num][2][1] = MOVE[1]
            ENAMO[num][2] = [round(OBC[num][0]), round(OBC[num][1])]
            DSCAM[num][2] = DSC[num]+90
            pygame.draw.circle(SURFACE, (245, 186, 0), ENAMO[num][2], amo)
            COUNTAM[num][2] += 1

        elif 10 < COUNTAM[num][2] < 25:
            if HERO[0]-15 < ENAMO[num][2][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][2][1] < HERO[1]+15:
                MOHIT += 1
                ENAMO[num][2] = [0, 0]
                COUNTAM[num][2] = 0
            else:
                if KEN == False:
                    ENAMO[num][2][0] += amsp*cos(radians(DSCAM[num][2]))
                    ENAMO[num][2][1] -= amsp*sin(radians(DSCAM[num][2]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][2][0]+MOVE[0]-MOVEHE[num][2][0]+KMOVE[0]), \
                                 round(ENAMO[num][2][1]+MOVE[1]-MOVEHE[num][2][1]+KMOVE[1])), amo)
                if KEN == False:
                    COUNTAM[num][2] += 1

        elif COUNTAM[num][2] == 25:
            if HERO[0]-15 < ENAMO[num][2][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][2][1] < HERO[1]+15:
                MOHIT += 1
            else:
                if KEN == False:
                    ENAMO[num][2][0] += amsp*cos(radians(DSCAM[num][2]))
                    ENAMO[num][2][1] -= amsp*sin(radians(DSCAM[num][2]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][2][0]+MOVE[0]-MOVEHE[num][2][0]+KMOVE[0]), \
                                 round(ENAMO[num][2][1]+MOVE[1]-MOVEHE[num][2][1]+KMOVE[1])), amo)
            if KEN == False:
                ENAMO[num][2] = [0, 0]
                COUNTAM[num][2] = 0

    def shoot_ene_ob(self, num, bl_n):
        global ENAMO, DSCAM, COUNTAM, MOHIT
        amo = 5
        amsp = 20
        """第一弾"""
        if bl_n[0] != 50:
            for j in bl_n:
                if blocg[j][3][0] <= ENAMO[num][0][0] <= blocg[j][5][0] and \
                   blocg[j][2][1] <= ENAMO[num][0][1] <= blocg[j][3][1]:
                   ENAMO[num][0] = [0, 0]
                   COUNTAM[num][0] = 0

        if 0 < COUNTAM[num][0] < 14:
            if HERO[0]-15 < ENAMO[num][0][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][0][1] < HERO[1]+15:
                MOHIT += 1
                ENAMO[num][0] = [0, 0]
                COUNTAM[num][0] = 0
            else:
                if KEN == False:
                    ENAMO[num][0][0] += amsp*cos(radians(DSCAM[num][0]))
                    ENAMO[num][0][1] -= amsp*sin(radians(DSCAM[num][0]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][0][0]+MOVE[0]-MOVEHE[num][0][0]+KMOVE[0]),\
                                 round(ENAMO[num][0][1]+MOVE[1]-MOVEHE[num][0][1]+KMOVE[1])), amo)
                if KEN == False:
                    COUNTAM[num][0] += 1
        elif COUNTAM[num][0] == 14:
            if HERO[0]-15 < ENAMO[num][0][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][0][1] < HERO[1]+15:
                MOHIT += 1
            else:
                if KEN == False:
                    ENAMO[num][0][0] += amsp*cos(radians(DSCAM[num][0]))
                    ENAMO[num][0][1] -= amsp*sin(radians(DSCAM[num][0]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][0][0]+MOVE[0]-MOVEHE[num][0][0]+KMOVE[0]),\
                                 round(ENAMO[num][0][1]+MOVE[1]-MOVEHE[num][0][1]+KMOVE[1])), amo)
            if KEN == False:
                ENAMO[num][0] = [0, 0]
                COUNTAM[num][0] = 0

        """第二弾"""
        if bl_n[0] != 50:
            for j in bl_n:
                if blocg[j][3][0] <= ENAMO[num][1][0] <= blocg[j][5][0] and \
                   blocg[j][2][1] <= ENAMO[num][1][1] <= blocg[j][3][1]:
                   ENAMO[num][1] = [0, 0]
                   COUNTAM[num][1] = 0

        if 5 < COUNTAM[num][1] < 20:
            if HERO[0]-15 < ENAMO[num][1][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][1][1] < HERO[1]+15:
                MOHIT += 1
                ENAMO[num][1] = [0, 0]
                COUNTAM[num][1] = 0
            else:
                if KEN == False:
                    ENAMO[num][1][0] += amsp*cos(radians(DSCAM[num][1]))
                    ENAMO[num][1][1] -= amsp*sin(radians(DSCAM[num][1]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][1][0]+MOVE[0]-MOVEHE[num][1][0]+KMOVE[0]), \
                                 round(ENAMO[num][1][1]+MOVE[1]-MOVEHE[num][1][1]+KMOVE[1])), amo)
                if KEN == False:
                    COUNTAM[num][1] += 1
        elif COUNTAM[num][1] == 20:
            if HERO[0]-15 < ENAMO[num][1][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][1][1] < HERO[1]+15:
                MOHIT += 1
            else:
                if KEN == False:
                    ENAMO[num][1][0] += amsp*cos(radians(DSCAM[num][1]))
                    ENAMO[num][1][1] -= amsp*sin(radians(DSCAM[num][1]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][1][0]+MOVE[0]-MOVEHE[num][1][0]+KMOVE[0]), \
                                 round(ENAMO[num][1][1]+MOVE[1]-MOVEHE[num][1][1]+KMOVE[1])), amo)
            if KEN == False:
                ENAMO[num][1] = [0, 0]
                COUNTAM[num][1] = 0

        """第三弾"""
        if bl_n[0] != 50:
            for j in bl_n:
                if blocg[j][3][0] <= ENAMO[num][2][0] <= blocg[j][5][0] and \
                   blocg[j][2][1] <= ENAMO[num][2][1] <= blocg[j][3][1]:
                   ENAMO[num][2] = [0, 0]
                   COUNTAM[num][2] = 0

        if 10 < COUNTAM[num][2] < 25:
            if HERO[0]-15 < ENAMO[num][2][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][2][1] < HERO[1]+15:
                MOHIT += 1
                ENAMO[num][2] = [0, 0]
                COUNTAM[num][2] = 0
            else:
                if KEN == False:
                    ENAMO[num][2][0] += amsp*cos(radians(DSCAM[num][2]))
                    ENAMO[num][2][1] -= amsp*sin(radians(DSCAM[num][2]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][2][0]+MOVE[0]-MOVEHE[num][2][0]+KMOVE[0]), \
                                 round(ENAMO[num][2][1]+MOVE[1]-MOVEHE[num][2][1]+KMOVE[1])), amo)
                if KEN == False:
                    COUNTAM[num][2] += 1
        elif COUNTAM[num][2] == 25:
            if HERO[0]-15 < ENAMO[num][2][0] < HERO[0]+15 and\
               HERO[1]-25 < ENAMO[num][2][1] < HERO[1]+15:
                MOHIT += 1
            else:
                if KEN == False:
                    ENAMO[num][2][0] += amsp*cos(radians(DSCAM[num][2]))
                    ENAMO[num][2][1] -= amsp*sin(radians(DSCAM[num][2]))
                pygame.draw.circle(SURFACE, (245, 186, 0), \
                                (round(ENAMO[num][2][0]+MOVE[0]-MOVEHE[num][2][0]+KMOVE[0]), \
                                 round(ENAMO[num][2][1]+MOVE[1]-MOVEHE[num][2][1]+KMOVE[1])), amo)
            if KEN == False:
                ENAMO[num][2] = [0, 0]
                COUNTAM[num][2] = 0

    def eyev(self, e, r_c, num, bl_n):
        global eyevi, eye_c, jrad1, jrad2, ALERT, AT, FINISH, COAL, \
               ALTIMER, ALCOUNT, COUNT3, FOUND, DSCFA2, SOEF, EYE_SET, EYE_SETl, \
               EYE_SETr, EYE_CO
        eye1 = e[0]
        eye2 = e[1]
        rad = r_c[1]
        r = r_c[0]
        eye = (eye1[0]+OBC[self.num][0], eye1[1]+OBC[self.num][1])
        eye_c = (r+OBC[self.num][0], r+OBC[self.num][1], abs(r)*2, abs(r)*2)

        pygame.draw.rect(SURFACE, (255, 255, 255), (890, 1, 110, 40))
        sysfont = pygame.font.SysFont(None, 40)
        if eyevi == True:
            pygame.draw.arc(SURFACE, (0, 0, 225), eye_c, radians(56+DSC[self.num]),
                            radians(124+DSC[self.num]), rad)
            mv = sysfont.render("{}".format("on"), True, (250, 125, 0))
        else:
            mv = sysfont.render("{}".format("off"), True, (250, 125, 0))
        mv_rect = mv.get_rect()
        mv_rect.center = (950, 33)
        SURFACE.blit(mv, mv_rect)

        """発見時目で追いかけ、発砲"""
        vecs = (5, 0)
        vec = (HERO[0]-OBC[num][0], HERO[1]-OBC[num][1])
        leno = hypot(vec[0], vec[1])
        lenos = leno * 5
        if lenos == 0:
            lenos = 0.01
        degs = degrees(acos(dot(vec, vecs)/lenos))
        vecad = (vecs[0]-vec[0], vecs[1]-vec[1])

        eyevi2_l = []
        for k in EYE_SETl:
            eyevi1 = []
            ind2 = EYE_SETl.index(k)
            for i in k:
                eyev_fa = [round(OBC[self.num][0]+deg_x(i[0], i[1], DSC[self.num])),
                         round(OBC[self.num][1]+deg_y(i[0], i[1], DSC[self.num]))]
                ind1 = k.index(i)
                if ind2 != 0:
                    cou = 0
                    for j in eyevi2_l[ind2-1]:
                        if j[3] == 1:
                            cou += 1
                    if 1 <= cou:
                        par = 1
                    else:
                        par = 0
                else:
                    par = 0
                bl_co1 = 0
                if ind1 == 0:
                    bl_co1 = 0
                else:
                    if eyevi1[ind1-1][3] == 0 and par == 0:
                        bl_co1 = 0
                    elif eyevi1[ind1-1][3] == 1 or par == 1:
                        bl_co1 = 1
                if bl_n[0] != 50:
                    for j in bl_n:
                        if blocg[j][3][0] <= eyev_fa[0] <= blocg[j][5][0] and \
                           blocg[j][2][1] <= eyev_fa[1] <= blocg[j][3][1]:
                            bl_co1 = 1
                        eyevi1.append([eyev_fa[0], eyev_fa[1], 0, bl_co1])
                elif bl_n[0] == 50:
                    eyevi1.append([eyev_fa[0], eyev_fa[1], 0, bl_co1])
            eyevi2_l.append(eyevi1)

        eyevi2_r = []
        for k in EYE_SETr:
            eyevi1 = []
            ind2 = EYE_SETr.index(k)
            for i in k:
                eyev_fa = [round(OBC[self.num][0]+deg_x(i[0], i[1], DSC[self.num])),
                         round(OBC[self.num][1]+deg_y(i[0], i[1], DSC[self.num]))]
                ind1 = k.index(i)
                if ind2 != 0:
                    cou = 0
                    for j in eyevi2_l[ind2-1]:
                        if j[3] == 1:
                            cou += 1
                    if 1 <= cou:
                        par = 1
                    else:
                        par = 0
                else:
                    par = 0
                bl_co1 = 0
                if ind1 == 0:
                    bl_co1 = 0
                else:
                    if eyevi1[ind1-1][3] == 0 and par == 0:
                        bl_co1 = 0
                    elif par == 1 or eyevi1[ind1-1][3] == 1:
                        bl_co1 = 1
                if bl_n[0] != 50:
                    for j in bl_n:
                        if blocg[j][3][0] <= eyev_fa[0] <= blocg[j][5][0] and \
                           blocg[j][2][1] <= eyev_fa[1] <= blocg[j][3][1]:
                            bl_co1 = 1
                        eyevi1.append([eyev_fa[0], eyev_fa[1], 0, bl_co1])
                elif bl_n[0] == 50:
                    eyevi1.append([eyev_fa[0], eyev_fa[1], 0, bl_co1])
            eyevi2_r.append(eyevi1)

        amo_co = 0
        for k in eyevi2_l:
            for i in k:
                if i[0]-10 <= HERO[0] <= i[0]+10 and\
                   i[1]-10 <= HERO[1] <= i[1]+10:
                   indk = eyevi2_l.index(k)
                   indi = k.index(i)
                   if i[3] == 0 and CLEAR == False and GAMEOVER == False:
                       eyevi2_l[indk][indi][2] = 1
                       if eyevi2_l[indk][indi][2] == 1:
                           FINISH = True
                           amo_co += 1
        for k in eyevi2_r:
            for i in k:
                if i[0]-10 <= HERO[0] <= i[0]+10 and\
                   i[1]-10 <= HERO[1] <= i[1]+10:
                   indk = eyevi2_r.index(k)
                   indi = k.index(i)
                   if i[3] == 0 and CLEAR == False and GAMEOVER == False:
                       eyevi2_r[indk][indi][2] = 1
                       if eyevi2_r[indk][indi][2] == 1:
                           FINISH = True
                           amo_co += 1

        if 1 <= amo_co:
            self.shoot_ene(self.num, bl_n)
            sysfont = pygame.font.SysFont(None, 180)
            mj = sysfont.render("{}".format("!"), True, (225, 0, 0))
            mj_rect = mj.get_rect()
            mj_rect.center = (500, 330)
            SURFACE.blit(mj, mj_rect)
            AT[self.num] += 1
            if AT[self.num] == 1:
                ALERT += 1
            if COAL != ALERT:
                ALTIMER = 60
                ALCOUNT = 0
                COAL = ALERT
            FOUND[num] = 1
            if COUNT3[num] == 0:
                DSCFA2[num] = DSC[num]
                COUNT3[num] += 1
            if vecad[1] > 0:
                DSC[num] = (degs-90)
            elif vecad[1] <= 0:
                DSC[num] = (270-degs)
        else:
            if COUNTAM != 0:
                self.shoot_ene_ob(self.num, bl_n)
            AT[self.num] = 0
            if DSCFA2[num] != 500:
                DSC[num] = DSCFA2[num]
            COUNT3[num] = 0
            FOUND[num] = 0
            if qslo == False and leno <= 70 and SOEF[num][0] == 0 and \
               SOEF[num][1] == 0 and (yup == True or ydown == True or\
               xright == True or xleft == True):
                SOEF[num][2] = 1
            DSCFA2[num] = 500

        """for k in eyevi2_l:
            for i in k:
                if i[3] == 0:
                    pygame.draw.circle(SURFACE, (225, 0, 0), (i[0], i[1]), 10)
        for k in eyevi2_r:
            for i in k:
                if i[3] == 0:
                    pygame.draw.circle(SURFACE, (225, 0, 0), (i[0], i[1]), 10)"""

    def move(self, num):
        global ENMOFA,  ENMO
        if ENMOFA[num][0] != 0 or ENMOFA[num][1] != 0:
            if ENMOFA[num][0] > 0 and ENMOFA[num][1] > 0:
                DSC[num] = 225
            elif ENMOFA[num][0] > 0 and ENMOFA[num][1] < 0:
                DSC[num] = 315
            elif ENMOFA[num][0] < 0 and ENMOFA[num][1] > 0:
                DSC[num] = 125
            elif ENMOFA[num][0] < 0 and ENMOFA[num][1] < 0:
                DSC[num] = 45
            elif ENMOFA[num][0] > 0:
                DSC[num] = 270
            elif ENMOFA[num][1] > 0:
                DSC[num] = 180
            elif ENMOFA[num][0] < 0:
                DSC[num] = 90
            elif ENMOFA[num][1] < 0:
                DSC[num] = 0

            ENMO[num][0] += ENMOFA[num][0]
            ENMO[num][1] += ENMOFA[num][1]

    def react(self, num):
        global COUREA, SOUND, COUNT2, DSC, REACO, DSCFA, VACAD2, degs2, SOEF
        if 0 <= STONUM < 2:
            for h in range(2-STONUM):
                vecs = (5, 0)
                vec = (HERO_POR[h][0]-OBC[num][0], HERO_POR[h][1]-OBC[num][1])
                leno = hypot(vec[0], vec[1])
                lenos = leno * 5
                degs = degrees(acos(dot(vec, vecs)/lenos))
                vecad = (vecs[0]-vec[0], vecs[1]-vec[1])
                if lenos == 0:
                    lenos = 0.01
                if HERO_POR[h][0]-10 <= STONE[h][0] <= HERO_POR[h][0]+10 and\
                   HERO_POR[h][1]-10 <= STONE[h][1] <= HERO_POR[h][1]+10:
                   if SOUND[num][h] == 0 :
                       if leno < 120:
                           SOEF[num][h] = 1
                           SOUND[num][h] += 1

                if SOEF[num][h] == 1 and leno <= 120:
                    REACO[num] = 1
                    sysfont = pygame.font.SysFont(None, 60)
                    mo = sysfont.render("?", True, (225, 0, 0))
                    mo_rect = mo.get_rect()
                    mo_rect.center = (OBC[num][0], OBC[num][1])
                    SURFACE.blit(mo, mo_rect)
                    if COUNT2[num] == 0:
                        DSCFA[num] = DSC[num]
                        if vecad[1] > 0:
                            DSC[num] = (degs-90)
                        elif vecad[1] <= 0:
                            DSC[num] = (270-degs)
                        if KEN == False:
                            COUNT2[num] += 1
                    elif 0 < COUNT2[num] < 100:
                        if KEN == False:
                            COUNT2[num] += 1
                    elif COUNT2[num] == 100:
                        if KEN == False:
                            COUNT2[num] = 0
                            SOEF[num][h] = 0
                            REACO[num] = 0
                            DSC[num] = DSCFA[num]

        if SOEF[num][2] == 1 and FOUND[num] == 0:
            sysfont = pygame.font.SysFont(None, 60)
            mo = sysfont.render("?", True, (225, 0, 0))
            mo_rect = mo.get_rect()
            mo_rect.center = (OBC[num][0], OBC[num][1])
            SURFACE.blit(mo, mo_rect)
            if COUNT2[num] == 0:
                DSCFA[num] = DSC[num]
                REACO[num] = 1
                pohe0 = HERO[0]
                pohe1 = HERO[1]
                vecs2 = (5, 0)
                vec2 = (pohe0-OBC[num][0], pohe1-OBC[num][1])
                leno2 = hypot(vec2[0], vec2[1])
                lenos2 = leno2 * 5
                if lenos2 == 0:
                    lenos2 = 0.01
                degs2[num] = degrees(acos(dot(vec2, vecs2)/lenos2))
                VACAD2[num] = (vecs2[0]-vec2[0], vecs2[1]-vec2[1])
                COUNT2[num] += 1
            elif 0 < COUNT2[num] < 7:
                if KEN == False:
                    COUNT2[num] += 1
            elif 7 <= COUNT2[num] < 100:
                if VACAD2[num][1] > 0:
                    DSC[num] = (degs2[num]-90)
                elif VACAD2[num][1] <= 0:
                    DSC[num] = (270-degs2[num])
                if KEN == False:
                    COUNT2[num] += 1
            elif COUNT2[num] == 100:
                if KEN == False:
                    SOEF[num][2] = 0
                    REACO[num] = 0
                    DSC[num] = DSCFA[num]
                    COUNT2[num] = 0

def block_escape(num, blocn):
    global DIS
    xr = (OBC[num][0]-blocg[blocn[0]][0][0], OBC[num][1]-blocg[blocn[0]][0][1])
    xd = (OBC[num][0]-blocg[blocn[0]][1][0], OBC[num][1]-blocg[blocn[0]][1][1])
    xl = (OBC[num][0]-blocg[blocn[0]][6][0], OBC[num][1]-blocg[blocn[0]][6][1])
    xu = (OBC[num][0]-blocg[blocn[0]][7][0], OBC[num][1]-blocg[blocn[0]][7][1])
    disr = hypot(xr[0], xr[1])
    disd = hypot(xd[0], xd[1])
    disl = hypot(xl[0], xl[1])
    disu = hypot(xu[0], xu[1])
    del blocn[0]
    for n in blocn:
        xr = (OBC[num][0]-blocg[n][0][0], OBC[num][1]-blocg[n][0][1])
        xd = (OBC[num][0]-blocg[n][1][0], OBC[num][1]-blocg[n][1][1])
        xl = (OBC[num][0]-blocg[n][6][0], OBC[num][1]-blocg[n][6][1])
        xu = (OBC[num][0]-blocg[n][7][0], OBC[num][1]-blocg[n][7][1])
        if hypot(xr[0], xr[1]) < disr:
            disr = hypot(xr[0], xr[1])
        if hypot(xd[0], xd[1]) < disd:
            disd = hypot(xd[0], xd[1])
        if hypot(xl[0], xl[1]) < disl:
            disl = hypot(xl[0], xl[1])
        if hypot(xu[0], xu[1]) < disu:
            disu = hypot(xu[0], xu[1])

    DIS.append((disr, disd, disl, disu))

def porpose(x, y):
    global POR
    POR.append((x+MOVE[0]+KMOVE[0], y+MOVE[1]+KMOVE[1]))

def difficalty():
    sysfont = pygame.font.SysFont(None, 40)
    if u == 0:
        mj = sysfont.render("{}".format("normal"), True, (250, 125, 0))
    elif u == 1:
        mj = sysfont.render("{}".format("hard"), True, (250, 125, 0))
    elif u == 2:
        mj = sysfont.render("{}".format("extreme"), True, (250, 125, 0))
    mj_rect = mj.get_rect()
    mj_rect.center = (948, 10)
    SURFACE.blit(mj, mj_rect)

def ene_move():
    global ENMOFA, COUNT, OBC, vecboe, POR, DIS, ENMO
    r = ((-100, -100), (100, -100))
    if u == 0:
        r_c = (-140, 130)
    elif u == 1 or u == 2:
        r_c = (-220, 200)

    num1 = 0
    n1 = [26]
    bl_n1 = [26]

    enemy1 = Enemy((830, 450), num1, n1)
    if MOVE[1] < 540:
        fig1 = True
    else:
        fig1 = False
    enemy1.figure(fig1)
    for k in n1:
        ind = n1.index(k)
        r_c1 = r_c

    if MOVE[1] < 540:
        enemy1.eyev(r, r_c1, num1, bl_n1)
        enemy1.react(num1)
    if REACO[num1] == 0 and FOUND[num1] == 0:
        if COUNT[num1] < 70:
            if KEN == False:
                COUNT[num1] += 1
            DSC[num1] = 90
        elif 70 <= COUNT[num1] < 270:
            if KEN == False:
                COUNT[num1] += 1
                ENMO[num1][0] -= 2
        elif 270 <= COUNT[num1] < 370:
            if KEN == False:
                COUNT[num1] += 1
            DSC[num1] = 0
        elif 370 <= COUNT[num1] < 570:
            if KEN == False:
                COUNT[num1] += 1
                ENMO[num1][0] += 2
            DSC[num1] = 270
        elif 570 <= COUNT[num1] < 640:
            if KEN == False:
                COUNT[num1] += 1
            DSC[num1] = 0
        else:
            if KEN == False:
                COUNT[num1] = 0

    num2 = 1
    n2 = [0]
    bl_n2 = [50]
    enemy2 = Enemy((1030, 450), num2, n2)
    if MOVE[1] < 540:
        fig2 = True
    else:
        fig2 = False
    enemy2.figure(fig2)
    if MOVE[1] < 540:
        r_c2 = r_c
        enemy2.eyev(r, r_c2, num2, bl_n2)
        enemy2.react(num2)
    if REACO[num2] == 0 and FOUND[num2] == 0:
        if COUNT[num2] < 60:
            if KEN == False:
                COUNT[num2] += 1
                DSC[num2] += 1
        elif 60 <= COUNT[num2] < 120:
            if KEN == False:
                COUNT[num2] += 1
                DSC[num2] -= 1
        else:
            if KEN == False:
                COUNT[num2] = 0


    num3 = 2
    n3 = [0]
    bl_n3 = [18]
    enemy3 = Enemy((950, -300), num3, n3)
    enemy3.figure(True)
    r_c3 = r_c
    if REACO[num3] == 0 and FOUND[num3] == 0:
        if COUNT[num3] < 100:
            if KEN == False:
                COUNT[num3] += 1
                ENMO[num3][1] += 2
            DSC[num3] = 180
        elif 100 <= COUNT[num3] < 186:
            if KEN == False:
                COUNT[num3] += 1
                ENMO[num3][1] += 2
            DSC[num3] = 200
        elif 186 <= COUNT[num3] < 240:
            if KEN == False:
                COUNT[num3] += 1
                ENMO[num3][1] += 2
            DSC[num3] = 180
        elif 240 <= COUNT[num3] < 350:
            if KEN == False:
                COUNT[num3] += 1
            DSC[num3] = 180
        elif 350 <= COUNT[num3] < 580:
            if KEN == False:
                COUNT[num3] += 1
                ENMO[num3][1] -= 2
            DSC[num3] = 0
        elif 580 <= COUNT[num3] < 650:
            if KEN == False:
                COUNT[num3] += 1
            DSC[num3] = 180
        else:
            COUNT[num3] = 0
    enemy3.eyev(r, r_c3, num3, bl_n3)
    enemy3.react(num3)

    num4 = 3
    n4 = [3]
    bl_n4 = [3]
    enemy4 = Enemy((850, -400), num4, n4)
    enemy4.figure(True)
    if REACO[num4] == 0 and FOUND[num4] == 0:
        if COUNT[num4] < 100:
            if KEN == False:
                COUNT[num4] += 1
                ENMO[num4][1] += 2
            DSC[num4] = 180
        elif 100 <= COUNT[num4] < 186:
            if KEN == False:
                COUNT[num4] += 1
                ENMO[num4][1] += 2
            DSC[num4] = 154
        elif 186 <= COUNT[num4] < 240:
            if KEN == False:
                COUNT[num4] += 1
                ENMO[num4][1] += 2
            DSC[num4] = 180
        elif 240 <= COUNT[num4] < 350:
            if KEN == False:
                COUNT[num4] += 1
        elif 350 <= COUNT[num4] < 580:
            if KEN == False:
                COUNT[num4] += 1
                ENMO[num4][1] -= 2
            DSC[num4] = 0
        elif 580 <= COUNT[num4] < 650:
            if KEN == False:
                COUNT[num4] += 1
                DSC[num4] = -90
        else:
            if KEN == False:
                COUNT[num4] = 0
    for k in n4:
        ind = n4.index(k)
    e4 = r
    r_c4 = r_c
    enemy4.eyev(e4, r_c4, num4, bl_n4)
    enemy4.react(num4)

    num5 = 4
    n5 = [0]
    bl_n5 = [50]
    enemy5 = Enemy((450, -455), num5, n5)
    if 210 <= MOVE[1]:
        fig5 = True
    else:
        fig5 = False
    enemy5.figure(fig5)
    if REACO[num5] == 0 and FOUND[num5] == 0:
        if COUNT[num5] < 118:
            if KEN == False:
                COUNT[num5] += 1
                DSC[num5] += 1
        elif 118 <= COUNT[num5] < 236:
            if KEN == False:
                COUNT[num5] += 1
                DSC[num5] -= 1
        else:
            if KEN == False:
                COUNT[num5] = 0
    if 210 <= MOVE[1]:
        r_c5 = r_c
        enemy5.eyev(r, r_c5, num5, bl_n5)
        enemy5.react(num5)

    """増援"""
    num6 = 5
    n6 = [22, 3]
    bl_n6 = [3, 22]
    if u == 2:
        enemy6 = Enemy((900, -300), num6, n6)
    else:
        enemy6 = Enemy((100, -400), num6, n6)
    blocn6 = [0, 1, 2, 3]
    block_escape(num6, blocn6)
    if FINISH == True or u == 2:
        porpose(900, -300)
        if -27 < MOVE[1]:
            fig6 = True
            figeye6 = True
        else:
            fig6 = False
            figeye6 = False
    else:
        porpose(100, -400)
        if POR[0][0]-3 <= OBC[num6][0] <= POR[0][0]+3 and \
           POR[0][1]-3 <= OBC[num6][1] <= POR[0][1]+3:
            fig6 = False
            figeye6 = False
        else:
            if -27 < MOVE[1]:
                fig6 = True
                figeye6 = True
            else:
                fig6 = False
                figeye6 = False
    enemy6.figure(fig6)
    """敵兵６の壁判定"""
    d6 = 200
    if REACO[num6] == 0 and FOUND[num6] == 0:
        if POR[0][0]-3 <= OBC[num6][0] <= POR[0][0]+3:
            ENMOFA[num6][0] = 0
        elif OBC[num6][0] < POR[0][0]:
            if d6 < DIS[0][0]:
                if KEN == False:
                    ENMOFA[num6][0] = 4
                else:
                    ENMOFA[num6][0] = 0
        elif OBC[num6][0] > POR[0][0]:
            if d6 < DIS[0][2]:
                if KEN == False:
                    ENMOFA[num6][0] = -4
                else:
                    ENMOFA[num6][0] = 0
    else:
        ENMOFA[num6][0] = 0

    if REACO[num6] == 0 and FOUND[num6] == 0:
        if POR[0][1]-3 <= OBC[num6][1] <= POR[0][1]+3:
            ENMOFA[num6][1] = 0
        elif OBC[num6][1] < POR[0][1]:
            if d6 < DIS[0][1]:
                if KEN == False:
                    ENMOFA[num6][1] = 4
                else:
                    ENMOFA[num6][1] = 0
        elif OBC[num6][1] > POR[0][1]:
            if d6 < DIS[0][3]:
                if KEN == False:
                    ENMOFA[num6][1] = -4
                else:
                    ENMOFA[num6][1] = 0
    else:
        ENMOFA[num6][1] = 0

    """敵兵６の動きの制御"""
    if (FINISH == True or u == 2) and POR[0][0]-3 <= OBC[num6][0] <= POR[0][0]+3 and REACO[num6] == 0 and\
       FOUND[num6] == 0:
        if COUNT[num6] < 110:
            if KEN == False:
                COUNT[num6] += 1
            DSC[num6] = 0
        elif 110 <= COUNT[num6] < 190:
            if KEN == False:
                COUNT[num6] += 1
                DSC[num6] += 1
        elif 190 <= COUNT[num6] < 290:
            if KEN == False:
                COUNT[num6] += 1
                DSC[num6] -= 1
        elif 290 <= COUNT[num6] < 360:
            if KEN == False:
                COUNT[num6] += 1
            DSC[num6] = 180
        elif COUNT[num6] == 360:
            COUNT[num6] = 0
    enemy6.move(num6)
    for k in n6:
        ind = n6.index(k)
    e6 = r
    if figeye6 == True:
        r_c6 = r_c
        enemy6.eyev(e6, r_c6, num6, bl_n6)
    enemy6.react(num6)

    num7 = 6
    n7 = [0]
    bl_n7 = [50]
    if u == 2:
        enemy7 = Enemy((300, -400), num7, n7)
    else:
        enemy7 = Enemy((30, -400), num7, n7)
    blocn7 = [0, 1]
    block_escape(num7, blocn7)
    if FINISH == True or u == 2:
        porpose(300, -400)
        if 200 <= MOVE[1]:
            fig7 = True
            figeye7 = True
        else:
            fig7 = False
            figeye7 = False
    else:
        porpose(30, -400)
        if POR[1][0]-3 <= OBC[num7][0] <= POR[1][0]+3 and \
           POR[1][1]-3 <= OBC[num7][1] <= POR[1][1]+3:
            fig7 = False
            figeye7 = False
        else:
            if 200 <= MOVE[1]:
                fig7 = True
                figeye7 = True
            else:
                fig7 = False
                figeye7 = False
    enemy7.figure(fig7)
    d7 = 200
    if REACO[num7] == 0 and FOUND[num7] == 0:
        if POR[1][0]-3 <= OBC[num7][0] <= POR[1][0]+3:
            ENMOFA[num7][0] = 0
        elif OBC[num7][0] < POR[1][0]:
            if d7 < DIS[1][0]:
                if KEN == False:
                    ENMOFA[num7][0] = 4
                else:
                    ENMOFA[num7][0] = 0
        elif OBC[num7][0] > POR[1][0]:
            if d7 < DIS[1][2]:
                if KEN == False:
                    ENMOFA[num7][0] = -4
                else:
                    ENMOFA[num7][0] = 0
    else:
        ENMOFA[num7][0] = 0

    if REACO[num7] == 0 and FOUND[num7] == 0:
        if POR[1][1]-3 <= OBC[num7][1] <= POR[1][1]+3:
            ENMOFA[num7][1] = 0
        elif OBC[num7][1] < POR[1][1]:
            if d7 < DIS[1][1]:
                if KEN == False:
                    ENMOFA[num7][1] = 4
                else:
                    ENMOFA[num7][1] = 0
        elif OBC[num7][1] > POR[1][1]:
            if d7 < DIS[1][3]:
                if KEN == False:
                    ENMOFA[num7][1] = -4
                else:
                    ENMOFA[num7][1] = 0
    else:
        ENMOFA[num7][1] = 0

    if (FINISH == True or u == 2) and POR[1][0]-3 <= OBC[num7][0] <= POR[1][0]+3 and REACO[num7] == 0 and\
       FOUND[num7] == 0:
        if COUNT[num7] == 0:
            if KEN == False:
                COUNT[num7] += 1
            DSC[num7] = 0
        elif 0 < COUNT[num7] < 110:
            if KEN == False:
                COUNT[num7] += 1
                DSC[num7] -= 1
        elif 110 <= COUNT[num7] < 190:
            if KEN == False:
                COUNT[num7] += 1
                DSC[num7] += 1
        elif COUNT[num7] == 190:
            if KEN == False:
                COUNT[num7] = 0

    enemy7.move(num7)

    if figeye7 == True:
        r_c7 = r_c
        enemy7.eyev(r, r_c7, num7, bl_n7)
    enemy7.react(num7)

    num8 = 7
    n8 = [0]
    bl_n8 = [6]
    if u == 2:
        enemy8 = Enemy((170, 320), num8, n8)
    else:
        enemy8 = Enemy((10, 400), num8, n8)
    blocn8 = [5, 6]
    block_escape(num8, blocn8)
    if FINISH == True or u == 2:
        porpose(170, 320)
        if MOVE[1] < 540:
            fig8 = True
            figeye8 = True
        else:
            fig8 = False
            figeye8 = False
    else:
        porpose(10, 400)
        if POR[2][0]-3 <= OBC[num8][0] <= POR[2][0]+3 and \
           POR[2][1]-3 <= OBC[num8][1] <= POR[2][1]+3:
            fig8 = False
            figeye8 = False
        else:
            if MOVE[1] < 540:
                fig8 = True
                figeye8 = True
            else:
                fig8 = False
                figeye8 = False
    enemy8.figure(fig8)
    d8 = 50
    if REACO[num8] == 0 and FOUND[num8] == 0:
        if POR[2][0]-3 <= OBC[num8][0] <= POR[2][0]+3:
            ENMOFA[num8][0] = 0
        elif OBC[num8][0] < POR[2][0]:
            if d8 < DIS[2][0]:
                if KEN == False:
                    ENMOFA[num8][0] = 2
                else:
                    ENMOFA[num8][0] = 0
        elif OBC[num8][0] > POR[2][0]:
            if d8 < DIS[2][2]:
                if KEN == False:
                    ENMOFA[num8][0] = -2
                else:
                    ENMOFA[num8][0] = 0
    else:
        ENMOFA[num8][0] = 0

    if REACO[num8] == 0 and FOUND[num8] == 0:
        if POR[2][1]-3 <= OBC[num8][1] <= POR[2][1]+3:
            ENMOFA[num8][1] = 0
        elif OBC[num8][1] < POR[2][1]:
            if d8 < DIS[2][1]:
                if KEN == False:
                    ENMOFA[num8][1] = 2
                else:
                    ENMOFA[num8][1] = 0
        elif OBC[num8][1] > POR[2][1]:
            if d8 < DIS[2][3]:
                if KEN == False:
                    ENMOFA[num8][1] = -2
                else:
                    ENMOFA[num8][1] = 0
    else:
        ENMOFA[num8][1] = 0

    if (FINISH == True or u == 2) and POR[2][0]-3 <= OBC[num8][0] <= POR[2][0]+3 and REACO[num8] == 0 and\
       FOUND[num8] == 0:
        if COUNT[num8] < 110:
            if KEN == False:
                COUNT[num8] += 1
                DSC[num8] -= 1
        elif 110 <= COUNT[num8] < 190:
            if KEN == False:
                COUNT[num8] += 1
                DSC[num8] += 1
        elif COUNT[num8] == 190:
            if KEN == False:
                COUNT[num8] = 0

    enemy8.move(num8)

    if figeye8 == True:
        r_c8 = r_c
        enemy8.eyev(r, r_c8, num8, bl_n8)
    enemy8.react(num8)

    num9 = 8
    n9 = [0]
    bl_n9 = [50]
    if u == 2:
        enemy9 = Enemy((870, 320), num9, n9)
    else:
        enemy9 = Enemy((1200, 400), num9, n9)
    if FINISH == True or u == 2:
        porpose(870, 320)
        if MOVE[1] < 540:
            fig9 = True
            figeye9 = True
        else:
            fig9 = False
            figeye9 = False
    else:
        porpose(1200, 400)
        if POR[3][0]-3 <= OBC[num9][0] <= POR[3][0]+3 and \
           POR[3][1]-3 <= OBC[num9][1] <= POR[3][1]+3:
            fig9 = False
            figeye9 = False
        else:
            if MOVE[1] < 540:
                fig9 = True
                figeye9 = True
            else:
                fig9 = False
                figeye9 = False
    enemy9.figure(fig9)
    if REACO[num9] == 0 and FOUND[num9] == 0:
        if POR[3][0]-3 <= OBC[num9][0] <= POR[3][0]+3:
            ENMOFA[num9][0] = 0
        elif OBC[num9][0] < POR[3][0]:
            if KEN == False:
                ENMOFA[num9][0] = 4
            else:
                ENMOFA[num9][0] = 0
        elif OBC[num9][0] > POR[3][0]:
            if KEN == False:
                ENMOFA[num9][0] = -4
            else:
                ENMOFA[num9][0] = 0
    else:
        ENMOFA[num9][0] = 0

    if REACO[num9] == 0 and FOUND[num9] == 0:
        if POR[3][1]-3 <= OBC[num9][1] <= POR[3][1]+3:
            ENMOFA[num9][1] = 0
        elif OBC[num9][1] < POR[3][1]:
            if KEN == False:
                ENMOFA[num9][1] = 4
            else:
                ENMOFA[num9][1] = 0
        elif OBC[num9][1] > POR[3][1]:
            if KEN == False:
                ENMOFA[num9][1] = -4
            else:
                ENMOFA[num9][1] = 0
    else:
        ENMOFA[num9][1] = 0

    if (FINISH == True or u == 2) and POR[3][0]-3 <= OBC[num9][0] <= POR[3][0]+3 and REACO[num9] == 0 and\
       FOUND[num9] == 0:
        if COUNT[num9] < 80:
            if KEN == False:
                COUNT[num9] += 1
                DSC[num9] += 1
        elif 80 <= COUNT[num9] < 235:
            if KEN == False:
                COUNT[num9] += 1
                DSC[num9] -= 1
        elif 235 <= COUNT[num9] < 240:
            if KEN == False:
                COUNT[num9] += 1
            DSC[num9] = 0
        elif 240 <= COUNT[num9] < 320:
            if KEN == False:
                COUNT[num9] += 1
                DSC[num9] -= 1
        elif 320 <= COUNT[num9] < 460:
            if KEN == False:
                COUNT[num9] += 1
                DSC[num9] += 1
        elif COUNT[num9] == 460:
            DSC[num9] = 90
            if KEN == False:
                COUNT[num9] = 0

    enemy9.move(num9)

    if figeye9 == True:
        r_c9 = r_c
        enemy9.eyev(r, r_c9, num9, bl_n9)
    enemy9.react(num9)

    OBC = []
    vecboe = []
    for k in range(9):
        vecboe.append([])
    POR = []
    DIS = []

def tick():
    global MOVE, HERO, yup, ydown, xleft, xright, space, eyevi,\
           ku, kd, kr, kl, KMOVE, i, u, enter, SCOPE, SHOOT, SHOCA, EQUIP, KEN, \
           KSPA, qslo, SOUND
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[K_e]:
                yup = True
            if pygame.key.get_pressed()[K_v]:
                ydown = True
            if pygame.key.get_pressed()[K_w]:
                xleft = True
            if pygame.key.get_pressed()[K_r]:
                xright = True
            if pygame.key.get_pressed()[K_UP]:
                ku = True
            if pygame.key.get_pressed()[K_j]:
                qslo = True
            if pygame.key.get_pressed()[K_DOWN]:
                kd = True
            if pygame.key.get_pressed()[K_LEFT]:
                kl = True
            if pygame.key.get_pressed()[K_RIGHT]:
                kr = True
            if pygame.key.get_pressed()[K_i]:
                if space == 1 and STOP == True:
                    eyevi = False
                    space = 0
                elif space == 0 and STOP == True:
                    eyevi = True
                    space = 1
            if pygame.key.get_pressed()[K_u]:
                    if u == 0 and STOP == True:
                        u = 1
                    elif u == 1 and STOP == True:
                        u = 2
                    elif u == 2 and STOP == True:
                        u = 0
            if pygame.key.get_pressed()[K_p]:
                if enter == False:
                    enter = True
                else:
                    enter = False
            if pygame.key.get_pressed()[K_k]:
                    SCOPE = True
            if pygame.key.get_pressed()[K_l]:
                    SHOOT = True
            if pygame.key.get_pressed()[K_SPACE]:
                if LIME != 0:
                    KSPA = True
            if pygame.key.get_pressed()[K_n]:
                KEN = True
            if pygame.key.get_pressed()[K_1]:
                EQUIP = 1
            if pygame.key.get_pressed()[K_2]:
                EQUIP = 2

        if event.type == KEYUP:
            if event.key == K_e:
                yup = False
            if event.key == K_v:
                ydown = False
            if event.key == K_w:
                xleft = False
            if event.key == K_r:
                xright = False
            if event.key == K_j:
                qslo = False
            if event.key == K_UP:
                ku = False
            if event.key == K_DOWN:
                kd = False
            if event.key == K_LEFT:
                kl = False
            if event.key == K_RIGHT:
                kr = False
            if event.key == K_k:
                SCOPE = False
            if event.key == K_l:
                SHOOT = False
            if event.key == K_SPACE:
                KSPA = False
            if event.key == K_n:
                KEN = False

    if GAMEOVER == False and KEN == False and CLEAR == False:
        if yup == True:
            if xright == True or xleft == True:
                i = 45
            else:
                i = 90
        if ydown == True:
            if xright == True or xleft == True:
                i = 45
            else:
                i = 90
        if xright == True:
            if yup == True or ydown == True:
                i = 45
            else:
                i = 90
        if xleft == True:
            if yup == True or ydown == True:
                i = 45
            else:
                i = 90

        if yup == True and SCOPE == True:
            if -250 <= SHOCA[1]:
                SHOCA[1] -= 10*sin(i)
        elif yup == True and qslo == True:
            if BLO[3] == 0:
                MOVE[1] += 3*sin(i)
        elif yup == True:
            if BLO[3] == 0:
                MOVE[1] += 5*sin(i)

        if ydown == True and SCOPE == True:
            if SHOCA[1] <= 250:
                SHOCA[1] += 10*sin(i)
        elif ydown == True and qslo == True:
            if BLO[1] == 0:
                MOVE[1] -= 3*sin(i)
        elif ydown == True:
            if BLO[1] == 0:
                MOVE[1] -= 5*sin(i)

        if xright == True and SCOPE == True:
            if SHOCA[0] <= 250:
                SHOCA[0] += 10*sin(i)
        elif xright == True and qslo == True:
            if BLO[0] == 0:
                MOVE[0] -= 3*sin(i)
        elif xright == True:
            if BLO[0] == 0:
                MOVE[0] -= 5*sin(i)

        if xleft == True and SCOPE == True:
            if -250 <= SHOCA[0]:
                SHOCA[0] -= 10*sin(i)
        elif xleft == True and qslo == True:
            if BLO[2] == 0:
                MOVE[0] += 3*sin(i)
        elif xleft == True:
            if BLO[2] == 0:
                MOVE[0] += 5*sin(i)

        if SCOPE == False:
            SHOCA = [0, 0]

        if ku == True:
            KMOVE[1] = 100
        elif kd == True:
            KMOVE[1] = -100
        elif ku == False and kd == False:
            KMOVE[1] = 0

        if kr == True:
            KMOVE[0] = -100
        elif kl == True:
            KMOVE[0] = 100
        elif kr == False and kl == False:
            KMOVE[0] = 0

def paint():
    global HEROP, POLYGON
    wall = Back_ground()
    hero = Hero(500, 330)
    hero.hero_rad()
    hero.figure()
    wall.block()
    ene_move()
    hero.shoot()
    hero.medicine()
    hero.life()
    goll()
    difficalty()
    alert()
    rank()

    """sysfont = pygame.font.SysFont(None, 60)
    mo = sysfont.render("{}".format(SOEF[1]), True, (225, 0, 0))
    mo_rect = mo.get_rect()
    mo_rect.center = (500, 400)
    SURFACE.blit(mo, mo_rect)"""
    HEROP.clear()
    POLYGON.clear()

def main():
    global COUNT, COUNT2, DSC, POLYGON, MOVE, HERO, HEROP, HEROD, HRAD, eye_c, \
        COUNTW, KMOVE,\
        BLO, CLEAR, ENMO, ENMOFA, blocg, vecboe, OBC, i, TIMER, TIMER2, TIMER3,\
        ALERT, AT, STOP, BLOC, FINISH, ALCOUNT, ALTIMER, COAL, POR,\
        SCOPE, SHOOT, STONE, STONUM, HERO_POR, STCO, STMO, STPO, STMOMAI, MOVEAD,\
        COUREA, SOUND, SOEF, REACO, DSCFA, SHOCA, FOUND, DSCFA2, ENAMO, DSCAM,\
        COUNTAM, MOVEHE, GAMEOVER, MOHIT, LIFECO, LIME, KSPA, KEN, EQUIP, DACOU, DAMAGE,\
        VACAD2, degs2, EYE_SETl, EYE_SETr, MUSIC, MUSTART
    VECVI1_l = [[(0, -10), (0, -30), (0, -50), (0, -70), (0, -90), (0, -110), (0, -130), (0, -150), (0, -170),
              (0, -190), (0, -210)],
             [(-20, -30), (-20, -50), (-20, -70), (-20, -90), (-20, -110), (-20, -130), (-20, 150), (-20, -170),
              (-20, -190), (-20, -210)],
             [(-40, -65), (-40, -85),(-40, -105), (-40, -125), (-40, -145), (-40, -165), (-40, -185),
              (-40, -205)],
             [(-60, -95), (-60, -115), (-60, -135), (-60, -155), (-60, -175), (-60, -195)],
             [(-80, -125), (-80, -135), (-80, -155), (-80, -175), (-80, -195)],
             [(-100, -165), (-100, -185)]]

    VECVI1_r = [[(0, -10), (0, -30), (0, -50), (0, -70), (0, -90), (0, -110), (0, -130), (0, -150), (0, -170),
                (0, -190), (0, -210)],
                [(20, -30), (20, -50), (20, -70), (20, -90), (20, -110), (20, -130), (20, 150), (20, -170), \
                (20, -190), (20, -210)],
                [(40, -65), (40, -85),(40, -105), (40, -125), (40, -145), (40, -165), (40, -185), (40, -205)],
                [(60, -95), (60, -115), (60, -135), (60, -155), (60, -175), (60, -195)],
                [(80, -125), (80, -135), (80, -155), (80, -175), (80, -195)],
                [(100, -165), (100, -185)]]

    VECVI0_l = [[(0, -10), (0, -30), (0, -50), (0, -70), (0, -90), (0, -110), (0, -130)],
             [(-20, -40), (-20, -50), (-20, -70), (-20, -90), (-20, -110), (-20, -130)],
             [(-40, -65), (-40, -85),(-40, -105), (-40, -125)],
             [(-60, -100), (-60, -120)]]

    VECVI0_r = [[(0, -10), (0, -30), (0, -50), (0, -70), (0, -90), (0, -110), (0, -130)],
               [(20, -40), (20, -50), (20, -70), (20, -90), (20, -110), (20, -130)],
               [(40, -65), (40, -85),(40, -105), (40, -125)],
               [(60, -100), (60, -120)]]

    EYE_SET0_l = []
    for k in VECVI0_l:
        EYE_SET = []
        for i in k:
            vecsc = (100, 0)
            lensc = 100
            lenvi0 = hypot(i[0], i[1])
            lenvi0s = lenvi0 * lensc
            if lenvi0s == 0:
                lenvi0s = 0.01
            degvi0s = degrees(acos(dot(i, vecsc)/lenvi0s))
            EYE_SET.append([lenvi0, degvi0s])
        EYE_SET0_l.append(EYE_SET)

    EYE_SET0_r = []
    for k in VECVI0_r:
        EYE_SET = []
        for i in k:
            vecsc = (100, 0)
            lensc = 100
            lenvi0 = hypot(i[0], i[1])
            lenvi0s = lenvi0 * lensc
            if lenvi0s == 0:
                lenvi0s = 0.01
            degvi0s = degrees(acos(dot(i, vecsc)/lenvi0s))
            EYE_SET.append([lenvi0, degvi0s])
        EYE_SET0_r.append(EYE_SET)

    EYE_SET1_l = []
    for k in VECVI1_l:
        EYE_SET = []
        for i in k:
            vecsc = (100, 0)
            lensc = 100
            lenvi0 = hypot(i[0], i[1])
            lenvi0s = lenvi0 * lensc
            if lenvi0s == 0:
                lenvi0s = 0.01
            degvi0s = degrees(acos(dot(i, vecsc)/lenvi0s))
            EYE_SET.append([lenvi0, degvi0s])
        EYE_SET1_l.append(EYE_SET)

    EYE_SET1_r = []
    for k in VECVI1_r:
        EYE_SET = []
        for i in k:
            vecsc = (100, 0)
            lensc = 100
            lenvi0 = hypot(i[0], i[1])
            lenvi0s = lenvi0 * lensc
            if lenvi0s == 0:
                lenvi0s = 0.01
            degvi0s = degrees(acos(dot(i, vecsc)/lenvi0s))
            EYE_SET.append([lenvi0, degvi0s])
        EYE_SET1_r.append(EYE_SET)
    while True:
        SURFACE.fill((250, 250, 250))
        if enter == False:
            POLYGON = []
            MOVE = [0, 0]
            HERO = []
            HEROP = []
            DSC = [90, 0, 180, 180, 180, 270, 270, 270, 90]
            HEROD = 0
            HRAD = [0, 0]
            eye_c = ()
            COUNTW = 0
            KMOVE = [0, 0]
            lenx = 0
            BLO = [0, 0, 0, 0]
            KSPA = False
            KEN = False
            CLEAR = False
            ENMO = []
            ENMOFA = []
            SOUND = []
            SOEF = []
            AT = []
            REACO = []
            DSCFA = []
            DSCFA2 = []
            COUNT = []
            COUNT2 = []
            FOUND = []
            vecboe = []
            ENAMO = []
            DSCAM = []
            COUNTAM = []
            MOVEHE = []
            VACAD2 = []
            degs2 = []
            for k in range(9):
                ENMO.append([0, 0])
                ENMOFA.append([0, 0])
                SOUND.append([0, 0, 0])
                SOEF.append([0, 0, 0])
                AT.append(0)
                REACO.append(0)
                DSCFA.append(0)
                DSCFA2.append(500)
                COUNT.append(0)
                COUNT2.append(0)
                FOUND.append(0)
                vecboe.append([])
                ENAMO.append([])
                DSCAM.append([])
                MOVEHE.append([])
                for i in range(3):
                    ENAMO[k].append([0, 0])
                    MOVEHE[k].append([0, 0])
                    DSCAM[k].append(0)
                COUNTAM.append([0, 0, 0, 0])
                VACAD2.append([0, 0])
                degs2.append(0)

            blocg = []
            OBC = []
            i = 0
            TIMER = 0
            TIMER2 = 0
            TIMER3 = 0
            ALERT = 0
            STOP = True
            FINISH = False
            ALCOUNT = 0
            ALTIMER = 60
            COAL = 0
            POR = []
            SCOPE = False
            SHOOT = False
            STONE = []
            STONUM = 2
            HERO_POR = []
            STCO = 0
            STMO = []
            STPO = []
            STMOMAI = []
            MOVEAD = []
            COUREA = []
            SHOCA = [0, 0]
            GAMEOVER = False
            MOHIT = 0
            EQUIP = 1
            DACOU = 0
            DAMAGE = False
            MUSIC = True
            MUSTART
            pygame.mixer.music.stop()
            tick()
            sysfont = pygame.font.SysFont(None, 100)
            mm = sysfont.render("{}".format("PAKURI GEAR SOLID"), True, (0, 0, 250))
            mm_rect = mm.get_rect()
            mm_rect.center = (500, 330)
            SURFACE.blit(mm, mm_rect)
            difficalty()
            if u == 1 or u == 2:
                EYE_SETl = EYE_SET1_l
                EYE_SETr = EYE_SET1_r
                LIFECO = 3
                LIME = 1
            elif u == 0:
                EYE_SETl = EYE_SET0_l
                EYE_SETr = EYE_SET0_r
                LIFECO = 5
                LIME = 2
            sysfont = pygame.font.SysFont(None, 40)
            if eyevi == True:
                mv = sysfont.render("{}".format("on"), True, (250, 125, 0))
            else:
                mv = sysfont.render("{}".format("off"), True, (250, 125, 0))
            mv_rect = mv.get_rect()
            mv_rect.center = (950, 33)
            SURFACE.blit(mv, mv_rect)
        elif enter == True:
            STOP = False
            tick()
            paint()

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
