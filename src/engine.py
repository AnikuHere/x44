import pygame
import sys

class X44Engine:
    def __init__(self):
        pygame.init()
        self.memory = {"clicks": 0} # Internal RAM for logic
        self.screen = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont("Courier New", 22)

    def run(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()

        while self.running:
            self.clock.tick(60)
            if self.screen: self.screen.fill((10, 10, 15))

            # --- INPUT SENSORS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Trigger the + Logic prefix manually for now
                    self.handle_cpu("INCREMENT_CLICKS")

            # --- INSTRUCTION DISPATCHER ---
            for line in lines:
                line = line.strip()
                if not line or line.startswith("--"): continue
                
                prefix = line[0]
                content = line[1:].strip()

                if prefix == "-": self.handle_gpu(content)
                elif prefix == "_": pass # Kernel logs already handled
                elif prefix == "#": self.handle_memory(content)

            if self.screen: pygame.display.flip()
        pygame.quit()

    def handle_gpu(self, content):
        if "window" in content:
            if not self.screen:
                self.screen = pygame.display.set_mode((800, 450))
                pygame.display.set_caption("X44 Interactive Engine")
        elif "draw_stat" in content and self.screen:
            # Displays the clicks from RAM
            msg = f"INTERACTION COUNT: {self.memory['clicks']}"
            img = self.font.render(msg, True, (255, 255, 100))
            self.screen.blit(img, (30, 80))
        elif "draw" in content and self.screen:
            msg = content.split('"')[1] if '"' in content else ""
            img = self.font.render(msg, True, (0, 255, 150))
            self.screen.blit(img, (30, 30))

    def handle_cpu(self, content):
        if "INCREMENT_CLICKS" in content:
            self.memory["clicks"] += 1
            print(f"[CPU] Logic: Clicks updated to {self.memory['clicks']}")

    def handle_memory(self, content):
        if "=" in content:
            var, val = content.split("=")
            self.memory[var.strip()] = val.strip()

if __name__ == "__main__":
    X44Engine().run(sys.argv[1])