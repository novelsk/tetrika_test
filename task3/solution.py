def appearance(intervals: dict[str, list[int]]) -> int:
    """Вычисление общего времени присутствия ученика и учителя на уроке."""
    result_gist = set(range(intervals['lesson'][0], intervals['lesson'][1]))
    pupil_gist = set()
    for i in range(0, len(intervals['pupil']), 2):
        pupil_gist |= set(range(intervals['pupil'][i], intervals['pupil'][i + 1]))
    tutor_gist = set()
    for i in range(0, len(intervals['tutor']), 2):
        tutor_gist |= set(range(intervals['tutor'][i], intervals['tutor'][i + 1]))
    return len(result_gist & pupil_gist & tutor_gist)
