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
<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>浏览器网页测试</title>
<style>
    body {
        font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 0;
        padding: 0;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: #333;
    }
    .container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        text-align: center;
        max-width: 600px;
        width: 90%;
        backdrop-filter: blur(10px);
    }
    h1 {
        color: #667eea;
        margin-bottom: 20px;
        font-weight: 300;
        font-size: 2.5em;
    }
    .description {
        color: #666;
        line-height: 1.6;
        margin-bottom: 30px;
        font-size: 1.1em;
    }
    .info-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    .info-title {
        color: #667eea;
        font-weight: 600;
        margin-bottom: 10px;
        font-size: 1.2em;
    }
    .info-content {
        color: #555;
        font-size: 1em;
    }
    .features {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
    }
    .feature {
        background: white;
        border-radius: 10px;
        padding: 20px;
        width: 150px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        cursor: pointer; 
    }
    .feature:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    .feature-icon {
        font-size: 2.5em;
        margin-bottom: 10px;
        color: #667eea;
    }
    .feature-title {
        font-weight: 600;
        color: #444;
        margin-bottom: 5px;
    }
    .feature-desc {
        color: #666;
        font-size: 0.9em;
    }
    .text-link {
        color: #667eea;
        text-decoration: none;
        transition: color 0.2s;
    }
    .text-link:hover {
        text-decoration: underline;
        color: #5a6fd6;
    }
    .footer {
        margin-top: 30px;
        color: #888;
        font-size: 0.9em;
    }
    @media (max-width: 600px) {
        .container {
            padding: 20px;
        }
        h1 {
            font-size: 2em;
        }
        .features {
            flex-direction: column;
            align-items: center;
        }
    }
</style>
</head>
<body>
<div class="container"><h1><a href="https://www.ekwing.com" class="text-link">浏览器网页测试</a></h1></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
    console.log('页面加载完成');
    const features = document.querySelectorAll('.feature');
    features.forEach(feature => {
        feature.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                return; 
            }
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 200);
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