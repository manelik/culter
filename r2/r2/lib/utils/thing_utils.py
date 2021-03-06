from datetime import datetime
import pytz

def make_last_modified():
    last_modified = datetime.now(pytz.timezone('GMT'))
    last_modified = last_modified.replace(microsecond = 0)
    return last_modified

def last_modified_key(thing, action):
    return 'last_%s_%s' % (str(action), thing._fullname)

def last_modified_date(thing, action):
    """Returns the date that should be sent as the last-modified header."""
    from pylons import g
    cache = g.permacache

    key = last_modified_key(thing, action)
    last_modified = cache.get(key)
    if not last_modified:
        #if there is no last_modified, add one
        last_modified = make_last_modified()
        cache.set(key, last_modified)
    return last_modified

def set_last_modified(thing, action):
    from pylons import g
    key = last_modified_key(thing, action)
    g.permacache.set(key, make_last_modified())
