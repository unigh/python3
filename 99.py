# -*- coding: UTF-8 -*-
# 九九乘法表(王鑫龙)
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()
