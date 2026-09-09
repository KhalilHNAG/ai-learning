# AI 学习 · 交接文档(给 ChatGPT 的完整背景)

> 用途:把在 DeepSeek Harness(DSH)里进行中的 AI 系统学习,完整交接给 ChatGPT 继续当 AI 老师。
> 使用方法:把本文件**全文**粘贴到 ChatGPT 的新对话作为第一条消息即可。

---

## 一、我是谁 / 我的目标

- 我是一名准备**考研**的学生,考研初试约在 **2027 年 12 月**(备考期长)。
- 我的目标是:**系统地学习 AI,为研究生阶段的 AI 学习与项目研究打基础**。
- 已初步入门 Python(语法会,但还没到"能用它干活"的程度)。

## 二、我的时间与节奏(必须遵守)

- 每天:**考研数学约 2 小时(主阵地)+ AI 学习约 1 小时 + 英语碎片 10~15 分钟**。
- AI 这 1 小时的模板:
  - 40 分钟:看课 + 记笔记(或做练习本)
  - 15 分钟:动手改代码、跑实验
  - 5 分钟:回看/自检
- 考前最后 2~3 个月切"保底模式"(每周 3 天),AI 让位给考研冲刺。
- 考研数学的线代/概率与 AI 地基重叠,可互相利用(矩阵乘法=前向传播、最大似然=交叉熵……)。

## 三、我的学习路线(已定稿)

**阶段 A(考前,约 10 个月,到考前 2~3 个月):**
- W1-2:工具与数据科学生态(NumPy → Pandas → Matplotlib + 环境)
- W3-24(约 5 个月):**吴恩达《Machine Learning Specialization》完整主线**(编程作业 + 评估思维);卡壳查李宏毅(B站)/3Blue1Brown
- W25-36(约 3 个月):考前预热 **PyTorch + CIFAR-10 CNN 项目**
- 考前最后 2~3 个月:保底模式

**阶段 B(考后,研一前):**深度学习深化 → 大模型 / Transformer → 论文复现(ResNet → Transformer → BERT → GPT),对接研究生课题。

## 四、已完成进度(Day 1~4)

| 天 | 日期 | 内容 | 状态 |
|---|---|---|---|
| Day 1 | 2026-08-19 | 环境搭建(Miniconda+JupyterLab+numpy/pandas/matplotlib)、首个 notebook、git 首次提交、项目迁入 D:\01_Study | ✅ |
| Day 2 | 2026-09-01 | NumPy 基础:创建/属性/形状/广播复习 + 小挑战;第一次独立走通命令行 git 收盘 | ✅ |
| Day 3 | 2026-09-05 | NumPy 进阶:索引切片/布尔掩码/聚合 axis/矩阵乘法;**发现并修正了 argmax 0 起始索引 bug** | ✅ |
| Day 4 | 2026-09-08 | NumPy 实战:模拟数据 + 统计(seed/统计量/相关性/可视化/标准化) | ✅ |

练习文件:`练习/day01-start.ipynb`、`练习/day02-numpy-basics.ipynb`、`练习/day03-numpy-advanced.ipynb`、`练习/day04-numpy-stats.ipynb`
学习日志:`学习日志/2026-08-19.md`、`学习日志/2026-09-01.md`、`学习日志/2026-09-05.md`、`学习日志/2026-09-08.md`

**W1-2 路线图**(已存入 `练习/README.md`,Day 5~14 练习本已全部生成并自测通过):W1 Day 5~7 = Pandas 基础/进阶 + Titanic 第一轮 EDA;W2 Day 8~14 = Matplotlib/可视化/清洗/重塑/时间序列/零售 EDA/完整 EDA 工作流。

## 五、我的机器环境(重要,别乱动!)

- **Python**:Miniconda 3(`C:\Users\Enhance\miniconda3`,conda 26.5.3,自带 Python 3.14.6);短命令 `python` 在普通终端已指到它(用户 PATH 里 Miniconda 在 WindowsApps 之前),但 Codex 执行环境的 PATH 前缀不同,可能解析到 WindowsApps 占位符——脚本里建议用完整路径 `C:\Users\Enhance\miniconda3\python.exe`。
- **库**:numpy 2.5.2 / pandas 3.0.5 / matplotlib 3.11.1 / JupyterLab 4.6.3(清华源安装)。
- **JupyterLab**:根目录 `D:\01_Study`,地址 `http://127.0.0.1:8888/lab`。默认启动会带 token(用 `--ServerApp.token=""` 可关闭);启动命令:`python -m jupyter lab --no-browser --notebook-dir="D:\01_Study"`。
- **git**:仓库 `D:\01_Study\ai-learning` → GitHub `https://github.com/KhalilHNAG/ai-learning`(用户名 KhalilHNAG,提交身份用隐私邮箱 `KhalilHNAG@users.noreply.github.com`)。
- **这台机器的已知坑(重要!)**:
  1. Windows **schannel TLS 凭据层损坏**:所有 HTTPS 工具(curl/git 默认后端)报 `SEC_E_NO_CREDENTIALS`。解法:git 已全局切 `sslBackend=openssl`;下载/装包走清华镜像(HTTP 或 Python OpenSSL 均可)。
  2. 外网需要 v2rayN,**10808 是 SOCKS 端口不是 HTTP 代理**(pip 不能直接当 HTTP 代理用)。
  3. PowerShell 是 **5.1,不支持 `&&`**——命令分隔用 `;`。
  4. 打印中文/emoji 需 UTF-8:`sys.stdout.reconfigure(encoding="utf-8")`。

## 六、我们的协作约定(请 ChatGPT 继续遵守)

1. 每次学习结束,我说"生成日志"时,把当天内容整理成 `学习日志/YYYY-MM-DD.md`(模板见该目录 README),commit 并 push。
2. 每天的收盘动作(可在本地执行):`cd D:\01_Study\ai-learning && git add -A; git commit -m "dayN: ..."; git push`(push 前要开 v2rayN)。
3. 每晚可以提前生成第二天的练习本(`练习/dayXX-*.ipynb`),先自测跑通再给我。
4. 我卡住时会把报错原文贴出来,请先解释"为什么错"再给修复。
5. 鼓励我动手、抓 bug;我是来学方法的,不是来要答案的。

## 七、下一步(给 ChatGPT 的第一个任务)

请先回复:
1. 确认你已读完背景,并用一两句话告诉我你理解的我的当前状态;
2. 如果今天是 **Day 5**,生成 `练习/day05-pandas-basics.ipynb`(Pandas 基础:Series/DataFrame、读写 CSV、缺失值),并先自测跑通;
3. 告诉我今天 1 小时的具体安排。

> 若需要练习本模板,参考现有 day01~day04 的格式(markdown 引导 + code + 自检清单 + 收盘动作)。
