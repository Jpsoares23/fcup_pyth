def seconds(hour: int, min: int, sec: int) -> int:
    hours_in_seconds = hour * 3600
    minutes_in_seconds = min * 60

    total_seconds = hours_in_seconds + minutes_in_seconds + sec

    return total_seconds
