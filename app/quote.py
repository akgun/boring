import wikiquote


def today():
    return '%s -%s' % wikiquote.quote_of_the_day()
