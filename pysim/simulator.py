from dataclasses import dataclass
import enum
import math
import random
import sqlite3
import threading
from time import time
import events
import json
import pathlib

VOLATILITY_FACTOR = 5

@dataclass
class StockMeta:
    @staticmethod
    def from_json_file(path: pathlib.Path) -> "StockMeta":
        with open(path, "r") as f:
            data = json.load(f)

        return StockMeta(
            stock_ticker=data["ticker"],
            stock_name=data["company_name"],
            biography=data["biography"],
            ipo=data["ipo"]
        )

    stock_ticker: str
    stock_name: str
    biography: str
    ipo: int

class MarketTrend(enum.Enum):
    BULL = (10 * VOLATILITY_FACTOR, 40 * VOLATILITY_FACTOR)
    BEAR = (-40 * VOLATILITY_FACTOR, -10 * VOLATILITY_FACTOR)
    STAGNANT = (-5 * VOLATILITY_FACTOR, 5 * VOLATILITY_FACTOR)


class Stock:
    def __init__(self, meta: StockMeta, *, write_to_disk: bool = False):
        self.name = meta.stock_name
        self.price = meta.ipo
        self.ipo = meta.ipo
        self.meta = meta
        self.trend = MarketTrend.STAGNANT
        self.surge_risk = 3
        self.crash_risk = 3

        self.mutex = threading.Lock()

        self.write_to_disk = write_to_disk

        if self.write_to_disk:
            with open(f"{self.name}_price.txt", "w") as f:
                f.write(f"{self.price}\n")

    def determine_trend(self):
        change_trend = random.randint(0, 10) == 0

        if change_trend:
            self.trend = random.choice(list(MarketTrend))
            print(f"Changing market trend to {self.trend.name}.")

    def crash_market(self):
        crash_amount = math.floor((random.randint(10, 50) / 100.0) * max(1, self.price))
        self.price -= crash_amount
        print(
            f"Crash! {self.name} drops by {crash_amount} cents to {self.price} cents."
        )

        self.crash_risk = 0

    def surge_market(self):
        surge_amount = math.floor(
            (random.randint(50, 100) / 100.0) * max(1, self.price)
        )
        self.price += surge_amount
        print(
            f"Surge! {self.name} rises by {surge_amount} cents to {self.price} cents."
        )

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
        if random.randint(1, 800) <= self.crash_risk:
            self.crash_market()
        elif random.randint(1, 800) <= self.surge_risk:
            self.surge_market()

    def simulate(self):
        with self.mutex:
            self.determine_correction()
            self.determine_trend()
            change = random.randint(*self.trend.value)
            self.price += change

            self.price = max(0, self.price)

            if self.write_to_disk:
                with open(f"{self.name}_price.txt", "a") as f:
                    f.write(f"{self.price}\n")

            print(
                f"Simulated {self.name}: change={change}, new price={self.price}, crash_risk={self.crash_risk}%, surge_risk={self.surge_risk}%"
            )

    def __repr__(self):
        return f"Stock(name={self.name}, price={self.price})"

    def __str__(self):
        return f"{self.name}: {self.price} cents"

    def event(self):
        events_manager = events.EventsManager()
        stock_description = events.StockDescription(
            name=self.name,
            biography="We are ACME. The leading provider of everything, from anvils to rockets. Our stock is known for its volatility due to our adventurous business strategies. An ACME product has never failed. And that's a binding contract in 50 states except for California. Invest in us to watch your money double in a matter of MINUTES, MINUTES, that's all it takes. We are not a ponzie scheme.",
            beforePrice=self.price
        )

        events_manager.dispatch_event(events.Event(events.EventType.BOOM, stock_description, 100))

        with self.mutex:
            print("Something should happen!")

class Market:
    def __init__(self,  stocks: list[Stock] = []):
        self.stocks = stocks

    def simulate(self):
        conn = sqlite3.connect("../market.db")
        cur = conn.cursor()

        for stock in self.stocks:
            stock.simulate()

            cur.execute(
                "INSERT INTO market_data (stock_ticker, price_cents, timestamp) VALUES (?, ?, ?)",
                (stock.meta.stock_ticker, stock.price, int(time()))
            )

        conn.commit()
        conn.close()

        # write market simulation to db
