import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set the window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the circle radius and line radius
circle_radius = 5
line_radius = 100

# Generate a list of random coordinates
num_points = 50
points = [(random.randint(0, screen_width), random.randint(0, screen_height)) for i in range(num_points)]


# Define a function to draw the circles and lines
def draw_points(points):
    # Draw the circles
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), point, circle_radius)

    # Draw the lines
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            if distance <= line_radius:
                pygame.draw.line(screen, (255, 255, 255), points[i], points[j], 1)


# Draw the initial points
draw_points(points)

# Update the display
pygame.display.update()

# Keep the window open until the user closes it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()