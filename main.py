from typing import List, Tuple, Any
from botpy.message import Message
from core.plugin import Plugin, handler
from core.plugin import PluginMetadata
from core import bot

class KeywordReplyPlugin(Plugin):
    # 插件元数据
    metadata = PluginMetadata(
        name='keyword_reply',
        description='关键词自动回复插件',
        usage='发送关键词即可触发回复',
        version='1.0.0',
        author='YourName'
    )

    # 关键词回复字典
    keyword_replies = {
        "地图密码": "零号大坝: 0229\n长弓溪谷: 0252\n巴克什: 2514\n航天基地: 2767",
        "特勤处推荐": "ACOG精准六倍镜 - 晚上11点\n4.6x30mm AP SX - 凌晨5点\n战地医疗箱 - 上午6点\n精英防弹背心 - 上午6点",
        "高价材料": "移动电缆 - 最佳买入:凌晨1点\n聚乙烯纤维 - 最佳买入:上午6点\n盒装挂耳咖啡 - 最佳买入:凌晨5点\n特种钢 - 最佳买入:上午6点",
        "帮助": "可用命令:\n- 地图密码\n- 特勤处推荐\n- 高价材料"
    }

    def __init__(self):
        super().__init__()

    @handler.on_message()
    async def handle_message(self, message: Message):
        # 获取消息内容
        content = message.content
        
        # 检查是否匹配关键词
        for keyword, reply in self.keyword_replies.items():
            if keyword in content:
                # 发送回复
                await bot.api.post_message(
                    channel_id=message.channel_id,
                    content=reply
                )
                return

    # 插件被加载时的处理
    async def on_loaded(self):
        print(f"[{self.metadata.name}] 插件已加载!")

    # 插件被卸载时的处理
    async def on_unloaded(self):
        print(f"[{self.metadata.name}] 插件已卸载!") 
