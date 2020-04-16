from .observer import AbsObserver
from .kpis import KPIs


class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis: KPIs):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print(f"Current Open tickets: {self.open_tickets}")
        print(f"Current Closed tickets: {self.closed_tickets}")
        print(f"Current New tickets: {self.new_tickets}")
        print(10 * "*")
