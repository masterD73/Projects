# Reviewer: Mr. Braunstein.
from time import sleep
from datetime import datetime


class Machine:
    ON = True
    OFF = False
    MINUTE = 60

    def __init__(self, price=1) -> None:
        self.switch = Machine.OFF
        self.start_time = None
        self.end_time = None
        self.total_mins = 0
        self.curr_cost = 0
        self.price = price

    def machine_start(self) -> datetime:
        """
        Initiate service, record start time.
        :return: Start time.
        """
        if self.switch == Machine.OFF:
            self.start_time = datetime.now()
            self.end_time = None
            self.switch = Machine.ON
            print("Service Initiated.")
        else:
            print("Service already in progress.")
        return self.start_time

    def end_service(self) -> datetime:
        """
        Terminate service. Update cost and time data.
        :return: End time.
        """
        if self.switch == Machine.OFF:
            print("Service is not active.")
        else:
            self.switch = Machine.OFF
            self.end_time = datetime.now()
            self.total_mins += ((self.end_time - self.start_time).total_seconds()
                                / Machine.MINUTE)
            self.curr_cost = round(self.total_mins * self.price, 2)
            print("Service terminated.")
        return self.end_time

    def service_bill(self) -> float:
        """
        Calculate and print the currently accumulated bill.
        :return: currently accumulated bill
        """
        if self.switch == Machine.ON:
            time_passed = (datetime.now() - self.start_time).seconds / Machine.MINUTE
            print("$",
                  "{:.2f}".format(time_passed * self.price + self.curr_cost),
                  " as of now.")
            return round(time_passed * self.price + self.curr_cost, 2)
        print("$", self.curr_cost, "in total.")
        return self.curr_cost

    def time(self) -> tuple:
        """
        print the start and end time of current or last run, if possible.
        :return: tuple of start, end.
        """
        if self.switch == Machine.OFF:
            print("Service hasn't been initiated yet.")
            return None, None
        else:
            print(f"The service has been initiated at: {self.start_time}.")
            if self.end_time is None:
                print("Service is still being used.")
            else:
                print("The service ended on:", {self.end_time})
        return self.start_time, self.end_time

    def reset(self) -> None:
        """
        Reset the machine's data.
        :return: None
        """
        self.switch = Machine.OFF
        self.start_time = None
        self.end_time = None
        self.total_mins = 0
        self.curr_cost = 0


class Cheap(Machine):
    PRICE = 2

    def __init__(self) -> None:
        super().__init__()
        self.price = Cheap.PRICE


class Expensive(Machine):
    PRICE = 5

    def __init__(self) -> None:
        super().__init__()
        self.price = Expensive.PRICE


def main():
    # Stage 1.
    a, b, c, d = Cheap(), Cheap(), Cheap(), Expensive()
    a.machine_start(), b.machine_start(), c.machine_start(), d.machine_start()
    sleep(60)
    # Stage 2.
    e = Expensive()
    e.machine_start()
    sleep(60)
    # Stage 3.
    b.end_service()
    sleep(60)
    # Stage 4.
    results = {"a": a.service_bill(), "b": b.service_bill(),
               "c": c.service_bill(), "d": d.service_bill(),
               "e": e.service_bill()}
    # Print results
    print(results)
    print("sum of all services up to this moment in time is:", sum(results.values()))
    assert sum(results.values()) == 41
    print("Done.")


if __name__ == '__main__':
    main()
