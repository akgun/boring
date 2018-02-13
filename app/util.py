import click


def read_stream():
    stdin = click.get_text_stream('stdin')
    if not stdin.isatty():
        return [line.strip() for line in stdin]
    return []
