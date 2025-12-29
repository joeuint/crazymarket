#!/usr/bin/env python3

import time
import scheduler
import simulator
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    sched = scheduler.Scheduler()

    stock = simulator.Stock(name="ACME", price=1000, write_to_disk=True)
        
    sim_task = scheduler.PeriodicTask(callback=stock.simulate, interval=1.0)
    event_task = scheduler.PeriodicTask(callback=stock.event, interval=60.0)

    sched.add_task(sim_task)
    # sched.add_task(event_task)

    while True:
        sched.run()
        time.sleep(0.01)