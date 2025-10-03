import sys
import time
from enum import Enum
from typing import Optional, Callable
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    # 如果colorama不可用，创建空的颜色类
    class Fore:
        RED = YELLOW = GREEN = BLUE = MAGENTA = CYAN = WHITE = ''
    class Style:
        BRIGHT = NORMAL = ''

class ProgressStyle(Enum):
    BASIC = "basic"
    COLORFUL = "colorful"
    BLOCK = "block"
    ARROW = "arrow"
    SPINNER = "spinner"
    PERCENTAGE = "percentage"

class ProgressBar:
    def __init__(self, 
                 total: int = 100,
                 style: ProgressStyle = ProgressStyle.BASIC,
                 desc: str = "Progress",
                 length: int = 50,
                 color_enabled: bool = True):
        """
        初始化进度条
        
        Args:
            total: 总进度值（默认为100）
            style: 进度条样式
            desc: 进度条描述
            length: 进度条长度（字符数）
            color_enabled: 是否启用颜色
        """
        self.total = total
        self.style = style
        self.desc = desc
        self.length = length
        self.color_enabled = color_enabled
        self.current = 0
        self.start_time = None
        self.spinner_chars = ['|', '/', '-', '\\']
        self.spinner_index = 0
        
    def start(self):
        """开始进度条"""
        self.start_time = time.time()
        self.current = 0
        self._render()
        
    def update(self, value: int):
        """
        直接更新进度值
        
        Args:
            value: 进度值（0-100）
        """
        if value < 0 or value > self.total:
            raise ValueError(f"进度值必须在0-{self.total}之间")
        
        self.current = value
        self._render()
        
    def increment(self, value: int = 1):
        self.update(min(self.current + value, self.total))
        
    def finish(self):
        self.update(self.total)
        print()  # 换行
        
    def _render(self):
        percentage = (self.current / self.total) * 100
        filled_length = int(self.length * self.current // self.total)
        
        # 计算已用时间和预估剩余时间
        elapsed_time = time.time() - self.start_time if self.start_time else 0
        if self.current > 0:
            eta = (elapsed_time / self.current) * (self.total - self.current)
        else:
            eta = 0
            
        if self.style == ProgressStyle.BASIC:
            bar = self._create_basic_bar(filled_length, percentage)
        elif self.style == ProgressStyle.COLORFUL:
            bar = self._create_colorful_bar(filled_length, percentage)
        elif self.style == ProgressStyle.BLOCK:
            bar = self._create_block_bar(filled_length, percentage)
        elif self.style == ProgressStyle.ARROW:
            bar = self._create_arrow_bar(filled_length, percentage)
        elif self.style == ProgressStyle.SPINNER:
            bar = self._create_spinner_bar(filled_length, percentage)
        elif self.style == ProgressStyle.PERCENTAGE:
            bar = self._create_percentage_bar(filled_length, percentage)
        else:
            bar = self._create_basic_bar(filled_length, percentage)
            
        time_info = f" [{elapsed_time:.1f}s<{eta:.1f}s]"
        bar += time_info
        
        sys.stdout.write('\r' + bar)
        sys.stdout.flush()
        
    def _create_basic_bar(self, filled_length: int, percentage: float) -> str:
        bar = '█' * filled_length + '░' * (self.length - filled_length)
        return f"{self.desc}: |{bar}| {percentage:.1f}%"
    
    def _create_colorful_bar(self, filled_length: int, percentage: float) -> str:
        if percentage < 33:
            color = Fore.RED
        elif percentage < 66:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN
            
        bar = '█' * filled_length + '░' * (self.length - filled_length)
        if self.color_enabled:
            bar = color + bar + Style.RESET_ALL
            
        return f"{self.desc}: |{bar}| {color}{percentage:.1f}%{Style.RESET_ALL}"
    
    def _create_block_bar(self, filled_length: int, percentage: float) -> str:
        bar = '■' * filled_length + '□' * (self.length - filled_length)
        return f"{self.desc}: {bar} {percentage:.1f}%"
    
    def _create_arrow_bar(self, filled_length: int, percentage: float) -> str:
        bar = '>' * filled_length + '-' * (self.length - filled_length)
        return f"{self.desc}: [{bar}] {percentage:.1f}%"
    
    def _create_spinner_bar(self, filled_length: int, percentage: float) -> str:
        spinner = self.spinner_chars[self.spinner_index]
        self.spinner_index = (self.spinner_index + 1) % len(self.spinner_chars)
        
        bar = '█' * filled_length + '░' * (self.length - filled_length)
        return f"{self.desc}: {spinner} |{bar}| {percentage:.1f}%"
    
    def _create_percentage_bar(self, filled_length: int, percentage: float) -> str:
        return f"{self.desc}: {percentage:.1f}% Complete"

# 工厂函数，便于创建不同类型的进度条
def create_progress_bar(style: str = "basic", **kwargs) -> ProgressBar:
    """
    创建进度条的工厂函数
    
    Args:
        style: 进度条样式（basic, colorful, block, arrow, spinner, percentage）
        **kwargs: 传递给ProgressBar的额外参数
    """
    style_map = {
        "basic": ProgressStyle.BASIC,
        "colorful": ProgressStyle.COLORFUL,
        "block": ProgressStyle.BLOCK,
        "arrow": ProgressStyle.ARROW,
        "spinner": ProgressStyle.SPINNER,
        "percentage": ProgressStyle.PERCENTAGE
    }
    
    progress_style = style_map.get(style.lower(), ProgressStyle.BASIC)
    return ProgressBar(style=progress_style, **kwargs)

# 使用示例
def demo_progress_bars():
    print("=== 进度条演示 ===\n")
    
    # 测试所有样式
    styles = ["basic", "colorful", "block", "arrow", "spinner", "percentage"]
    
    for style_name in styles:
        print(f"\n{style_name.upper()} 样式:")
        bar = create_progress_bar(style=style_name, desc=f"{style_name}测试", length=30)
        bar.start()
        
        # 进度更新
        for progress in [0, 25, 50, 75, 100]:
            bar.update(progress)
            time.sleep(0.5)
        
        bar.finish()

if __name__ == "__main__":
    demo_progress_bars()
