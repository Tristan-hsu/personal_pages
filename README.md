---
title: Tristan Hsu – Personal Page
emoji: 🏠
colorFrom: indigo
colorTo: purple
sdk: docker  
pinned: false
license: mit
---

# 許銘軒 - 個人作品集網站

這是一個專業的個人作品集網站，展示 AI 工程師許銘軒的技能、經驗和專案。

## 🌟 功能特色

- **雙語支援**：完整的中英文切換功能
- **響應式設計**：適配各種設備和螢幕尺寸
- **GitHub 整合**：自動獲取並展示 GitHub 專案
- **聯絡表單**：訪客可以直接發送訊息
- **深色主題**：現代化的專業外觀
- **動態效果**：流暢的滾動和動畫效果

## 🚀 技術架構

### 後端
- **Flask** - Python Web 框架
- **SQLAlchemy** - 資料庫 ORM
- **Flask-WTF** - 表單處理和驗證
- **Gunicorn** - WSGI 伺服器

### 前端
- **Bootstrap 5** - CSS 框架
- **Vanilla JavaScript** - 前端互動
- **Font Awesome** - 圖示庫
- **自訂 CSS** - 客製化樣式

### 資料庫
- **SQLite** (開發環境)
- **PostgreSQL** (生產環境)

## 📱 主要區塊

1. **關於我** - 個人簡介和背景
2. **工作經驗** - 專業經歷時間線
3. **教育背景** - 學歷資訊
4. **技術技能** - 專業技能展示
5. **專案作品** - 精選專案展示
6. **證照認證** - 專業證照
7. **GitHub 專案** - 實時獲取的 GitHub 資料
8. **聯絡我** - 聯絡表單和資訊

## 🛠️ 本機開發

### 環境需求
- Python 3.8+
- pip 套件管理器

### 安裝步驟

1. 複製專案
```bash
git clone https://github.com/Tristan-hsu/personal_pages.git
cd personal_pages
```

2. 建立虛擬環境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

3. 安裝依賴
```bash
pip install -r requirements.txt
```

4. 設定環境變數
```bash
export SESSION_SECRET="your-secret-key-here"
export GITHUB_TOKEN="your-github-token-here"  # 選擇性
```

5. 啟動應用
```bash
python main.py
```

應用將在 `http://localhost:5000` 啟動。

## 🌐 部署

### Replit 部署
1. 在 Replit 中開啟專案
2. 設定環境變數 (Secrets)
3. 點擊部署按鈕

### Heroku 部署
1. 建立 Heroku 應用
2. 設定環境變數
3. 推送代碼到 Heroku

### Vercel 部署
1. 連接 GitHub 儲存庫
2. 設定環境變數
3. 自動部署

## 🔧 設定說明

### 必要環境變數
- `SESSION_SECRET`: Flask 會話密鑰

### 選擇性環境變數
- `GITHUB_TOKEN`: GitHub API 令牌（提高 API 請求限制）
- `DATABASE_URL`: 資料庫連接字串（預設使用 SQLite）

### GitHub Token 設定
1. 前往 GitHub Settings → Developer settings → Personal access tokens
2. 建立新的 Classic token
3. 選擇 `public_repo` 權限
4. 複製令牌到環境變數

## 📝 內容管理

所有網站內容都在 `translations.py` 檔案中管理，包括：
- 界面文字翻譯
- 個人資料
- 工作經驗
- 教育背景
- 技能列表
- 專案描述
- 證照資訊

修改這個檔案即可更新網站內容。

## 🎨 自訂化

### 修改樣式
- 主要樣式：`static/css/style.css`
- Bootstrap 主題：使用 Replit 深色主題

### 修改內容
- 文字內容：`translations.py`
- 靜態檔案：`static/` 目錄

### 新增功能
- 路由邏輯：`routes.py`
- 資料模型：`models.py`
- 表單處理：`forms.py`

## 📞 聯絡資訊

- **姓名**: 許銘軒 (Ming-Hsuan Hsu)
- **職位**: AI 工程師 & 資料科學家
- **電子郵件**: minghsuanhsu.workspace@gmail.com
- **電話**: 0972-143-390
- **GitHub**: [Tristan-hsu](https://github.com/Tristan-hsu)

## 📄 授權

此專案僅供個人作品集使用。

---

*建立於 2025 年 - 使用 ❤️ 和 Python Flask 製作*