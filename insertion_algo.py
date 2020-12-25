import time, random

class Algorithm:
    #random
    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name
    #visual
    def update_display(self, swap1=None, swap2=None):
        import insertion_visual

        insertion_visual.update(self, swap1, swap2)
    #running time
    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("Insertion Sort")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx = i
            while idx > 0 and self.array[idx-1] > cursor:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[idx] = cursor
            self.update_display(self.array[idx], self.array[i])
