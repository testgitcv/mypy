from _typeshed.tkinter import DndSource
from tkinter import Event, Misc, Tk
from typing import ClassVar, Optional

class DndHandler:
    root: ClassVar[Optional[Tk]]
    def __init__(self, source: DndSource, event: Event[Misc]) -> None: ...
    def cancel(self, event: Optional[Event[Misc]] = ...) -> None: ...
    def finish(self, event: Optional[Event[Misc]], commit: int = ...) -> None: ...
    def on_motion(self, event: Event[Misc]) -> None: ...
    def on_release(self, event: Event[Misc]) -> None: ...

def dnd_start(source, event) -> Optional[DndHandler]: ...