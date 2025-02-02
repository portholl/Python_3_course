import sys
import tarfile
import io
import gzip

def count(tar):
    files = 0
    size = 0
    for i in tar.getmembers():
        if i.isfile():  
            files += 1
            size += i.size
    print(size, files)

hex_archive = sys.stdin.read()
hex_archive = ''.join(hex_archive.split())
binary_data = bytes.fromhex(hex_archive)
if binary_data[:2] == b'\x1f\x8b':
    with gzip.open(io.BytesIO(binary_data), mode='rb') as gz:
        with tarfile.open(fileobj=gz, mode='r') as tar:
            count(tar)
else:
        with tarfile.open(fileobj=io.BytesIO(binary_data), mode='r') as tar:
            count(tar)