import pygame
import random

# initialising pygame
pygame.init()

# making the screen
screen = pygame.display.set_mode((800, 600))

# for setting font
base_font = pygame.font.Font(None, 32)

# setting title and logo
pygame.display.set_caption("BALL GAME")
icon = pygame.image.load('football.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('Untitled-1.png')

# starting position of ball (basically centre)
iconX = 400
iconY = 300


# making the football
def football(x, y):
    screen.blit(icon, (x, y))


# defining user answer
userans = ''

# making the question
n1 = random.randint(0, 100)
n2 = random.randint(0, 100)

ans1 = n1 + n2
ans1 = str(ans1)
nn1 = str(n1)
nn2 = str(n2)
nn3 = nn1 + " + " + nn2
question = ("What is " + nn3 + " ? (Press Space After Writing ans)")

# making variable for the amount by which the ball moves left when user gives the right answer
p = 0

running = True
# for user inputs
while running:
    for event in pygame.event.get():

        # for making the game quit after user presses cross button

        if event.type == pygame.QUIT:
            running = False

        # making the typing mechanism
        if event.type == pygame.KEYDOWN:
            # making backspace mechanism
            if event.key == pygame.K_BACKSPACE:
                userans = userans[:-1]
            # for making the letter mechanism
            else:
                userans += event.unicode

            # for entering the answer
            if event.key == pygame.K_SPACE:
                # if user enters wrong answer
                if userans.strip() not in (ans1) or userans.strip == "":
                    userans = "WRONG"
                else:
                    # for printing new question after user enters right answer
                    userans = ""

                    n1 = random.randint(0, 100)
                    n2 = random.randint(0, 100)

                    ans1 = n1 + n2
                    ans1 = str(ans1)
                    nn1 = str(n1)
                    nn2 = str(n2)
                    nn3 = nn1 + " + " + nn2
                    question = ("What is " + nn3 + " ? (Press Space After Writing ans)")

                    p += 0.008

                    '''for increasing the value of 'p' (variable which dcides the amount by which ball 
                    moves left / the speed of going right decreases when user enters correct answer)'''

    # for making the ball move left/right.
    iconX += 0.042 - p

    # for making background green
    screen.fill((0, 255, 0))

    # making background appear
    screen.blit(background, (0, 0))

    # for making the football appear
    football(iconX, iconY)

    # for printing the question
    questionbox = base_font.render(question, True, (0, 0, 0))
    screen.blit(questionbox, (0, 0))

    # for printing answer bar
    if iconX < 799 and iconX > 0:
        useranswertext = base_font.render(userans, True, (0, 0, 0))
        screen.blit(useranswertext, (0, 20))
    elif iconX < 0:
        hello = base_font.render("YOU WON", True, (0, 0, 0))
        screen.blit(hello, (0, 20))
    else:
        bye = base_font.render("YOU LOST", True, (0, 0, 0))
        screen.blit(bye, (0, 20))

    print(ans1)

    # for constantly updating the screen
    pygame.display.update()
