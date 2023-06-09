from models.SampleOption import SampleOption
from .Columns import Columns

sample_options = {
    "1a": SampleOption("1a", "AWC Top 55 clips", Columns.AWC, "_55snippets_awc", 55, 180),
    "1b": SampleOption("1b", "AWC Top 105 clips", Columns.AWC, "_105snippets_awc", 105, 120),
    "1c": SampleOption("1c", "Random 55 with non zero AWC", Columns.AWC, "_55snippets_random", 55, 180, True),
    "2a": SampleOption("2a", "TVN Top 55 clips", Columns.TVN, "_55snippets_tvn", 55, 60),
    "2b": SampleOption("2b", "TVN Top 105 clips", Columns.TVN, "_105snippets_tvn", 105, 60),
    "3a": SampleOption("3a", "CTC Top 55 clips", Columns.CTC, "_55snippets_ctc", 55, 180),
    "3b": SampleOption("3b", "CTC Top 105 clips", Columns.CTC, "_105snippets_ctc", 105, 120),
    "4a": SampleOption("4a", "CVC Top 55 clips", Columns.CVC, "_55snippets_cvc", 55, 180),
    "4b": SampleOption("4b", "CVC Top 105 clips", Columns.CVC, "_105snippets_cvc", 105, 120),
    "5a": SampleOption("5a", "MAN Top 55 clips", Columns.MAN, "_55snippets_man", 55, 60),
    "5b": SampleOption("5b", "MAN Top 105 clips", Columns.MAN, "_105snippets_man", 105, 60),
    "6a": SampleOption("6a", "FAN Top 55 clips", Columns.FAN, "_55snippets_fan", 55, 60),
    "6b": SampleOption("6b", "FAN Top 105 clips", Columns.FAN, "_105snippets_fan", 105, 60)
}