import struct
import sys
import io
def read_bmp_header(file_path):
        f = io.BytesIO(file_path)
        bmp_header = f.read(14)
        if bmp_header[:2] != b'BM':
            return "Not a Windows BMP"
        
        file_size = struct.unpack('<I', bmp_header[2:6])[0]  #размер BMP файла
        if len(file_path) != file_size:
            return "Incorrect size"

        dib_header_size = struct.unpack('<I', f.read(4))[0] #DIB header (первые 4 байта указывают на размер DIB header)
        if dib_header_size not in {12, 40, 52, 56, 64, 108, 124, 16, 32, 64}:
            return "Incorrect header size"
        
        
        dib = f.read(dib_header_size - 4)
        if dib_header_size < 40:
            width, height, i, color_depth = struct.unpack("<HHHH", dib[:8])
            return width, height, color_depth, 0, 0
        else:
            width, height, i, color_depth, compression_method, image_size = struct.unpack("<iiHHII", dib[:20])
            row_size = (width * color_depth + 31) // 32 * 4  # округление до кратного 4
            calculated_image_size = row_size * abs(height)
            if image_size != 0 and image_size != calculated_image_size and image_size != calculated_image_size + 2:
                return "Incorrect image size"

        return {
            'Width': abs(width),
            'Height': abs(height),
            'Color Depth': color_depth,
            'Compression Method': compression_method,
            'Padding Size': image_size - calculated_image_size
        }


file_path = sys.stdin.buffer.read()
result = read_bmp_header(file_path)

if isinstance(result, dict):
    print(*result.values())
else:
    print(result)
