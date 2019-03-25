try:
    raise ValueError
except Exception as e:
    raise IndexError('sorry') from e


# try:
#     raise ValueError
# except Exception as e:
#     raise IndexError('sorry') from None
