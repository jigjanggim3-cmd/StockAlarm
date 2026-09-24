import yfinance as yf
import requests

TOKEN = '8880512706:AAELTlQXsRelaPvXbmqUFFEw7bx0tpkZP8w'
CHAT_ID = '8654083409'

# 삼성전자 데이터 (최근 21일)
stock = yf.Ticker("005930.KS")
hist = stock.history(period="21d")

# 현재가와 20일 이동평균선(MA20) 계산
price = hist['Close'].iloc[-1]
ma20 = hist['Close'].rolling(window=20).mean().iloc[-1]

# 알림 로직
if price > ma20:
    message = f"매수 신호! 삼성전자({price:.0f}원)가 20일 평균({ma20:.0f}원)을 뚫고 상승 중!"
else:
    message = f"관망 모드. 삼성전자({price:.0f}원)가 20일 평균({ma20:.0f}원)보다 낮음."

# 텔레그램 발송
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
requests.get(url)
print("분석 완료! 폰으로 전송했어.")