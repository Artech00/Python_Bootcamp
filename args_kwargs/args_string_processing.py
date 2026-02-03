def process_text(*lines, lowercase=False, strip=False):
    result = []

    for line in lines:

        if lowercase:
            line = line.lower()

        if strip:  # if strip is True
            line = line.strip()
        result.append(line)

    # Combine lines in 1 string, with space between
    txt = " ".join(result)
    txt = txt.title()  # Uppercase first letter of each word

    print(result)
    print(txt)


process_text(
    "  No Space  ",
    " NO UPPERWORDS ",
    lowercase=True,
    strip=True
)
