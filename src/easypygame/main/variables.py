from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional, Tuple

# private runtime state
_isRunning: bool = False
_height: Optional[int] = None
_width: Optional[int] = None
_size: Tuple[Optional[int], Optional[int]] = (_width, _height)
_screen: Optional["pygame.Surface"] = None
_busy:bool = False

# pygame module helpers
_display: Any = None
_time: Any = None
_events: Any = None
_clock: Any = None
_draw: Any = None
_surface: Any = None
_transform: Any = None

# control state
_func: Dict[str, Optional[Callable[..., Any]]] = {
    "mainLoop": None,
    "physicsLoop":None,
    "leftMouseDown": None,
    "rightMouseDown": None,
    "middleMouseDown": None,
    "mouseDown": None,
    "mouseWheel":None,
}

#info states
_fps: int|float = 0
_game_dt: float = 0.0
_physic_dt: float = 0.0

# shapes registered for drawing
_shapes: List[Any] = []

# public configuration
background: str = "white"
maxFrames: int = 60

