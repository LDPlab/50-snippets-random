from models.SampleOption import SampleOption
from .Columns import Columns

sample_options = {
    "1a": SampleOption("1a", "AWC Top 55 clips", Columns.AWC, "_55snippets_awc", 55, 180),
    "1b": SampleOption("1b", "AWC Top 105 clips", Columns.AWC, "_105snippets_awc", 105, 120),
    "1c": SampleOption("1c", "Random 55 with non zero AWC", Columns.AWC, "_55snippets_awc_random", 55, 180, True),
    "2a": SampleOption("2a", "TVN Top 55 clips", Columns.TVN, "_55snippets_tvn", 55, 60),
    "2b": SampleOption("2b", "TVN Top 105 clips", Columns.TVN, "_105snippets_tvn", 105, 60),
    "2c": SampleOption("2c", "Random 55 with non zero TVN", Columns.TVN, "_55snippets_tvn_random", 55, 60, True),
    "3a": SampleOption("3a", "CTC Top 55 clips", Columns.CTC, "_55snippets_ctc", 55, 180),
    "3b": SampleOption("3b", "CTC Top 105 clips", Columns.CTC, "_105snippets_ctc", 105, 120),
    "3c": SampleOption("3c", "Random 55 with non zero CTC", Columns.CTC, "_55snippets_ctc_random", 55, 180, True),
    "4a": SampleOption("4a", "CVC Top 55 clips", Columns.CVC, "_55snippets_cvc", 55, 180),
    "4b": SampleOption("4b", "CVC Top 105 clips", Columns.CVC, "_105snippets_cvc", 105, 120),
    "4c": SampleOption("4c", "Random 55 with non zero CVC", Columns.CVC, "_55snippets_cvc_random", 55, 180, True),
    "5a": SampleOption("5a", "MAN Top 55 clips", Columns.MAN, "_55snippets_man", 55, 60),
    "5b": SampleOption("5b", "MAN Top 105 clips", Columns.MAN, "_105snippets_man", 105, 60),
    "5c": SampleOption("5c", "Random 55 with non zero MAN", Columns.MAN, "_55snippets_man_random", 55, 60, True),
    "6a": SampleOption("6a", "FAN Top 55 clips", Columns.FAN, "_55snippets_fan", 55, 60),
    "6b": SampleOption("6b", "FAN Top 105 clips", Columns.FAN, "_105snippets_fan", 105, 60),
    "6c": SampleOption("6c", "Random 55 with non zero FAN", Columns.FAN, "_55snippets_fan_random", 55, 60, True),
}