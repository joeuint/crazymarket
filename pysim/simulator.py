import enum
import math
import random

STAGNANT_MAX_CHANGE = 5
STAGNANT_MIN_CHANGE = -5

class MarketTrend(enum.Enum):
    BULL = (10, 40)
    BEAR = (-40, -10)
    STAGNANT = (-5, 5)

class Stock():
    def __init__(self, name: str, price: int, *, write_to_disk: bool = False):
        self.name = name
        self.price = price
        self.ipo = price
        self.trend = MarketTrend.STAGNANT
        self.surge_risk = 3 # percentage
        self.crash_risk = 3 # percentage

        self.write_to_disk = write_to_disk

        if self.write_to_disk:
            with open(f"{self.name}_price.txt", "w") as f:
                f.write(f"{self.price}\n")

    def determine_trend(self):
        change_trend = random.randint(0, 5) == 0

        if change_trend:
            self.trend = random.choice(list(MarketTrend))
            print(f"Changing market trend to {self.trend.name}.")

    def crash_market(self):
        crash_amount = math.floor((random.randint(10, 50) / 100.0) * max(1, self.price))
        self.price -= crash_amount
        print(f"Crash! {self.name} drops by {crash_amount} cents to {self.price} cents.")

        self.crash_risk = 0

    def surge_market(self):
        surge_amount = math.floor((random.randint(50, 100) / 100.0) * max(1, self.price))
        self.price += surge_amount
        print(f"Surge! {self.name} rises by {surge_amount} cents to {self.price} cents.")

        self.surge_risk = 0
            
    def determine_correction(self):
        # Don't look at this :(
        if self.price > self.ipo * 1.5:
            self.surge_risk -= random.randint(0, 4)
            self.crash_risk += random.randint(0, 4)
        elif self.price > self.ipo * 1.25:
            self.surge_risk -= random.randint(-1, 2)
            self.crash_risk += random.randint(-1, 2)
        elif self.price < self.ipo * 0.75:
            self.surge_risk += random.randint(-1, 2)
            self.crash_risk -= random.randint(-1, 2)
        elif self.price < self.ipo * 0.5:
            self.crash_risk -= random.randint(0, 4)
            self.surge_risk += random.randint(0, 4)
        else:
            self.surge_risk += random.randint(-1, 2)
            self.crash_risk += random.randint(-1, 2)

        self.surge_risk = max(0, self.surge_risk)
        self.crash_risk = max(0, self.crash_risk)

        # determine if a correction happens
        if random.randint(1, 100) <= self.crash_risk:
            self.crash_market()
        elif random.randint(1, 100) <= self.surge_risk:
            self.surge_market()


    def simulate(self):
        self.determine_correction()
        self.determine_trend()
        change = random.randint(*self.trend.value)
        self.price += change

        self.price = max(0, self.price)

        if self.write_to_disk:
            with open(f"{self.name}_price.txt", "a") as f:
                f.write(f"{self.price}\n")

        print(f"Simulated {self.name}: change={change}, new price={self.price}, crash_risk={self.crash_risk}%, surge_risk={self.surge_risk}%")

    def __repr__(self):
        return f"Stock(name={self.name}, price={self.price})"
    
    def __str__(self):
        return f"{self.name}: {self.price} cents"