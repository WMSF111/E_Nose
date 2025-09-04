import sys
sys.path.insert(0, sys.path[0]+"/../")
import time
import traceback
from collections import defaultdict
from datetime import date, datetime, timedelta
from itertools import cycle

import constants
import requests

# import requests_cache
from PySide6.QtCore import (
    QObject,
    QRunnable,
    Qt,
    QThreadPool,
    Signal,
    Slot,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QStandardItem,
    QStandardItemModel,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QMainWindow,
    QProgressBar,
    QTableView,
    QToolBar,
    QWidget,
)
# 创建颜色循环器，用于为不同的货币分配颜色
color_cycle = cycle(constants.BREWER12PAIRED)
# requests_cache.install_cache("cache")

# PyQtGraph must be imported after Qt.
import pyqtgraph as pg
# 设置 PyQtGraph 的背景和前景颜色
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")


DATE_REQUEST_OFFSETS = [0] # 初始化日期偏移量列表，初始值为0, 从当前日期开始。
current = [(0, constants.HISTORIC_DAYS_N)] # 初始化一个队列，表示从0天到 HISTORIC_DAYS_N 天的范围
while current: # 当队列不为空时，继续循环
    a, b = current.pop(0) # 从队列中取出一个元组 (a, b)
    n = (a + b) // 2
    DATE_REQUEST_OFFSETS.append(n) # 将中间值 n 添加到日期偏移量列表中

    if abs(a - n) > 1:
        current.insert(0, (a, n))

    if abs(b - n) > 1:
        current.append((b, n))

# 定义 WorkerSignals 类，用于定义工作线程可用的信号
class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    finished = Signal()  # 完成信号
    error = Signal(tuple)  # 错误信号
    progress = Signal(int)  # 进度信号
    data = Signal(int, dict)  # 数据信号
    cancel = Signal()  # 取消信号

# 定义 UpdateWorker 类，用于更新数据的工作线程
class UpdateWorker(QRunnable):
    """
    Worker thread for updating currency.
    """

    signals = WorkerSignals()  # 初始化信号，用于在多线程中传递数据和状态
    is_interrupted = False  # 是否被中断的标志，用于控制线程的中断

    def __init__(self, base_currency):
        super().__init__()  # 调用父类的构造函数
        self.base_currency = base_currency  # 设置基础货币
        self.signals.cancel.connect(self.cancel)  # 将取消信号连接到取消方法

    @Slot()
    def run(self):
        """
        线程的运行逻辑。
        """
        try:
            today = date.today()  # 获取当前日期
            total_requests = len(DATE_REQUEST_OFFSETS)  # 总请求数量，根据日期偏移量列表的长度确定
            # 遍历日期偏移量列表，发送请求并处理数据
            for n, offset in enumerate(DATE_REQUEST_OFFSETS, 1):  # 计算日期
                when = today - timedelta(days=offset)  # 计算偏移后的日期
                url = "http://api.fixer.io/{}".format(when.isoformat())  # 构造请求的URL
                r = requests.get(url, params={"base": self.base_currency})  # 发送请求
                r.raise_for_status()  # 检查请求是否成功
                data = r.json()  # 解析返回的JSON数据
                rates = data["rates"]  # 获取汇率数据
                rates[self.base_currency] = 1.0  # 将基础货币的汇率设置为1.0

                self.signals.data.emit(offset, rates)  # 发射数据信号，传递偏移量和汇率数据
                self.signals.progress.emit(int(100 * n / total_requests))  # 发射进度信号，计算并传递当前进度

                if not r.from_cache:  # 如果请求不是来自缓存
                    time.sleep(1)  # 等待1秒，避免过于频繁地发送请求

                if self.is_interrupted:  # 如果线程被中断
                    break  # 跳出循环

        except Exception as e:  # 捕获异常
            print(e)  # 打印异常信息
            exctype, value = sys.exc_info()[:2]  # 获取异常类型和值
            self.signals.error.emit((exctype, value, traceback.format_exc()))  # 发射错误信号，传递异常信息
            return  # 退出线程

        self.signals.finished.emit()  # 发射完成信号，表示线程运行结束

    def cancel(self):
        """
        取消线程的运行。
        """
        self.is_interrupted = True  # 设置中断标志为True