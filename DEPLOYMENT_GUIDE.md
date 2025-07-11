# 部署指南 - 許銘軒個人作品集網站

## 🚀 部署選項

### 1. Replit 部署 (推薦)
最簡單快速的部署方式。

**步驟：**
1. 確保所有環境變數已設定：
   - `SESSION_SECRET`: 已設定
   - `GITHUB_TOKEN`: 已設定
2. 點擊 Replit 右上角的 "Deploy" 按鈕
3. 選擇部署類型
4. 等待部署完成

**優點：**
- 零配置部署
- 自動 SSL 證書
- 內建監控和日誌
- 支援自訂域名

### 2. Heroku 部署

**前置準備：**
```bash
# 安裝 Heroku CLI
# 登入 Heroku 帳戶
heroku login
```

**部署步驟：**
```bash
# 建立 Heroku 應用
heroku create your-portfolio-name

# 設定環境變數
heroku config:set SESSION_SECRET="your-secret-key-here"
heroku config:set GITHUB_TOKEN="your-github-token-here"

# 部署應用
git push heroku main

# 開啟應用
heroku open
```

### 3. Vercel 部署

**步驟：**
1. 將專案推送到 GitHub
2. 前往 [Vercel Dashboard](https://vercel.com/dashboard)
3. 點擊 "New Project"
4. 選擇您的 GitHub 儲存庫
5. 設定環境變數
6. 部署完成

**環境變數設定：**
- `SESSION_SECRET`: 您的會話密鑰
- `GITHUB_TOKEN`: 您的 GitHub 令牌

### 4. Railway 部署

**步驟：**
1. 前往 [Railway](https://railway.app)
2. 連接 GitHub 儲存庫
3. 設定環境變數
4. 自動部署

## 🔧 Git 設定和推送到 GitHub

### 初始化 Git 儲存庫
```bash
git init
git add .
git commit -m "Initial commit: Personal portfolio website"
```

### 連接到 GitHub 儲存庫
```bash
git remote add origin https://github.com/Tristan-hsu/personal_pages.git
git branch -M main
git push -u origin main
```

### 後續更新
```bash
git add .
git commit -m "Update portfolio content"
git push origin main
```

## 🌐 自訂域名設定

### Replit 自訂域名
1. 在 Replit 專案中點擊 "Deployments" 
2. 選擇 "Custom Domain"
3. 輸入您的域名
4. 按照 DNS 設定指示操作

### Cloudflare 設定（選擇性）
如果您使用 Cloudflare：
1. 新增 CNAME 記錄指向部署 URL
2. 開啟 SSL/TLS 加密
3. 設定頁面規則（如需要）

## 📊 監控和維護

### 部署檢查清單
- [ ] 環境變數正確設定
- [ ] GitHub Token 有效且有適當權限
- [ ] 資料庫連接正常
- [ ] 聯絡表單功能正常
- [ ] 語言切換功能正常
- [ ] 響應式設計在各裝置上正常顯示

### 效能監控
- 使用 Replit 內建的監控工具
- 檢查 GitHub API 請求限制使用情況
- 監控表單提交狀況

### 定期維護
- 定期更新 GitHub Token
- 更新個人資訊和專案內容
- 檢查並更新相依套件

## 🔐 安全性建議

### 環境變數管理
- 絕不在程式碼中硬編碼密鑰
- 使用平台提供的密鑰管理系統
- 定期更換 API 令牌

### 資料庫安全
- 使用強密碼
- 定期備份資料庫
- 限制資料庫存取權限

## 📱 SEO 和效能優化

### 建議的後續改進
1. 新增 `robots.txt` 檔案
2. 設定 Google Analytics
3. 加入 meta 標籤優化
4. 實作頁面快取機制
5. 圖片優化和壓縮

### 社群媒體整合
- 新增 Open Graph 標籤
- 設定 Twitter Card
- 加入 LinkedIn 分享功能

## 🆘 常見問題解決

### 部署失敗
1. 檢查環境變數設定
2. 確認 requirements.txt 正確
3. 檢查 Procfile 設定
4. 查看部署日誌

### GitHub API 限制
- 確認 GITHUB_TOKEN 設定正確
- 檢查 API 請求限制使用情況
- 考慮實作快取機制

### 資料庫連接問題
- 檢查 DATABASE_URL 設定
- 確認資料庫服務正常運作
- 檢查網路連接

## 📞 支援聯絡

如果您在部署過程中遇到問題，請檢查：
1. 平台的官方文件
2. 社群論壇和討論區
3. 官方支援管道

---

*祝您部署成功！您的專業作品集網站即將上線。*