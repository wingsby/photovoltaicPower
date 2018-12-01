import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np

path = 'E:/tcdata/photovoltaic_power/'


def readData(type, fileid):
    name = path + type + '_%d.csv' % fileid
    df1 = pd.read_csv(name, sep=',', header=0)
    df1.head()
    tmp = df1['时间']

    lday = []
    hm = []

    for str in tmp:
        tmpt = time.strptime(str, "%Y-%m-%d %H:%M:%S")
        lday.append(tmpt.tm_yday)
        hm.append(tmpt.tm_hour + tmpt.tm_min / 60)
    # df1=pd.concat([df1, pd.DataFrame(columns=['lday','hm'])])
    # df1['lday'] = lday
    # df1['hm'] = hm
    # print(df1.corr())
    # figure=plt.figure()
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    # plt.plot(np.array(lday), np.array(hm))
    # plt.plot(df1['温度'],'*')
    # figure.show()



    # print(np.corrcoef(df1['实际功率'],df1['实发辐照度'])[0,1])
    # print(np.corrcoef(df1['实际功率'], df1['实发辐照度'] - 20 * df1['湿度'] * df1['湿度'])[0, 1])
    # print(np.corrcoef(df1['实际功率'], df1['实发辐照度']+1 /df1['湿度'] )[0, 1])
    # print(np.corrcoef(df1['实际功率'],df1['实发辐照度']-80*df1['温度']*df1['温度'])[0,1])
    # print(np.corrcoef(df1['实际功率'],df1['实发辐照度']-85*df1['温度']*df1['温度'])[0,1])
    # print(np.corrcoef(df1['实际功率'],df1['实发辐照度']-85*df1['温度']*df1['温度'] - 20 * df1['湿度'] * df1['湿度'])[0,1])
    hm=np.array(hm)

    ind=np.where((hm>7) & (hm<19))
    final=np.array(df1['实际功率'])
    real=np.array(df1['实发辐照度'])
    pred=np.array(df1['辐照度'])

    print(np.corrcoef(real[ind],pred[ind])[0, 1])
    print(np.corrcoef(final[ind],pred[ind])[0, 1])
    print(np.corrcoef(real[ind], final[ind])[0, 1])



str = '辐照度 风速 温度 湿度'

readData('train', 1)

