# iterative
# def reverse_from_left(text):
#     if not text:
#         return ""
#     if len(text) == 1:
#         return text
#     new = ""
#     for i in range(0, len(text)):
#         new = text[i] + new
#     return new

def reverse_from_left(text):
    if not text:
        return ""

    return reverse_from_left(text[1:]) + text[0]


# Iterative
# def reverse_from_right(text):
#     if not text:
#         return ""
#     if len(text) == 1:
#         return text
#     new = ""
#     for i in range(len(text)-1, -1, -1):
#         new = new + text[i]
#     return new

def reverse_from_right(text):
    if not text:
        return ""
    return text[-1] + reverse_from_right(text[:-1])