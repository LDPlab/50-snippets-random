from config.Columns import Columns
from dataclasses import dataclass

@dataclass
class SampleOption:
    key: str
    name: str
    column: Columns
    file_modifier: str
    count: int
    time_filter_in_seconds: int
    is_random: bool = False
