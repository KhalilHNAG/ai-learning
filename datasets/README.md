# datasets · 数据说明

本目录存放练习用数据。网络受这台机器 TLS 问题影响,样本全部打包在仓库里,离线可用。

| 文件 | 说明 | 对应练习 |
|---|---|---|
| `titanic-sample.csv` | 200 行泰坦尼克样本,与 Kaggle `train.csv` 同结构(合成数据,含少量缺失值) | Day 7 / Day 14 |
| `retail-orders.csv` | 500 行模拟零售订单(订单、日期、客户、城市、类别、金额) | Day 13 |
| `day05-students.csv` | Day 5 练习运行时自动生成,已被 git 忽略 | Day 5 |

想换成真实数据:下载 Kaggle Titanic `train.csv`,保持同名列后直接替换 `titanic-sample.csv` 即可(换成完整 891 行也无需改代码)。
