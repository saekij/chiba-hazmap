import pandas as pd

# CSVファイル読み込み
df = pd.read_csv("ekijouka_filtered.csv")

# AVS値に基づく危険度（LV）の再分類
def classify_lv(avs):
    if avs < 200:
        return 3
    elif avs < 400:
        return 2
    elif avs < 600:
        return 1
    else:
        return 0

# LV列の更新
df["LV"] = df["AVS"].apply(classify_lv)

# 上書き保存
df.to_csv("ekijouka_filtered.csv", index=False, encoding="utf-8-sig")
