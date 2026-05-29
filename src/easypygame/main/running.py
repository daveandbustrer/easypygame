from .variables import isRunning


def running():
    if isRunning:
        count = 0
        while isRunning:
            if count >= 100:
                isRunning = False
            count += 1
            pass
    pass
