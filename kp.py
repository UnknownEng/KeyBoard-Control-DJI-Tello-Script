import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((500,500))
    
def getKey(KeyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(KeyName))
    
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    
    return ans

def main():
    if getKey("a"):
        print("move Left")

        
if __name__ ==  "__main__":
    init()
    while True:
        main()

