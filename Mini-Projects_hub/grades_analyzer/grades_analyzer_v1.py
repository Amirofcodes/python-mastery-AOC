# grades_analyzer_v1.py

# --- Pure logic (no prints/input) ---

def average_score(records):
    """Return the arithmetic mean of scores."""
    num_of_scores = len(records)
    if num_of_scores == 0:
        return 0  # or raise ValueError("No records")
    sum_of_scores = sum(record[1] for record in records)
    avr_score = sum_of_scores / num_of_scores
    return avr_score


def min_score(records):
    """Return the (name, score) tuple with the minimum score."""
    return min(records, key=lambda t: t[1])


def max_score(records):
    """Return the maximum score who has it."""
    return max(records, key=lambda t: t[1])


def honors_list(records, threshold=90):
    """Return list of (name, score) for scores >= threshold using a list comprehension."""
    return [(n, s) for (n, s) in records if s >= threshold]


def curve_scores(records, increment=5, cap=100):
    """Return a NEW list with each score increased by `increment`, capped at `cap`."""
    return [(n, min(s + increment, cap)) for (n, s) in records]


def sort_by_score_desc(records):
    """Return a NEW list sorted by score descending."""
    # sorted(records, key=lambda t: t[1], reverse=True)
    return sorted(records, key=lambda t: t[1], reverse=True)


def compute_stats(records):
    """Return a dict with average, min, max, and count of records."""
    stats = {
        "average": average_score(records),
        "min": min_score(records),   # full tuple (name, score)
        "max": max_score(records),   # full tuple (name, score)
        "count": len(records),
    }
    return stats


# --- I/O & orchestration (printing only) ---

def format_record(item):
    """Return a nice 'Name: score' string for display."""
    name, score = item   # unpack the tuple
    return f"{name}: {score}"


def print_report(original, curved, stats, honors, honors_threshold=90):
    """
    Pretty-print the results and also return the full report as a string.

    Args:
        original: list[(name, score)]  — original records
        curved:   list[(name, score)]  — curved records
        stats:    dict                 — expects keys: 'average' (float),
                                         'min' (tuple), 'max' (tuple), 'count' (int)
        honors:   list[(name, score)]  — honors students (already filtered)
        honors_threshold: int          — threshold used to compute honors
    Returns:
        str: the complete report text
    """
    lines = []
    lines.append("=== Student Grades Report ===")
    lines.append(f"Average: {stats['average']:.2f}")
    lines.append(f"Lowest: {stats['min'][0]} — {stats['min'][1]}")
    lines.append(f"Highest: {stats['max'][0]} — {stats['max'][1]}")
    lines.append(f"Number of students: {stats['count']}")
    lines.append("")

    lines.append(f"Honors List (>= {honors_threshold}):")
    if honors:
        for student in sort_by_score_desc(honors):
            lines.append("  " + format_record(student))
    else:
        lines.append("  (none)")
    lines.append("")

    lines.append("Sorted Scores (Original):")
    for student in sort_by_score_desc(original):
        lines.append("  " + format_record(student))
    lines.append("")

    lines.append("Sorted Scores (Curved):")
    for student in sort_by_score_desc(curved):
        lines.append("  " + format_record(student))

    report = "\n".join(lines)
    print(report)
    return report


def main():
    records = [
        ("Alice", 88),
        ("Bob", 95),
        ("Cara", 72),
        ("Dan", 100),
        ("Eli", 90),
    ]

    # 1) Compute stats on original
    stats = compute_stats(records)

    # 2) Build honors list (original)
    honors = honors_list(records, threshold=90)

    # 3) Curve scores (+5, max 100)
    curved = curve_scores(records, increment=5, cap=100)

    # 4) Sort (desc)
    sorted_original = sort_by_score_desc(records)
    sorted_curved = sort_by_score_desc(curved)

    # 5) Print a neat report
    print_report(original=records, curved=curved, stats=stats, honors=honors)


if __name__ == "__main__":
    main()
