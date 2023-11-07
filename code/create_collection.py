"""将图片解析到数据集
    图片的命名规则为 <label>_<swq>.jpg  例如 cat_01.jpg 也可以是png图片
"""
import json
import os.path

import cv2 as cv


def img2binary(img_path):
    """
    图像二值化并建立数据集
    :param img_path: 绝对路径
    :return:
    """
    org = cv.imread(img_path, 0)
    img = cv.resize(org, (32, 32), interpolation=cv.INTER_CUBIC)
    img = cv.medianBlur(img, 5)
    ret = cv.adaptiveThreshold(img, 1, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    print(ret)
    name = os.path.basename(img_path).split('.')[0] + '.txt'

    with open(os.path.join('../data_collection', name), 'w') as f:
        for row_words in ret:
            f.write(''.join(str(word) for word in row_words))
            f.write('\n')


if __name__ == '__main__':
    for i in os.listdir('D:\work\code\my_knn\img'):
        img2binary(os.path.join('D:\work\code\my_knn\img', i))
