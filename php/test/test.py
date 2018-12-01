import numpy as np  # numpy库
import pandas as pd  # 导入pandas
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor  # 集成算法
from sklearn.linear_model import ElasticNet  # 批量导入要实现的回归算法
from sklearn.metrics import mean_absolute_error  # 批量导入指标算法
from sklearn.model_selection import cross_val_score  # 交叉检验
from sklearn.svm import SVR  # SVM中的回归算法

from pvi.check.dataReader import getData, composeData, writePredictData, getFullData


# 数据准备
# raw_data = np.loadtxt('regression.txt')  # 读取数据文件
# X = raw_data[:, :-1]  # 分割自变量
# y = raw_data[:, -1]  # 分割因变量
def predict(fileid):
    X,y=getFullData(fileid)
    out=getData(fileid,'test',False)
    # 训练回归模型
    n_folds = 10  # 设置交叉检验的次数
    # model_br = BayesianRidge()  # 建立贝叶斯岭回归模型对象
    # model_lr = LinearRegression()  # 建立普通线性回归模型对象
    model_etc = ElasticNet()  # 建立弹性网络回归模型对象
    model_svr = SVR()  # 建立支持向量机回归模型对象
    model_gbr = GradientBoostingRegressor(learning_rate=0.01,n_estimators=500,criterion='mae')  # 建立梯度增强回归模型对象
    model_rf=RandomForestRegressor(n_estimators=500,max_depth=500,criterion='mae')
    # model_names = ['BayesianRidge',  'ElasticNet', 'SVR', 'GBR','RFR']  # 不同模型的名称列表
    model_names = ['ElasticNet', 'SVR', 'GBR','RFR']  # 不同模型的名称列表
    # model_dic = [model_br,  , model_svr, model_gbr,model_rf]  # 不同回归模型对象的集合
    model_dic = [model_etc,  model_svr, model_gbr,model_rf]  # 不同回归模型对象的集合
    cv_score_list = []  # 交叉检验结果列表
    pre_y_list = []  # 各个回归模型预测的y值列表
    for model in model_dic:  # 读出每个回归模型对象
        scores = cross_val_score(model, X, y, cv=n_folds)  # 将每个回归模型导入交叉检验模型中做训练检验
        cv_score_list.append(scores)  # 将交叉检验结果存入结果列表
        pre_y_list.append(model.fit(X, y).predict(X))  # 将回归训练中得到的预测y存入列表
    # 模型效果指标评估
    n_samples, n_features = X.shape  # 总样本量,总特征数
    model_metrics_name = [ mean_absolute_error]  # 回归评估指标对象集
    model_metrics_list = []  # 回归评估指标列表
    for i in range(4):  # 循环每个模型索引
        tmp_list = []  # 每个内循环的临时结果列表
        for m in model_metrics_name:  # 循环每个指标对象
            tmp_score = m(y, pre_y_list[i])  # 计算每个回归指标结果
            tmp_list.append(tmp_score)  # 将结果存入每个内循环的临时结果列表
        model_metrics_list.append(tmp_list)  # 将结果存入回归评估指标列表
    df1 = pd.DataFrame(cv_score_list, index=model_names)  # 建立交叉检验的数据框
    df2 = pd.DataFrame(model_metrics_list, index=model_names, columns=[ 'mae'])  # 建立回归指标的数据框
    print ('samples: %d \t features: %d' % (n_samples, n_features))  # 打印输出样本量和特征数量
    print (70 * '-')  # 打印分隔线
    print ('cross validation result:')  # 打印输出标题
    print (df1)  # 打印输出交叉检验的数据框
    print (70 * '-')  # 打印分隔线
    print ('regression metrics:')  # 打印输出标题
    print (df2)  # 打印输出回归指标的数据框
    print (70 * '-')  # 打印分隔线
    print ('short name \t full name')  # 打印输出缩写和全名标题
    print ('ev \t explained_variance')
    print ('mae \t mean_absolute_error')
    print ('mse \t mean_squared_error')
    print ('r2 \t r2')
    print (70 * '-')  # 打印分隔线
    # 模型效果可视化
    # plt.figure()  # 创建画布
    # plt.plot(np.arange(X.shape[0]), y, color='k', label='true y')  # 画出原始值的曲线
    # color_list = ['r', 'b', 'g', 'y', 'c','p']  # 颜色列表
    # linestyle_list = ['-', '.', 'o', 'v', '*','+']  # 样式列表
    # for i, pre_y in enumerate(pre_y_list):  # 读出通过回归模型预测得到的索引及结果
    #     try:
    #       plt.plot(np.arange(X.shape[0]), pre_y_list[i], color_list[i], label=model_names[i])  # 画出每条预测结果线
    #     except:
    #         print(i)
    # plt.title('regression result comparison')  # 标题
    # plt.legend(loc='upper right')  # 图例位置
    # plt.ylabel('real and predicted value')  # y轴标题
    # plt.show()

    # 预测
    outlist=[]
    for model in model_dic:  # 读出每个回归模型对象
        outlist.append(model.fit(X, y).predict(out))
    ensamble=np.mean(np.array(outlist),0)

    writePredictData(ensamble,fileid)

for i in range(5):
   predict(i+1)
composeData()