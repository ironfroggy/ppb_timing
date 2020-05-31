# ppb_timing

ppb_timing is a timing system for [PursuedPyBear](https://ppb.dev/).

The library includes a `TimingSystem` to add to your PPB engine's `systems`
parameter and two utilities to utilize it: `repeat` and `delay`.


## Delaying an action

Delaying an action for a determined amount of time.

```python
from ppb_timing import delay

# Remove a sprite after 5 seconds have passed
delay(5.0, lambda: scene.remove(sprite))
```

## Repeating an action

Repeating an action every N seconds over time.

```python
from ppb_timing import repeat

# Make a sprite blink 20 times a second
def blink():
  if sprite.opacity == 255:
    sprite.opacity = 0
  else:
    sprite.opacity = 255
repeat(1/20, blink)
```

## Canceling a previous timer

Both `repeat()` and `delay()` return a `Timer` object which represents
the delayed or repeating action. The object also has a `cancel()` method
which will remove the timer from the timing system.

```python
from ppb_timing import delay, repeat

# Repeat for 5 seconds
t = repeat(1/20, blink)
delay(5.0, t.cancel)
```
