# Reviewer: Alexander.
from time import sleep
from oop.exc3 import Machine

COST = 0.17
SECONDS = 10


def test_machine_initiated():
    a = Machine()
    a.machine_start()
    assert a.switch is True


def test_machine_end():
    a = Machine()
    a.machine_start()
    a.end_service()
    assert a.switch is False


def test_end_before_start():
    a = Machine()
    a.end_service()
    assert a.switch is False


def test_start_after_start():
    a = Machine()
    a.machine_start()
    a.machine_start()
    assert a.switch is True


def test_machine_cost():
    a = Machine()
    a.machine_start()
    sleep(SECONDS)
    a.end_service()
    assert a.curr_cost == COST and a.service_bill() == COST


def test_running_cost():
    a = Machine()
    a.machine_start()
    sleep(SECONDS)

    assert a.service_bill() == COST and a.curr_cost == 0
