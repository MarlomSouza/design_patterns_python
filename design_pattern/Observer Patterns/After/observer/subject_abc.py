import abc
from observer_abc import AbsObserver


class AbsSubject(object):
    __metaclass__ = abc.ABCMeta
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
