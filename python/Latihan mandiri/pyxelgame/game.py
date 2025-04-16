import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
STONE_INTERVAL = 30 
PLAYER_SIZE = 16
STONE_SIZE = 16

class Stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        self.y += 1  

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 32, 0, STONE_SIZE, STONE_SIZE, pyxel.COLOR_BLACK)

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="PYXELGAME")
        pyxel.load("my_resource.pyxres")

        self.best_score = 0  # Store the best score
        self.reset_game()

        self.facing_right = True  # Track player direction

        pyxel.run(self.update, self.draw)

    def reset_game(self):
        """Resets game variables to restart instantly."""
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT * 4 // 5
        self.stones = []
        self.is_collision = False
        self.score = 0  # Reset current score
        self.facing_right = True  # Reset direction to default

    def update(self):
        if pyxel.btnp(pyxel.KEY_R):  # Instantly restart when pressing "R"
            self.reset_game()

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if not self.is_collision:
            self.update_gameplay()

    def update_gameplay(self):
        self.score += 1  # Increase score each frame

        # Player movement
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - PLAYER_SIZE:
            self.player_x += 2
            self.facing_right = True  # Face right
        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 2
            self.facing_right = False  # Face left

        # Summon new stones
        if pyxel.frame_count % STONE_INTERVAL == 0:
            self.stones.append(Stone(pyxel.rndi(0, SCREEN_WIDTH - STONE_SIZE), 0))

        # Update stones & check for collision
        stones_to_remove = []
        for stone in self.stones:
            stone.update()

            # Collision Detection
            if (self.player_x < stone.x + STONE_SIZE and
                self.player_x + PLAYER_SIZE > stone.x and
                self.player_y < stone.y + STONE_SIZE and
                self.player_y + PLAYER_SIZE > stone.y):
                self.is_collision = True

                # Update best score if the current score is higher
                if self.score > self.best_score:
                    self.best_score = self.score

            # Remove stone if it goes out of screen
            if stone.y >= SCREEN_HEIGHT:
                stones_to_remove.append(stone)

        # Remove off-screen stones
        for stone in stones_to_remove:
            self.stones.remove(stone)

    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)

        # Draw stones
        for stone in self.stones:
            stone.draw()

        # Draw player (flip if facing left)
        direction = PLAYER_SIZE if self.facing_right else -PLAYER_SIZE
        pyxel.blt(self.player_x, self.player_y, 0, 16, 0, direction, PLAYER_SIZE, pyxel.COLOR_BLACK)

        # Display score
        pyxel.text(5, 5, f"Score: {self.score // 30}", pyxel.COLOR_WHITE)
        pyxel.text(5, 15, f"Best: {self.best_score // 30}", pyxel.COLOR_YELLOW)

        if self.is_collision:
            self.draw_centered_text("Game Over", SCREEN_HEIGHT // 2 - 10, pyxel.COLOR_YELLOW)
            self.draw_centered_text(f"Score: {self.score // 30}", SCREEN_HEIGHT // 2, pyxel.COLOR_WHITE)
            self.draw_centered_text(f"Best: {self.best_score // 30}", SCREEN_HEIGHT // 2 + 10, pyxel.COLOR_YELLOW)
            self.draw_centered_text("Press R to Restart", SCREEN_HEIGHT // 2 + 20, pyxel.COLOR_WHITE)

    def draw_centered_text(self, text, y, color):
        """Helper function to draw centered text."""
        text_width = len(text) * 4
        x = (SCREEN_WIDTH - text_width) // 2
        pyxel.text(x, y, text, color)

App()
