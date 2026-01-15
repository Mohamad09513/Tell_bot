name: Run Telegram Bot 24/7
on:
  push:
    branches: [ main ]
  workflow_dispatch: # يسمح بتشغيله يدويًا من واجهة GitHub

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 تحميل الكود من المستودع
        uses: actions/checkout@v3

      - name: 🐍 إعداد بايثون
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: 📦 تثبيت المكتبات المطلوبة
        run: pip install -r requirements.txt

      - name: 🤖 تشغيل بوت التلغرام
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }} # يقرأ التوكن من الإعدادات السرية
        run: python bot.py
