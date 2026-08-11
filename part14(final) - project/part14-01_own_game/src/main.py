import pygame
import copy

TILE = 40
W, H = 800, 480
FPS = 60
DELAY = 150

FLOOR, WALL, COIN, DOOR_L, START, DOOR_O = 0, 1, 2, 3, 4, 5

lvl = [
    [1] * 20,
    [1, 4, 0, 0, 2, 0, 0, 2, 0, 1, 1, 0, 2, 0, 0, 0, 2, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 2, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 1, 1, 1, 1, 0, 2, 1, 1, 0, 0, 1, 1, 1, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 1],
    [1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 2, 1],
    [1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 2, 0, 1],
    [1, 2, 0, 1, 1, 1, 1, 0, 2, 1, 1, 0, 2, 1, 1, 1, 0, 1, 2, 3],
]

colors = {
    "floor": (30, 30, 40),
    "wall": (80, 30, 120),
    "txt": (255, 255, 255),
    "hud": (15, 15, 25),
}


class Mob:
    def __init__(self, x, y, d, spd):
        self.x, self.y, self.d, self.spd, self.t = x, y, d, spd, 0

    def update(self, g):
        self.t += 1
        if self.t >= self.spd:
            nx = self.x + self.d
            if nx < 0 or nx >= 20 or g[self.y][nx] == WALL:
                self.d *= -1
            else:
                self.x = nx
            self.t = 0


def main():
    pygame.init()
    scr = pygame.display.set_mode((W, H))
    clk = pygame.time.Clock()
    fnt = pygame.font.SysFont("Arial", 18)
    big_fnt = pygame.font.SysFont("Arial", 32, bold=True)

    try:
        img_plr = pygame.transform.scale(
            pygame.image.load("robot.png").convert_alpha(), (TILE, TILE)
        )
        img_mob = pygame.transform.scale(
            pygame.image.load("monster.png").convert_alpha(), (TILE, TILE)
        )
        img_coin = pygame.transform.scale(
            pygame.image.load("coin.png").convert_alpha(), (TILE, TILE)
        )
        img_door = pygame.transform.scale(
            pygame.image.load("door.png").convert_alpha(), (TILE, TILE)
        )
    except:
        img_plr = img_mob = img_coin = img_door = None

    g = copy.deepcopy(lvl)
    px, py = 1, 1
    coins = moves = last = 0
    tot = sum(r.count(COIN) for r in g)
    door_open = dead = win = False
    mobs = [Mob(5, 3, 1, 40), Mob(5, 7, -1, 40)]

    while True:
        now = pygame.time.get_ticks()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_F2:
                g = copy.deepcopy(lvl)
                px, py = 1, 1
                coins = moves = last = 0
                door_open = dead = win = False
                mobs = [Mob(5, 3, 1, 40), Mob(5, 7, -1, 40)]
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
                return

        if not dead and not win:
            k = pygame.key.get_pressed()
            dx = dy = 0
            if k[pygame.K_LEFT]:
                dx = -1
            elif k[pygame.K_RIGHT]:
                dx = 1
            elif k[pygame.K_UP]:
                dy = -1
            elif k[pygame.K_DOWN]:
                dy = 1

            if (dx or dy) and now - last > DELAY:
                nx, ny = px + dx, py + dy
                if 0 <= nx < 20 and 0 <= ny < 10 and g[ny][nx] != WALL:
                    px, py = nx, ny
                    last = now
                    moves += 1
                    if g[py][px] == COIN:
                        coins += 1
                        g[py][px] = FLOOR

            rem = sum(r.count(COIN) for r in g)
            if rem == 0 and not door_open:
                door_open = True
                for r in range(10):
                    for c in range(20):
                        if g[r][c] == DOOR_L:
                            g[r][c] = DOOR_O

            if door_open and g[py][px] == DOOR_O:
                win = True

            for m in mobs:
                m.update(g)
                if m.x == px and m.y == py:
                    dead = True

        scr.fill(colors["floor"])

        instr = fnt.render(
            "Collect all the coins. Avoid monsters. Reach the door (In as less moves as possible).",
            True,
            colors["txt"],
        )
        scr.blit(instr, (W // 2 - instr.get_width() // 2, 5))

        for y in range(10):
            for x in range(20):
                t = g[y][x]
                rect = (x * TILE, y * TILE + 25, TILE, TILE)
                if t == WALL:
                    pygame.draw.rect(scr, colors["wall"], rect)
                    pygame.draw.rect(scr, (120, 60, 180), rect, 2)
                elif t == COIN and img_coin:
                    scr.blit(img_coin, rect)
                elif t in (DOOR_L, DOOR_O) and img_door:
                    scr.blit(img_door, rect)
                else:
                    pygame.draw.rect(scr, colors["floor"], rect)

        if img_plr:
            scr.blit(img_plr, (px * TILE, py * TILE + 25))
        else:
            pygame.draw.rect(
                scr,
                (0, 200, 255),
                (px * TILE + 5, py * TILE + 30, TILE - 10, TILE - 10),
            )

        for m in mobs:
            if img_mob:
                scr.blit(img_mob, (m.x * TILE, m.y * TILE + 25))
            else:
                pygame.draw.rect(
                    scr,
                    (0, 0, 0),
                    (m.x * TILE + 4, m.y * TILE + 29, TILE - 8, TILE - 8),
                )
                pygame.draw.rect(
                    scr,
                    (255, 0, 200),
                    (m.x * TILE + 4, m.y * TILE + 29, TILE - 8, TILE - 8),
                    2,
                )

        hs = pygame.Surface((W, 50))
        hs.fill(colors["hud"])
        scr.blit(hs, (0, 430))
        txt = f"Coins: {coins}/{tot} | Moves: {moves} | F2=Restart ESC=Quit"
        scr.blit(fnt.render(txt, True, colors["txt"]), (10, 445))

        if dead or win:
            ov = pygame.Surface((W, H), pygame.SRCALPHA)
            ov.fill((0, 0, 0, 180))
            scr.blit(ov, (0, 0))
            msg = "GAME OVER" if dead else "CONGRATULATIONS!"
            clr = (255, 0, 200) if dead else (0, 255, 120)
            t1 = big_fnt.render(msg, True, clr)
            t2 = fnt.render("Press F2 to Replay", True, colors["txt"])
            scr.blit(t1, t1.get_rect(center=(W // 2, H // 2 - 20)))
            scr.blit(t2, t2.get_rect(center=(W // 2, H // 2 + 20)))

        pygame.display.flip()
        clk.tick(FPS)


if __name__ == "__main__":
    main()
