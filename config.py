# -*- coding:utf8 -*-
"""
@Author: Zhirui(Alex) Yang
@Date: 2021/4/25 下午11:07
"""

import os


__proj_dir = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(__proj_dir, 'recommender/data')

RAW_DIR = os.path.join(DATA_DIR, 'raw_data')
PRE_DIR = os.path.join(DATA_DIR, 'precossed_data')
RES_DIR = os.path.join(__proj_dir, 'res_data')


if __name__ == '__main__':
    print(f"DATA_DIR: {DATA_DIR}")