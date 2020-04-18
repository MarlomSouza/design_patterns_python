import abc
from observer.observer_abc import AbsObserver


class AbsSubject(metaclass=abc.ABCMeta):
    _observer = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from ABSObserver')
        self._observer |= {observer}

    def detach(self, observer):
        self._observer -= {observer}

    def notify(self, value=None):
        for observer in self._observer:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._observer.clear()
