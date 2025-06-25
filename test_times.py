import times
from pytest import raises

def test_times():
    large = times.time_range("2010-01-12 10:00:00","2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_times_notoverlapping():
    t0 = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    t1 = times.time_range("2010-01-13 10:00:00", "2010-01-13 12:00:00")
    result = times.compute_overlap_time(t0,t1)
    expected = []
    assert result == expected
    
def test_times_several_overlapping():
    t0 = times.time_range("2025-06-25 00:00:00", "2025-06-25 00:10:00", 2, 60)
    t1 = times.time_range("2025-06-25 00:05:00", "2025-06-25 00:15:00", 2, 60)
    result = times.compute_overlap_time(t0,t1)
    expected = [('2025-06-25 00:05:30', '2025-06-25 00:09:30')]
    assert result == expected

def test_times_several_overlapping2():
    t0 = times.time_range("2025-06-25 00:00:00", "2025-06-25 00:10:00", 4, 60)
    t1 = times.time_range("2025-06-25 00:05:00", "2025-06-25 00:20:00", 2, 60)
    result = times.compute_overlap_time(t0,t1)
    expected = [('2025-06-25 00:05:30', '2025-06-25 00:07:15'),("2025-06-25 00:08:15","2025-06-25 00:10:00")]
    assert result == expected

def test_times_start_end_same_time():
    t0 = times.time_range("2025-06-25 00:00:00", "2025-06-25 00:10:00")
    t1 = times.time_range("2025-06-25 00:10:00", "2025-06-25 00:15:00")
    result = times.compute_overlap_time(t0,t1)
    expected = []
    assert result == expected

def test_times_backward():
    with raises(ValueError, match = r"End time must be greater than start time"):
        times.time_range("2025-06-25 00:05:00", "2025-06-23 00:15:00")

def test_interval_larger_than_range():
    with raises(ValueError, match = r"Gap between intervals must be less than the total time range"):
        times.time_range("2025-06-25 00:00:00", "2025-06-25 00:00:10", 2, 20)

# To generate coverage report, run:
pytest --cov="times" --cov-report "html"