#osu types
from enum import IntFlag

class CurveTypes(IntFlag):
    Catmull = 1,
    Bezier = 2,
    Linear = 3,
    PerfectCurve = 4

class HitObjectTypes(IntFlag):
	Circle = 1 << 0,
	Slider = 1 << 1,
	NewCombo = 1 << 2,
	Spinner = 1 << 3,
	ColourHax = 112,
	Hold = 1 << 7