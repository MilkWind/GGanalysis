import GGanalysis.games.genshin_impact as GI
from GGanalysis.gacha_plot import QuantileFunction
import matplotlib.cm as cm
import numpy as np
import time

'''
注意若出现找不到字体的情况
Windows 下检查 C:/Windows/Fonts/ 下是否有以 SourceHanSansSC 开头的otf字体
Linux 下检查 ~/.local/share/fonts/ 下是否有以 SourceHanSansSC 开头的otf字体
如果没有安装字体，请下载并安装字体包 https://github.com/adobe-fonts/source-han-sans/releases/download/2.004R/SourceHanSansSC.zip
如果安装后还是找不到字体，请检查 GGanalysis/gacha_plot.py 内对字体路径的定义，自行修改为你的字体文件所在的位置
'''

# 以原神为例，演示绘制分位函数

# 定义获取物品个数的别名
def gi_character(x):
    return str(x-1)+'命'
def gi_weapon(x):
    return str(x)+'精'

# 原神UP五星角色
GI_fig = QuantileFunction(
        GI.up_5star_character(item_num=7, multi_dist=True),
        title='原神UP五星角色抽取概率',
        item_name='UP五星角色',
        text_head='采用www.bilibili.com/read/cv10468091模型\n本算例中UP物品均不在常驻祈愿中',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=1300,
        mark_func=gi_character,
        is_finite=True)
GI_fig.show_figure(dpi=300, savefig=True)

# 原神特定UP四星角色
GI_fig = QuantileFunction(
        GI.up_4star_specific_character(item_num=7, multi_dist=True),
        title='原神特定UP四星角色抽取概率',
        item_name='特定UP四星',
        text_head='采用www.bilibili.com/read/cv10468091模型\n本算例中UP物品均不在常驻祈愿中\n绘图曲线忽略五星与四星耦合情况',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=600,
        mark_func=gi_character,
        line_colors=cm.Purples(np.linspace(0.5, 0.9, 7+1)),
        is_finite=False)
GI_fig.show_figure(dpi=300, savefig=True)

# 原神定轨UP五星武器
GI_fig = QuantileFunction(
        GI.up_5star_ep_weapon(item_num=5, multi_dist=True),
        title='原神定轨UP五星武器抽取概率',
        item_name='定轨五星武器',
        text_head='采用www.bilibili.com/read/cv10468091模型\n本算例中UP物品均不在常驻祈愿中',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=1200,
        mark_func=gi_weapon,
        line_colors=cm.Reds(np.linspace(0.5, 0.9, 5+1)),
        is_finite=True)
GI_fig.show_figure(dpi=300, savefig=True)

# 原神不定轨UP五星武器
GI_fig = QuantileFunction(
        GI.up_5star_specific_weapon(item_num=5, multi_dist=True),
        title='原神不定轨特定UP五星武器抽取概率',
        item_name='特定五星武器',
        text_head='采用www.bilibili.com/read/cv10468091模型\n本算例中UP物品均不在常驻祈愿中',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=1600,
        y2x_base=1.6,
        mark_func=gi_weapon,
        line_colors=(cm.Greys(np.linspace(0.5, 0.9, 5+1))+cm.Reds(np.linspace(0.5, 0.9, 5+1)))/2,
        is_finite=False)
GI_fig.show_figure(dpi=300, savefig=True)

# 原神特定UP四星武器
GI_fig = QuantileFunction(
        GI.up_4star_specific_weapon(item_num=5, multi_dist=True),
        title='原神特定UP四星武器抽取概率',
        item_name='特定UP四星',
        text_head='采用www.bilibili.com/read/cv10468091模型\n本算例中UP物品均不在常驻祈愿中\n绘图曲线忽略五星与四星耦合情况',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=600,
        mark_func=gi_weapon,
        line_colors=cm.Oranges(np.linspace(0.5, 0.9, 5+1)),
        is_finite=False)
GI_fig.show_figure(dpi=300, savefig=True)