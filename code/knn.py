import operator
import os

import cv2 as cv
import numpy as np


class KNN:
    def __init__(self, data_collection_path):
        self.data_collection_path = data_collection_path
        self._collection = []
        self._labels = []
        self._total_labels = 0

        self._init_data_collection()

    @staticmethod
    def img2binary(img_path) -> np.array:
        """
        图像二值化
        :param img_path:
        :return: [[],[],[]] 是一个32行 32列的数组
        """
        org = cv.imread(img_path, 0)
        img = cv.resize(org, (32, 32), interpolation=cv.INTER_CUBIC)
        img = cv.medianBlur(img, 5)
        binary = cv.adaptiveThreshold(img, 1, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        return binary

    def _save_collection(self, collection_name, binary):
        with open(os.path.join(self.data_collection_path, collection_name), 'w') as f:
            for row_words in binary:
                f.write(''.join(str(word) for word in row_words))
                f.write('\n')

    def _init_data_collection(self):
        """初始化数据集
        将数据集目录下的每片数据集整合起来，变成一个二维表，返回二维表和每个子集对应的标签名"""
        for _file in os.listdir(self.data_collection_path):
            tmp = []
            with open(os.path.join(self.data_collection_path, _file)) as f:
                tmp = [int(i) for i in f.read().replace('\n', '')]
            self._collection.append(tmp)
            self._labels.append(_file.split('_')[0])
            self._total_labels += 1

        self._collection = np.array(self._collection)

    def classify(self, input_img, k) -> str:
        """
        knn归类
        :param input_img: 输入图片 需要绝对路径
        :param k: k值
        :return: 输入数据属于的标签
        """

        # 1.计算测试数据与各训练数据之间的距离。
        _binary = self.img2binary(input_img)
        _input = _binary.flatten()
        x = np.tile(_input, (self._total_labels, 1)) - self._collection
        x_positive = x ** 2
        x_distances = x_positive.sum(axis=1)
        distances = np.sqrt(x_distances)
        print(1111)

        # 2.按照距离的大小进行排序。
        sort_dis_index = distances.argsort()

        # 3.选择其中距离最小的k个样本点。4.确定K个样本点所在类别的出现频率。
        class_count = {}  # 创建字典：label为键，频数为值
        for i in range(k):
            get_label = self._labels[sort_dis_index[i]]
            class_count[get_label] = class_count.get(get_label, 0) + 1

        print(1111, class_count)
        # 5.返回K个样本点中出现频率最高的类别作为最终的预测分类。
        sort_class = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
        print(sort_class[0][0])

        return sort_class[0][0]


if __name__ == '__main__':
    knn = KNN(r'D:\work\code\my_knn\data_collection')
    res = knn.classify(r'D:\work\code\my_knn\test_data\car.jpg', 3)
    print('识别到的东西为：', res)
