# Modules
import random
import hashlib

from .colors import colored
from throwaway_keys.ext.logging import warn

# "Unsafe" generators
unsafe = [hashlib.md5, hashlib.sha1]

# Generators
def generate_base(generator, length):

    if generator in unsafe:
        warn("you are using an unsafe or crackable generator ({}); consider changing.".format(generator.__name__))

    # todo: change this to a different method of encryption
    num = str(random.randint(100 * 100 * 100, 999 * 100 * 100))
    hash = generator(num.encode("UTF-8"))

    try:
        return hash.hexdigest(length = length)
    except:
        if length != 75:
            warn("the generator you are using ({}) does not support custom length.".format(generator.__name__))

        return hash.hexdigest()

def make_hash(key, generator, length):

    try:
        return generator(key.encode("UTF-8")).hexdigest(length = length)
    except:
        return generator(key.encode("UTF-8")).hexdigest()

def generate_hash(generator, rounds, length):

    result = generate_base(generator, length)

    for _ in range(rounds):
        result = make_hash(result, generator, length)

    return result
