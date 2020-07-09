import pygame
from state import State
from minimax import minimax
from copy import deepcopy

HEIGHT, WIDTH = 600,600
TITLE = "Tic-Tac-Toe"

pygame.init()

screne = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

fps = 60
fpsClock = pygame.time.Clock()

background = pygame.Surface(screne.get_size())
background = background.convert()
background.fill((0,0,0))


rect = [[0 for _ in range(3)] for _ in range(3)]

def show(state):
    PAD = 5
    L = WIDTH//3
    W = HEIGHT//3
    COLOR = (200,200,200)
    for i in range(3):
        for j in range(3):
            x, y = j*L,i*L
            dim = (x,y,W - PAD,L- PAD)
            rect[i][j] = pygame.draw.rect(screne,COLOR,dim)
            if state.board[i][j] == "O":
                # draw O
                pygame.draw.circle(screne,(0,0,0),(x + L//2,y + W//2),L//2 - 20,3)
            elif state.board[i][j] == "X":
                # draw X
                pygame.draw.line(screne,(0,0,0),(x + 20,y + 20),(x + L - 20,y + W - 20),5)
                pygame.draw.line(screne,(0,0,0),(x + 20,y + W - 20),(x + L - 20,y + 20),5)


def mark_victory(state):
    L = WIDTH//3
    W = HEIGHT//3

    strike = state.get_strike()
    if not strike is None:
        i = strike[0]
        if strike[1] == "row":
            pygame.draw.line(screne,(0,255,0,10),(10,i*L + L//2),(WIDTH - 10,i*L + L//2),10)
        elif strike[1] == "col":
            pygame.draw.line(screne,(0,255,0,10),(i*W + W//2,10),(i*W + W//2,HEIGHT-10),10)
        elif i == 0:
            pygame.draw.line(screne,(0,255,0,10),(10,10),(WIDTH-10,HEIGHT-10),10)
        else:
            pygame.draw.line(screne,(0,255,0,10),(10,HEIGHT-10),(WIDTH-10,10),10)
  

def make_move(state,pos,turn):
    for i in range(3):
        for j in range(3):
            if rect[i][j].collidepoint(pos):
                if state.make_move((i,j),turn):
                    return "O" if turn == "X" else "X"
                else:
                    return turn


def start_game(keys):
    global turn
    global ai
    global playing
    global state
    if keys[pygame.K_a]:
        turn,ai= "X","X"
        state = State()
        playing = True
    if keys[pygame.K_b]:
        turn,ai= "X","O"
        state = State()
        playing = True
    if keys[pygame.K_c]:
        turn,ai= "X",None
        state = State()
        playing = True
    

state = State()
run,playing = True,False
turn,ai = None,None

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if playing:
                if turn != ai:
                    turn = make_move(state,pos,turn)
            else:
                turn = "X"
                playing = True
                state = State()

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if turn is None:
                start_game(keys)
            if not playing:
                turn,ai = None,None

    screne.blit(background,(0,0))

    if turn is None:
        textsurface = myfont.render('Press A AI goes first', False, (255, 255, 255))
        screne.blit(textsurface,(100,200))
        textsurface = myfont.render('Press B AI goes second', False, (255, 255, 255))
        screne.blit(textsurface,(100,260))
        textsurface = myfont.render('Press C Two player', False, (255, 255, 255))
        screne.blit(textsurface,(100,320))
    else:
        show(state)
        if not state.result() is None:
            mark_victory(state)
            playing = False
            font = pygame.font.SysFont('Comic Sans MS', 40)
            textsurface = font.render('Click On Screen to Play Again!', False, (255,0,0,20))
            screne.blit(textsurface,(20,100))
            textsurface = font.render('Press any key for Main Menue!', False, (255,0,0,20))
            screne.blit(textsurface,(20,200))

        if playing and turn == ai:
            font = pygame.font.SysFont('Comic Sans MS', 80)
            textsurface = font.render('AI Thiniking...', False, (255, 0, 0,10))
            screne.blit(textsurface,(50,200))

    pygame.display.flip()
    # fpsClock.tick(fps)
    if playing and turn == ai:
        print("----Its AI's Turn!----")
        print("....Thinking.....")
        ai_move = minimax(state, turn)[1]
        state.make_move(ai_move, turn)
        print("---AI made a move. Your turn!---")
        turn = "O" if turn == "X" else "X"


pygame.quit()


