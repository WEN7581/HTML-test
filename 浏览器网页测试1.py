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
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>浏览器网页测试 - 完美修复版</title>
<style>
    :root {
        --primary-color: #6a11cb;
        --secondary-color: #2575fc;
        --text-main: #333333;
        --text-secondary: #666666;
        --card-bg: #ffffff;
    }
    body {
        font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', 'PingFang SC', 'Microsoft YaHei', sans-serif;
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        margin: 0;
        padding: 0;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: var(--text-main);
    }
    /* 使用语义化标签 main */
    main.container {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 24px;
        padding: 50px 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
        text-align: center;
        max-width: 700px;
        width: 90%;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        animation: fadeIn 0.8s ease-out;
    }
    h1 {
        margin: 0 0 15px 0;
        font-weight: 700;
        font-size: 2.5em;
        letter-spacing: -0.5px;
    }
    h1 a {
        color: var(--primary-color);
        text-decoration: none;
        background: linear-gradient(120deg, transparent 0%, transparent 60%, rgba(106, 17, 203, 0.2) 60%);
        background-size: 220% 100%;
        transition: all 0.3s ease-in-out;
        padding: 0 5px;
        border-radius: 4px;
    }
    h1 a:hover {
        background-position: 100% 0;
        color: #4a00e0;
    }
    .description {
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 40px;
        font-size: 1.1em;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }
    .info-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 40px;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
        text-align: left;
        border-left: 5px solid var(--primary-color);
    }
    .info-title {
        color: var(--primary-color);
        font-weight: 700;
        margin-bottom: 8px;
        font-size: 1.1em;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .info-content {
        color: #555555;
        font-size: 0.95em;
    }
    .features {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    .feature {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 25px 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        cursor: pointer;
        border: 1px solid rgba(0,0,0,0.03);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .feature:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(106, 17, 203, 0.15);
        border-color: rgba(106, 17, 203, 0.1);
    }
    .feature:active {
        transform: scale(0.95);
    }
    .feature-icon {
        font-size: 2.5em;
        margin-bottom: 15px;
        color: var(--primary-color);
        width: 50px;
        height: 50px;
        fill: currentColor;
    }
    .feature-title {
        font-weight: 600;
        color: var(--text-main);
        margin-bottom: 5px;
        font-size: 1.05em;
    }
    .feature-desc {
        color: var(--text-secondary);
        font-size: 0.85em;
        line-height: 1.4;
    }
    /* 使用语义化标签 footer */
    footer.footer {
        margin-top: 40px;
        color: #888888;
        font-size: 0.85em;
        border-top: 1px solid rgba(0,0,0,0.05);
        padding-top: 20px;
        width: 100%;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @media (max-width: 600px) {
        main.container {
            padding: 30px 20px;
            width: 95%;
        }
        h1 {
            font-size: 1.8em;
        }
        .description {
            font-size: 1em;
        }
        .features {
            grid-template-columns: 1fr;
        }
    }
</style>
</head>
<body>
<main class="container">
    <h1><a href="https://www.ekwing.com" target="_blank">浏览器网页测试</a></h1>
    <p class="description">
        欢迎使用现代化网页测试工具。本页面旨在展示 HTML5、CSS3 及 JavaScript 的基础交互能力与响应式布局设计。
    </p>
    <div class="info-box">
        <div class="info-title">
            <svg style="width:20px;height:20px" viewBox="0 0 24 24" aria-hidden="true">
                <path fill="currentColor" d="M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z" />
            </svg>
            系统状态
        </div>
        <div class="info-content">
            当前环境检测正常。所有样式表与脚本均已成功加载。您可以点击下方的功能卡片体验微交互效果。
        </div>
    </div>
    <div class="features">
        <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M12,6A6,6 0 0,0 6,12A6,6 0 0,0 12,18A6,6 0 0,0 18,12A6,6 0 0,0 12,6M12,8A4,4 0 0,1 16,12A4,4 0 0,1 12,16A4,4 0 0,1 8,12A4,4 0 0,1 12,8Z" />
            </svg>
            <div class="feature-title">极速加载</div>
            <div class="feature-desc">优化代码结构<br>实现秒开体验</div>
        </div>
        <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1Z" />
            </svg>
            <div class="feature-title">安全防护</div>
            <div class="feature-desc">数据加密传输<br>保障隐私安全</div>
        </div>
        <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M4,6H20V18H4V6M20,4A2,2 0 0,1 22,6V18A2,2 0 0,1 20,20H4C2.89,20 2,19.1 2,18V6C2,4.89 2.89,4 4,4H20M11,10H13V14H11V10M11,16H13V18H11V16Z" />
            </svg>
            <div class="feature-title">多端适配</div>
            <div class="feature-desc">完美兼容手机<br>平板与电脑</div>
        </div>
    </div>
    <footer class="footer">
        &copy; 2026 浏览器网页测试1 
    </footer>
</main>
<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('页面加载完成，DOM已就绪。');
    const features = document.querySelectorAll('.feature');
    features.forEach(feature => {
        feature.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                return; 
            }
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
});
</script>
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