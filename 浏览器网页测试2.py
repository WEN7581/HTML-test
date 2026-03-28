import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QDir

class SimpleBrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python浏览器")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 创建Web视图
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        
        # 获取当前目录路径
        current_dir = QDir.currentPath()
        
        # 创建HTML内容
        html_content = self.create_simple_html()
        
        # 设置基础URL为当前目录，以便加载本地资源
        base_url = QUrl.fromLocalFile(current_dir + "/")
        
        # 加载HTML内容
        self.web_view.setHtml(html_content, base_url)
    
    def create_simple_html(self):
        """创建简单的HTML内容"""
        return '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>浏览器网页测试 - 简化版</title>
<style>
    body {
        margin: 0;
        font-family: system-ui, -apple-system, sans-serif;
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #333;
    }
    main {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 40px;
        width: 90%;
        max-width: 700px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    }
    h1 { margin: 0 0 10px; font-size: 2em; }
    h1 a { color: #6a11cb; text-decoration: none; transition: 0.3s; }
    h1 a:hover { color: #4a00e0; }
    .description { color: #666; margin-bottom: 30px; line-height: 1.6; }
    .info-box {
        background: #f5f7fa;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 30px;
        text-align: left;
        border-left: 4px solid #6a11cb;
        font-size: 0.9em;
        color: #555;
    }
    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
    }
    .feature {
        background: #fff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .feature:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .feature:active { transform: scale(0.95); }
    .feature-icon { width: 40px; height: 40px; fill: #6a11cb; margin-bottom: 10px; }
    .feature-title { font-weight: bold; margin-bottom: 5px; }
    .feature-desc { font-size: 0.85em; color: #777; }
    footer { margin-top: 30px; font-size: 0.8em; color: #999; border-top: 1px solid #eee; padding-top: 15px; }
    @media (max-width: 600px) {
        main { padding: 20px; }
        .features { grid-template-columns: 1fr; }
    }
</style>
</head>
<body>
<main>
    <h1><a href="https://www.ekwing.com" target="_blank">浏览器网页测试</a></h1>
    <p class="description">欢迎使用现代化网页测试工具。本页面展示 HTML5 与 CSS3 的基础交互与响应式布局。</p>
    <div class="info-box">
        <strong>系统状态：</strong> 当前环境检测正常。您可以点击下方的功能卡片体验交互效果。
    </div>
    <div class="features">
        <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24"><path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M12,6A6,6 0 0,0 6,12A6,6 0 0,0 12,18A6,6 0 0,0 18,12A6,6 0 0,0 12,6M12,8A4,4 0 0,1 16,12A4,4 0 0,1 12,16A4,4 0 0,1 8,12A4,4 0 0,1 12,8Z"/></svg>
            <div class="feature-title">极速加载</div>
            <div class="feature-desc">优化代码结构<br>实现秒开体验</div>
        </div>
        <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24"><path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1Z"/></svg>
            <div class="feature-title">安全防护</div>
            <div class="feature-desc">数据加密传输<br>保障隐私安全</div>
        </div>
        <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24"><path d="M4,6H20V18H4V6M20,4A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4C2.89,20 2,19.1 2,18V6C2,4.89 2.89,4 4,4H20M11,10H13V14H11V10M11,16H13V18H11V16Z"/></svg>
            <div class="feature-title">多端适配</div>
            <div class="feature-desc">完美兼容手机<br>平板与电脑</div>
        </div>
    </div>
    <footer>
        &copy; 2026 浏览器网页测试2
    </footer>
</main>
</body>
</html>
'''
def main():
    app = QApplication(sys.argv)
    window = SimpleBrowserApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()