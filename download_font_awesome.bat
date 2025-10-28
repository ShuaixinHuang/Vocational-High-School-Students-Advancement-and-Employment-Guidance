@echo off

REM 创建必要的文件夹结构
mkdir -p libs/font-awesome/css
mkdir -p libs/font-awesome/fonts

REM 下载Font Awesome CSS文件
curl -o libs/font-awesome/css/font-awesome.min.css https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css

REM 下载必要的字体文件
curl -o libs/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0 https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/fonts/fontawesome-webfont.woff2
curl -o libs/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0 https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/fonts/fontawesome-webfont.woff
curl -o libs/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0 https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/fonts/fontawesome-webfont.ttf

REM 重命名字体文件，移除查询参数
ren "libs/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0" fontawesome-webfont.woff2
ren "libs/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0" fontawesome-webfont.woff
ren "libs/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0" fontawesome-webfont.ttf

echo Font Awesome已下载到本地！请修改HTML文件中的引用路径。