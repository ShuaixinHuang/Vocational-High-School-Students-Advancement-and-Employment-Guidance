import os
import requests
import shutil

# 创建必要的文件夹结构
os.makedirs('libs/font-awesome/css', exist_ok=True)
os.makedirs('libs/font-awesome/fonts', exist_ok=True)

# 下载Font Awesome CSS文件
css_url = 'https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css'
css_path = 'libs/font-awesome/css/font-awesome.min.css'

print('下载CSS文件: {}'.format(css_url))
response = requests.get(css_url)
with open(css_path, 'wb') as f:
    f.write(response.content)

# 下载字体文件
fonts = [
    ('https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/fonts/fontawesome-webfont.woff2', 'fontawesome-webfont.woff2'),
    ('https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/fonts/fontawesome-webfont.woff', 'fontawesome-webfont.woff'),
    ('https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/fonts/fontawesome-webfont.ttf', 'fontawesome-webfont.ttf')
]

for url, filename in fonts:
    font_path = 'libs/font-awesome/fonts/{}'.format(filename)
    print('下载字体文件: {}'.format(url))
    response = requests.get(url)
    with open(font_path, 'wb') as f:
        f.write(response.content)

print('Font Awesome已下载到本地！')

# 修改CSS文件中的字体路径
try:
    with open(css_path, 'r') as f:
        css_content = f.read()
    
    # 替换字体路径引用
    css_content = css_content.replace(
        '../fonts/fontawesome-webfont.woff2?v=4.7.0', 
        '../fonts/fontawesome-webfont.woff2'
    ).replace(
        '../fonts/fontawesome-webfont.woff?v=4.7.0', 
        '../fonts/fontawesome-webfont.woff'
    ).replace(
        '../fonts/fontawesome-webfont.ttf?v=4.7.0', 
        '../fonts/fontawesome-webfont.ttf'
    )
    
    with open(css_path, 'w') as f:
        f.write(css_content)
    
    print('CSS文件中的字体路径已更新！')
except Exception as e:
    print('修改CSS文件时出错: {}'.format(str(e)))