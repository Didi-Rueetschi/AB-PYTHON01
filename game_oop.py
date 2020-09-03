import random

# Klasse "Game"
class Game:
    def __init__(self):
        # Start the game
        random.seed()
        self.correct = 0

        # Count
        self.count = -1
        while self.count<0 or self.count>10:
            try:
                print("How many tasks? (1 bis 10):")
                self.count = int(input())
            except:
                continue

    def play(self):
        #
        for i in range(1,self.count+1):
            a = Task(i, self.count)
            print(a)
            self.correct += a.answer()

    def __str__(self):
        # Result
        return "correct: " + str(self.correct) \
            + " von " + str(self.count)

# Klasse "Task"
class Task:
    # initialize Task
    def __init__(self, i, count):
        self.nr = i
        self.total = count

    # create Task
    def __str__(self):
        a = random.randint(10,30)
        b = random.randint(10,30)
        self.result = a + b
        return "Task " + str(self.nr) \
            + " out of " + str(self.total) + " : " \
            + str(a) + " + " + str(b)
        
    # the answers
    def answer(self):
        try:
            if self.result == int(input()):
                print(self.nr, ": ***correct ***")
                return 1
            else:
                raise
        except:
            print(self.nr, ": *** Wrong ***")
            return 0

# Hauptprogramm
s = Game()
s.play()
print(s)
