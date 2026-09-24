import os
import requests
from datetime import datetime

# 監視設定（静龍苑の店舗IDと10月、2・3名席）
SHOP_ID = "seiryuen"
YEAR_MONTH = "2026-10"  # 10月を監視
TARGET_COURSES = [2, 3]  # 2名、3名

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

def check_slots():
    url = f"https://tablecheck.com{SHOP_ID}/clear_slots"
    params = {"month": YEAR_MONTH, "party_size": 2} # 代表でリクエスト
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            return
        
        data = response.json()
        # 日付ごとの空き枠をチェックするロジック
        # ※TableCheckの仕様に合わせて空席検知
        available_dates = []
        
        # 簡易デモ用ロジック（実際はAPI構造に合わせて解析します）
        # 空席が見つかった場合、Discordへ通知
        if available_dates:
            msg = f"【静龍苑】10月の空席（2名/3名）が見つかりました！\nhttps://tablecheck.com{SHOP_ID}/reserve"
            requests.post(DISCORD_WEBHOOK_URL, json={"content": msg})
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if DISCORD_WEBHOOK_URL:
        check_slots()
