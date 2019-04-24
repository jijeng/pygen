# pygen

## Why pygen?

用于生成有关联的个人信息，包括人名，邮箱，ID Card (ssn)，电话，地址等信息，并且可以选择保存为 pandas dataframe格式, 数据库".db" 文件, Excel 文件和csv 文件格式，用于机器学习训练。

## Motivation

项目需要生成一些个人信息进行模型的预训练，没有找到开源的项目，目前使用最为广泛的开源库 faker在中文方面支持有限，所以开始造轮子。

## Prerequisites

- Python 3.6
- [xpinyin](https://github.com/lxneng/xpinyin)
- [faker](https://github.com/joke2k/faker)
- [namesex](https://pypi.org/project/namesex/)


## Installation
  
```python
>>> pip install xpinyin
>>> pip install faker
>>> pip install namesex
```

## Usage

可以参考我写的[这篇博客]()

## ToDo

- [ ] 提高根据姓名预测性别的精度，
- [ ] 优化姓氏和名字的列表，提高生成姓名的可读性（繁体/简体）
- [ ] 提供更多方面的个人数据的生成，比如邮编、工作职能


## Related Projects

[ID Card Calculation](https://github.com/jayknoxqu/id-number-util])

[pydbgen](https://github.com/tirthajyoti/pydbgen)

## Contribute

You're welcome to fork and make pull requests!

## License
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg?style=flat-square)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
