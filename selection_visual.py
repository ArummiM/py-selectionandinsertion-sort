import  selection_algo, time, os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

dimensions = (1024, 512) 

# Pygame Initialisation
pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("pink"))

def play_sound(swap):
    duration = 0.01
    freq = 20
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq+swap*10))

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

def update(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color("pink"))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting".format(algorithm.name, time.time() - algorithm.start_time))
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (0,0,0)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_events()
    pygame.display.update()

def keep_open(algorithm, display, time):
    pygame.display.set_caption("Sorting Visualizer   Algorithm: {}     Time: {:.3f}      Status: Done".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():

        algorithm = selection_algo.SelectionSort()
        try:
            time_elapsed = algorithm.run()[1]
            keep_open(algorithm, display, time_elapsed)
            pass
        except:
            pass

if __name__ == "__main__":
    main()