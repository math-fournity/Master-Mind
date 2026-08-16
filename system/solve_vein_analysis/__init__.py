"""Independent solve-side nonlinear vein analysis pipeline.

This package intentionally does not import the absorb-side ``system.vein_analysis``
module or the shared legacy ``system.schema`` module.  Its first release is an
offline, deterministic POC over a canonical reasoning-event trajectory.
"""

from .models import (
    AnalysisBundle,
    EdgeRelation,
    EventKind,
    EventStatus,
    ReasoningDag,
    ReasoningEvent,
    ReasoningTrajectory,
    TrajectoryValidationError,
)
from .pipeline import analyze_incrementally, analyze_trajectory

__all__ = [
    "AnalysisBundle",
    "EdgeRelation",
    "EventKind",
    "EventStatus",
    "ReasoningDag",
    "ReasoningEvent",
    "ReasoningTrajectory",
    "TrajectoryValidationError",
    "analyze_incrementally",
    "analyze_trajectory",
]

__version__ = "0.1.0"
