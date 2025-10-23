from PIL import Image
import sys

# 确保中文显示正常
def convert_to_webp(input_file, output_file, quality=80):
    try:
        img = Image.open(input_file)
        # 转换为RGB模式（如果不是）
        if img.mode == 'RGBA':
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        # 保存为WebP格式
        img.save(output_file, 'WEBP', quality=quality)
        print("转换成功：" + output_file)
    except Exception as e:
        print("转换失败：" + str(e))

if __name__ == "__main__":
    convert_to_webp('1111.png', '1111.webp')