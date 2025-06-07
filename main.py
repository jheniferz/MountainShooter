import pygame

print('Setup Star')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Setup loop')
while True:
    # check fo all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window
            quit()  # end pygame
