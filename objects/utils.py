import pygame

def drawRect(screen, color, rect, width):
    return pygame.draw.rect(screen, color, rect, width)

def drawPolygon(screen, color, pointlist, width):
    return pygame.draw.polygon(screen, color, pointlist, width)

def drawCircle(screen, color, pos, radius, width):
    return pygame.draw.circle(screen, color, pos, radius, width)
