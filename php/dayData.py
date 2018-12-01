import time

import numpy as np


def getdayData(type,batch_size,fileid=1):
    # filename = '/dpdata/photovoltaic_power/data/train_%d.csv' % fileid
    filename = 'e:/tcdata/photovoltaic_power/%s_%d.csv' % (type,fileid)
    while (1):
        with open(filename, encoding='utf-8') as file:
            cnt = 0
            batchcnt=0
            daycnt=-1
            titles = []
            datalist = []
            labels = []
            daydata=[]
            for line in file:
                if cnt < 1:
                    titles = line.split(',')
                else:
                    data = line.split(',')
                    mstime = data[0].split('.')
                    ctime = time.strptime(mstime[0], "%Y-%m-%d %H:%M:%S")
                    if mstime.__len__() > 1:
                        ctime = time.localtime(time.mktime(ctime) + round(float(mstime[1]) / 1000))
                    if (daycnt!=ctime[2] and daycnt != -1):
                        #     day feature( mean std var peak ...)
                        tmp = np.array(daydata).astype(float)
                        mean = []
                        var = []
                        max = []
                        min = []
                        mean.append(np.mean(tmp, 0))
                        max.append(np.max(tmp, 0))
                        # min.append(np.min(tmp,0))
                        var.append(np.var(tmp, 0))
                        for j in range(daydata.__len__()):
                            tmpndata = daydata[j]
                            for i in range(5):
                                tmpndata.append(tmpndata[i + 5] - mean[0][i + 5])
                                # tmpndata.append(tmpndata[i + 5] /(max[0][i + 5]+2))
                                # tmpndata.append(min[0][i+5])
                                tmpndata.append(var[0][i + 5])
                            datalist.append(tmpndata)
                        daydata = []
                        batchcnt+=1
                        if (batch_size > 0 and batchcnt >= batch_size):
                            yield (datalist, labels)
                            datalist = []
                            labels = []
                            batchcnt = 0
                    ndata = []
                    ndata.append(ctime[0])
                    ndata.append(ctime[1])
                    ndata.append(ctime[2])
                    ndata.append(ctime[3])
                    ndata.append(ctime[4])
                    # 5
                    ndata.append(float(data[1]))
                    ndata.append(float(data[2]))
                    # ndata.append(float(data[3]))
                    ndata.append(float(data[4]))
                    ndata.append(float(data[5]))
                    ndata.append(float(data[6]))
                    ndata.append(float(data[1])-50*pow(float(data[4]),2))
                    ndata.append(float(data[1])-50*pow(float(data[6]),2))
                    daydata.append(ndata)
                    daycnt=ctime[2]
                    label = float(data[8])
                    labels.append(label)
                cnt += 1
                # print(datalist.__len__())




def getValorPredict(type,fileid=1,yflag=True):
    # filename = '/dpdata/photovoltaic_power/data/train_%d.csv' % fileid
    filename = 'e:/tcdata/photovoltaic_power/%s_%d.csv' % (type,fileid)
    with open(filename, encoding='utf-8') as file:
        cnt = 0
        daycnt=-1
        titles = []
        datalist = []
        labels = []
        daydata=[]
        for line in file:
            if cnt < 1:
                titles = line.split(',')
            else:
                data = line.split(',')
                mstime = data[1].split('.')
                ctime = time.strptime(mstime[0], "%Y-%m-%d %H:%M:%S")
                if mstime.__len__() > 1:
                    ctime = time.localtime(time.mktime(ctime) + round(float(mstime[1]) / 1000))
                if (daycnt != ctime[2] and daycnt != -1 ):
                    #     day feature( mean std var peak ...)
                    tmp = np.array(daydata).astype(float)
                    mean = []
                    var = []
                    max = []
                    min = []
                    mean = []
                    var = []
                    max = []
                    min = []
                    mean.append(np.mean(tmp, 0))
                    max.append(np.max(tmp, 0))
                    # min.append(np.min(tmp, 0))
                    var.append(np.var(tmp, 0))
                    for j in range(daydata.__len__()):
                        tmpndata = daydata[j]
                        for i in range(5):
                            tmpndata.append(tmpndata[i + 5] - mean[0][i + 5])
                            # tmpndata.append(tmpndata[i + 5] / (max[0][i + 5]+2))
                            # tmpndata.append(min[0][i + 5])
                            tmpndata.append(var[0][i + 5])
                        datalist.append(tmpndata)
                    daydata = []

                ndata = []
                ndata.append(ctime[0])
                ndata.append(ctime[1])
                ndata.append(ctime[2])
                ndata.append(ctime[3])
                ndata.append(ctime[4])
                ndata.append(float(data[2]))
                # ndata.append(float(data[3]))
                ndata.append(float(data[4]))
                ndata.append(float(data[5]))
                ndata.append(float(data[6]))
                ndata.append(float(data[7]))
                ndata.append(float(data[2]) - 50 * pow(float(data[5]), 2))
                ndata.append(float(data[2]) - 50 * pow(float(data[7]), 2))
                daydata.append(ndata)
                daycnt = ctime[2]
                if yflag:
                    label = float(data[8])
                    labels.append(label)

            cnt += 1
        # 最后处理
        tmp = np.array(daydata).astype(float)
        mean = []
        var = []
        max = []
        min = []
        mean = []
        var = []
        max = []
        min = []
        mean.append(np.mean(tmp, 0))
        max.append(np.max(tmp, 0))
        # min.append(np.min(tmp, 0))
        var.append(np.var(tmp, 0))
        for j in range(daydata.__len__()):
            tmpndata = daydata[j]
            for i in range(5):
                tmpndata.append(tmpndata[i + 5] - mean[0][i + 5])
                # tmpndata.append(tmpndata[i + 5] / (max[0][i + 5] + 2))
                # tmpndata.append(min[0][i + 5])
                tmpndata.append(var[0][i + 5])
            datalist.append(tmpndata)
        return datalist,labels