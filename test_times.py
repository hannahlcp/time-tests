import times

def test_times():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2020-01-01 00:02:00', '2020-01-01 00:03:00'), ('2020-01-01 00:08:00', '2020-01-01 00:09:00')]
    assert result == expected

