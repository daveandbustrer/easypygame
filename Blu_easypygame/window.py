from . import var


def __getattr__(name: str):
    if name in {"bg", "width", "height", "fps"}:
        return getattr(var, name)

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
