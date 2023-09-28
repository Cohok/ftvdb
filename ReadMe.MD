# 影视数据库建设

## 环境要求
Python Version：3.7.12  
    conda create pyscenedetect python=3.7.12  
必要库：  
    ffmpeg：pip install ffmpeg-python  
    pyscenedetect：pip install scenedetect[opencv] --upgrade （ 链接：https://github.com/Breakthrough/PySceneDetect ）  
    numpy：pip install numpy  
    matplotlib：pip install matplotlib  
    openCV：pip install opencv-python
ffmpeg安装并添加至path（ 链接：https://ffmpeg.org/download.html ）
    
## 文件目录管理
目录管理：  
“/”：根目录  
“/multimedia”：存放视频文件，包括原视频文件与切分镜头视频文件  
“/db”：存放数据库文件  
文件命名规则：  
“/”：根目录下只有py、ipynb文件，只用英文命名，无空格，用下划线 _ 链接  
“/input_videos”：准备加入数据库的视频文件，通过video类添加视频信息，这些信息最终添加到数据库中