import pygame
import pygame_gui

pygame.init()
pygame.display.set_caption = "turbo ._."
window_surface = pygame.display.set_mode((800, 600))

img = pygame.image.load("face.png")
background = pygame.Surface((800, 600))
background.fill("#ffffff")
img = pygame.transform.scale(img, (356, 245))


manager = pygame_gui.UIManager((800, 600))

size_x = 100
size_y = 100
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 500), (100, 50)), text="Start", manager=manager)
imp = pygame.image.load("fish.jpg")
imp = pygame.transform.scale(imp, (size_x, size_y))

clock = pygame.time.Clock()
time_cumulative = 0
running = True

image_x = 0
image_y = 0

while running: 
    time_delta = clock.tick(60) / 1000.0
    time_cumulative += time_delta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quit")
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                if image_y < 600:
                    image_x += 10
                    image_y += 10
                else:
                    image_x = -100
                    image_y = -100
                print(time_delta)
                print(time_cumulative)
                print("._.")
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0,0))
    window_surface.blit(img, (0, 0))
    window_surface.blit(imp, (image_x, image_y))
    manager.draw_ui(window_surface)
    pygame.display.update()

pygame.quit()


