import pygame
from population import Population


L, H = 600, 600
TAILLE_CASE = 75
NOIR=(0,0,0)
VERT_BOUTEILLE = (0, 128, 0)
VERT_BOUTEILLE_CLAIR = (255, 250, 240)
BEIGE = (245, 245, 220)
BEIGE_CLAIR = (0, 170, 0)

def drawKnight(ecran, padding):
    
    ecran.fill(BEIGE)
    pygame.draw.rect(
        ecran,
        (255, 255, 255),
        (0, 0, L+ 2 * padding, H + 2 * padding),
    )

    font = pygame.font.Font(None, 36)
    for i in range(8):
        text = font.render(str(i + 1), True, NOIR)
        text_rect = text.get_rect(
            center=(padding // 2, padding + i * TAILLE_CASE + TAILLE_CASE // 2)
        )
        ecran.blit(text, text_rect)

    for i in range(8):
        text = font.render(str(i + 1), True, NOIR)
        text_rect = text.get_rect(
            center=(
                L + padding + padding // 2,
                padding + i * TAILLE_CASE + TAILLE_CASE // 2,
            )
        )
        ecran.blit(text, text_rect)

    for i in range(8):
        text = font.render(str(i + 1), True, NOIR)
        text_rect = text.get_rect(
            center=(
                padding + i * TAILLE_CASE + TAILLE_CASE // 2,
                H + padding + padding // 2,
            )
        )
        ecran.blit(text, text_rect)

    for y in range(8):
        for x in range(8):
            couleur = (
                VERT_BOUTEILLE_CLAIR if (x + y) % 2 == 0 else VERT_BOUTEILLE
            )  
            pygame.draw.rect(
                ecran,
                couleur,
                (
                    x * TAILLE_CASE + padding,
                    y * TAILLE_CASE + padding,
                    TAILLE_CASE,
                    TAILLE_CASE,
                ),
            )
            pygame.draw.line(
                ecran,
                VERT_BOUTEILLE,
                (x * TAILLE_CASE + padding, y * TAILLE_CASE + padding),
                (x * TAILLE_CASE + padding, (y + 1) * TAILLE_CASE + padding),
            )
            pygame.draw.line(
                ecran,
                VERT_BOUTEILLE,
                (x * TAILLE_CASE + padding, y * TAILLE_CASE + padding),
                ((x + 1) * TAILLE_CASE + padding, y * TAILLE_CASE + padding),
            )
    font = pygame.font.Font(None, 36)
    text = font.render("The Knight’s Tour", True, NOIR)
    text_rect = text.get_rect(center=(L// 2 + padding, padding // 2))
    text_rect.move_ip(0, +10)  
    ecran.blit(text, text_rect)
    pygame.display.flip() 



def knightPath(ecran, chemin):
    chevalier_image = pygame.image.load("knight.png")  
    chevalier_image = pygame.transform.scale(
        chevalier_image, (70, 70)
    )  

    font = pygame.font.Font(None, 40)  
    for i, (pos, num) in enumerate(chemin):
        pos_x = pos[0] * TAILLE_CASE + TAILLE_CASE // 2 - 20
        pos_y = pos[1] * TAILLE_CASE + TAILLE_CASE // 2 - 20

        couleur_case = BEIGE_CLAIR if (pos[0] + pos[1]) % 2 == 0 else BEIGE

        ecran.blit(chevalier_image, (pos_x + 37, pos_y + 37))
        pygame.display.flip()
        wait = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    wait = False
        pygame.draw.rect(ecran, couleur_case, (pos_x + 33, pos_y + 33, 76, 76))
        text = font.render(
            str(num), True, NOIR
        )  
        text_rect = text.get_rect(center=(pos_x + 70, pos_y + 70))
        ecran.blit(text, text_rect)
    pygame.display.flip()  


def main():
    pygame.init()
    padding = 50 
    ecran = pygame.display.set_mode(
        (L + 2 * padding, H + 2 * padding)
    )  
    pygame.display.set_caption("Tour du Chevalier")

    taille_population = 50
    population = Population(taille_population)

    horloge = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        population.check_population()
        maxFit, bestFitness = population.evaluate()
        population.create_new_generation()
        print(f"Generation: {population.generation}, Best Fitness: {maxFit}")

        ecran.fill(BEIGE) 
        drawKnight(ecran, padding)

        if bestFitness and bestFitness.fitness == 64:
            print("Solution optimale trouvée!")
            knightPath(ecran, bestFitness.path)
            running = False  
            break

        population.create_new_generation()
        if bestFitness:
            knightPath(ecran, bestFitness.path)
        pygame.display.flip()
        horloge.tick(10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                exit()


if __name__ == "__main__":
    main()
