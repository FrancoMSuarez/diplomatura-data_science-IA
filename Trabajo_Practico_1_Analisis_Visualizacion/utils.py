from IPython.display import display, Markdown


def display_markdown(*args, **kwargs):
    return display(Markdown(*args, **kwargs))


def summarize_iterable(values, max_len=10):
    """
    Summarize an iterable object, such as a list or a set.

    Example:
    >>> summarize_iterable(range(100))
    '0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...'
    """
    if len(values) > max_len:
        summary_format = '{}, ...'
        summary_values = values[:max_len]
    else:
        summary_format = '{}'
        summary_values = values
    summary_reprs = (repr(value) for value in summary_values)
    return summary_format.format(', '.join(summary_reprs))
