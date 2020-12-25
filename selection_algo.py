import random, time

class Algorithm:
    #random
    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name
    #visual
    def update_display(self, swap1=None, swap2=None):
        import selection_visual

        selection_visual.update(self, swap1, swap2)
    #running time
    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("Selection Sort")
    def algorithm(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update_display(self.array[i], self.array[min_idx])