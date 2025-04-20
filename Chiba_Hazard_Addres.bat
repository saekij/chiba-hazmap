@echo off
cd /d "C:\Users\junda\Dropbox\00 講演関係\00 個別資料\千葉県防災研修センター\202507 防災マップ活用セミナー\map"

start "" python -m http.server 8000

timeout /t 2 >nul  REM サーバー起動待ち

start microsoft-edge:http://localhost:8000/index.html
