# from distutils.core import setup, Extension
# from Cython.Build import cythonize
# import numpy

# # setup(
# #     ext_modules=[
# #         Extension("AoC_16", ["AoC_16.c"],
# #                   include_dirs=[numpy.get_include()]),
# #     ],
# # ) 



# setup(
#     ext_modules = cythonize("AoC_16.pyx")
# )

# # setup(
# #     ext_modules=cythonize(
# #         "AoC_16.pyx",
# #         include_dirs=[numpy.get_include()],
# #     )
# # )

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    ext_modules=cythonize("AoC_16.pyx"),
    include_dirs=[numpy.get_include()],
    compiler_directives={'language_level' : "3"}
)