from config.Columns import Columns
from dataclasses import dataclass

@dataclass
class FileSampleInfo:
    input_filename: str
    output_filename: str
    column_index: Columns
    is_random: bool
    count: int
    time_filter_in_seconds: int
