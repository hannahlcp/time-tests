import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):

    if end_time <= start_time:
        raise ValueError("End time must be greater than start time")
    
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    # Convert end_time_s and start_time_s to int
    end_time_s_int = int(end_time_s.timestamp())
    start_time_s_int = int(start_time_s.timestamp())

    if gap_between_intervals_s > (end_time_s_int - start_time_s_int):
        raise ValueError("Gap between intervals must be less than the total time range")
    
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            if low < high:
                overlap_time.append((low, high))
    return overlap_time

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 11:00:00", "2010-01-12 11:00:40", 2, 60)
    print(compute_overlap_time(large, short))