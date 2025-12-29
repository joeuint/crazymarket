#!/usr/bin/env python3

import time
import sqlite3

from dotenv import load_dotenv

import scheduler
import simulator

import pathlib

STOCKS_PATH = pathlib.Path(__file__).parent / "stocks"

def load_companies() -> list[simulator.StockMeta]:
    metas = []

    files = list(STOCKS_PATH.glob("*.json"))

    for file in files:
        if file.name == "company.schema.json":
            continue
        
        try: 
            meta = simulator.StockMeta.from_json_file(file)
        except Exception as e:
            print(f"Error loading {file}: {e}")
            print("Skipping this file.")
            continue

        metas.append(meta)

    return metas

if __name__ == "__main__":
    load_dotenv()

    metas = load_companies()

    stocks = []
    for meta in metas:
        stock = simulator.Stock(meta=meta, write_to_disk=True)
        stocks.append(stock)

    conn = sqlite3.connect("../market.db")
    cur = conn.cursor()

    # Drop table if exists for clean testing
    cur.execute("DROP TABLE IF EXISTS market_data")
    cur.execute("DROP TABLE IF EXISTS stocks_meta")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS market_data (
        stock_name TEXT,
        price_cents INTEGER,
        timestamp INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS stocks_meta (
        stock_ticker TEXT PRIMARY KEY,
        stock_name TEXT,
        biography TEXT
    )""")

    sched = scheduler.Scheduler()

    market = simulator.Market(stocks=stocks)
        
    sim_task = scheduler.PeriodicTask(callback=market.simulate, interval=0.1)

    sched.add_task(sim_task)
    # sched.add_task(event_task)

    while True:
        sched.run()
        time.sleep(0.01)