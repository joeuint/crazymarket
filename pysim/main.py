#!/usr/bin/env python3

import time
import scheduler
import simulator

if __name__ == "__main__":
    sched = scheduler.Scheduler()

    stock = simulator.Stock(name="ACME", price=1000, write_to_disk=True)
        
    periodic_task = scheduler.PeriodicTask(callback=stock.simulate, interval=0.001)

    sched.add_task(periodic_task)

    while True:
        sched.run()
        time.sleep(0.01)