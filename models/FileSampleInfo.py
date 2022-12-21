from config.Columns import Columns

class FileSampleInfo:
    def __init__(self,
                 input_filename: str,
                 output_filename: str,
                 column_index: Columns,
                 is_random: bool,
                 count: int = 55):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.column_index = column_index
        self.is_random = is_random
        self.count = count
