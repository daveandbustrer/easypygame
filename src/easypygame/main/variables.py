"""private"""

# running variables
_isRunning = False

# displays variables
_height = None
_width = None
_size = (_width, _height)
_screen = None

# pygame variables
_display = None
_time = None
_events = None
_clock = None

# control variables
_dt = 0
_func = {
    "main": None,
}
# shape variables
_shapes = []

""" public """
background = None
frames = 60
