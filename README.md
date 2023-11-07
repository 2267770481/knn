# 基于KNN的图片识别

## KNN算法介绍
![image](https://github.com/2267770481/knn/assets/48823256/9ce91652-c420-4a2e-8490-63dbbfbf1368)
https://zhuanlan.zhihu.com/p/25994179
## 项目简介
```使用numpy和opencv实现的一个简易的knn图片识别模块```

### 项目结构
```
- code: 存放代码
  - create_collection.py: 创建数据集功能， 会将img中的图片建立数据集到data_collection下
  - knn.py: knn实现
- data_collection: 数据集存放目录
- img: 生成数据集的原始图片存放目录，生成数据集之后可以删掉
- test_data: 测试数据图片存放目录
```

### 使用
```
执行knn.py文件
```

### 测试结果展示
输入测试数据中的car.jpg（车）图片，k=3，执行knn.py之后，得到：
![image](https://github.com/2267770481/knn/assets/48823256/57c60e1e-3990-4d08-836e-7e5134a8ea4f)
