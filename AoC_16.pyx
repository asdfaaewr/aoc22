import cython
from cython.view cimport array as cvarray
import numpy as np
cimport numpy as np

cdef (char, char, char, char, char, char,char, char, char, char, char, char, char, char, char,) is_closed
is_closed = tuple([1]*15)

#is_closed = (1,) * 15

possibility_dict = {}
possibility_dict.update({is_closed : 'test'})

print(possibility_dict)


cdef tuple open_valve(tuple is_closed, int idx):
    #cdef (char, char, char, char, char, char,char, char, char, char, char, char, char, char, char,) out
    cdef list new_l[] 
    new_l = list(is_closed)
    #new_l[non_zero_list[idx]] = 0
    return tuple(new_l)

cpdef int test(np.ndarray[int, ndim=1] non_zero_list,
               np.ndarray[int, ndim=1] flow, 
               np.ndarray[list, ndim=1] tunnels):

    print(open_valve(is_closed, int(3)))

    return np.sum(flow)

