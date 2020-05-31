from dataclasses import dataclass
from types import FunctionType
from typing import Optional

import ppb
from ppb.systemslib import System
from ppb.utils import get_time


@dataclass
class Timer:
    end_time: float
    callback: FunctionType
    repeating: float = 0
    clear: bool = False
    until: float = None

    def __hash__(self):
        return hash(id(self))
    
    def cancel(self):
        self.clear = True


class Timers(System):
    timers = set()

    @classmethod
    def delay(cls, seconds, func):
        t = Timer(get_time() + seconds, func)
        cls.timers.add(t)
        return t
    
    @classmethod
    def repeat(cls, seconds, func, until=None):
        n = get_time()
        t = Timer(n + seconds, func, repeating=seconds, until=n + until)
        cls.timers.add(t)
        return t

    @classmethod
    def on_idle(cls, idle, signal):
        clear = []
        for t in list(cls.timers):
            if t.clear:
                clear.append(t)
            else:
                now = get_time()
                if now >= t.end_time:
                    if t.until is None or t.until > now:
                        t.callback()
                    if t.repeating > 0:
                        if t.until is None or t.until > now:
                            t.end_time += t.repeating
                            continue
                    clear.append(t)
        for t in clear:
            cls.timers.remove(t)


delay = Timers.delay
repeat = Timers.repeat
