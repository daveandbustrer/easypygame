from .variables import _isRunning


def running():
    if _isRunning:
        count = 0
        while _isRunning:
            if count >= 100:
                _isRunning = False
            count += 1
            pass
    pass
