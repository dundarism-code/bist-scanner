import yfinance as yf
import pandas as pd

symbols = ["TEHOL.IS", "ISKPL.IS", "CEMAS.IS"]

results = []

for symbol in symbols:
    data = yf.download(symbol, period="60d")

    if data.empty:
        continue

    last_close = data["Close"].iloc[-1]
    last_volume = data["Volume"].iloc[-1]
    avg_volume = data["Volume"].rolling(20).mean().iloc[-1]

    volume_spike = last_volume > 2 * avg_volume

    results.append({
        "symbol": symbol,
        "close": round(float(last_close), 2),
        "volume": int(last_volume),
        "avg_volume_20": int(avg_volume),
        "volume_spike": volume_spike
    })

df = pd.DataFrame(results)

print(df)

df.to_csv("scan_results.csv", index=False)
