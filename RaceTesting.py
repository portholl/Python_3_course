from itertools import cycle
def speed(path, stops, times):
    path = iter(path)
    stops = cycle(stops)
    times = iter(times)
    while True:
        distance = 0
        stops_idx = next(stops)
        for _ in range(stops_idx):
            if (next_path := next(path, None)) is not None:
                distance += next_path
            else:
                if distance > 0 and (next_time := next(times, None)) is not None:
                    yield distance / next_time
                return  
        next_time = next(times, None)
        if next_time is not None:
            yield distance / next_time
        else:
            return