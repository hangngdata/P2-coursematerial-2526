def cycle(xs):
    saved = []
    for element in xs:
        yield element
        saved.append(element)

    while saved:
        for element in saved:
            yield element
