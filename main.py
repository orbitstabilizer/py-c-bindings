# import ctypes
# import pathlib


# if __name__ == '__main__':
#     # Get the path to the DLL file
#     dll_path = pathlib.Path().absolute() / 'libcmult.so'

#     # Load the DLL
#     lib = ctypes.CDLL(dll_path)
#     # Call the function
#     lib.cmult.argtypes = (ctypes.c_int, ctypes.c_int)
#     lib.cmult.restype = ctypes.c_int
#     print(lib.cmult(3, 4))

import cffi_example
print(cffi_example.lib.cmult(3, 4))
