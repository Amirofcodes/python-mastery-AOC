# --- Pure logic (no input/print) ---
def normalize_text(text):
    """Return lowercase text with punctuation stripped (non-alnum -> space)."""
    chars = []
    for ch in str(text).lower():
        if ch.isalnum() or ch.isspace():
            chars.append(ch)
        else:
            chars.append(" ")
    return "".join(chars)


def tokenize(text):
    """Split normalized text into words (list of strings)."""
    return text.split()


def unique_words(words):
    """Return a set of unique words from a list."""
    return set(words)


def frequency_dict(words):
    """Return a dict {word: count}."""
    # Hint: loop over words; if key not in dict, initialize to 0 then increment.
    # No collections.Counter yet (saving that for later sections).
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_n(freqs, n=5):
    """Return a list of (word, count) pairs, top n by count desc, then word asc."""
    sorted_items = sorted(freqs.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]


# --- I/O & orchestration (printing only) ---

def print_report(text, n_top=5):
    """Normalize, count, and print unique count + top N."""
    normalized = normalize_text(text)
    words = tokenize(normalized)
    uniques = unique_words(words)
    freqs = frequency_dict(words)
    top = top_n(freqs, n_top)
    print(f"Unique words: {len(uniques)}")
    print(f"Top {n_top} words:")
    for word, count in top:
        print(f" {word}: {count}")


def main():
    # For v1: hardcode a sample paragraph (no user input yet).
    sample = (
        "Hello, hello! This is a test. A quick, QUICK test; isn't it nice?"
        " Punctuation—like dashes—and symbols #$% should be removed."
    )
    print_report(sample, n_top=5)


if __name__ == "__main__":
    main()
