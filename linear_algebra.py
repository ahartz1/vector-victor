class ShapeException(Exception):
    pass

import math


def shape(vec):
    return (len(vec),)


def vector_add(vec1, vec2):
    if shape(vec1)[0] == shape(vec2)[0]:
        ret = [vec1[n] + vec2[n]           # collection
               for n in range(shape(vec1)[0]) # iteration
               ]
    else:
        raise ShapeException('Shape rule: the vectors must be the same size.')
    return ret


def vector_sub(vec1, vec2):
    if shape(vec1)[0] == shape(vec2)[0]:
        ret = [vec1[n] - vec2[n]           # collection
               for n in range(shape(vec1)[0]) # iteration
               ]
    else:
        raise ShapeException('Shape rule: the vectors must be the same size.')
    return ret


def vector_sum(*vectors):
    # if shape(vec1)[0] == shape(vec2)[0]:
    #     ret = [vec1[n] + vec2[n]           # collection
    #            for n in range(shape(vec1)[0]) # iteration
    #            ]
    # else:
    #     raise ShapeException('Shape rule: the vectors must be the same size.')
    # return ret
    pass



def dot(vec1, vec2):
    pass


def vector_multiply(vec1, scalar):
    pass


def vector_mean(vec):
    pass


def magnitude(vec):
    pass
