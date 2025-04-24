import json

# 入力ファイルと出力ファイルのパス
input_path = "P29-23_12.geojson"
output_path = "P29-23_12_filtered.geojson"

# 読み込み
with open(input_path, encoding="utf-8") as f:
    data = json.load(f)

# フィルター処理：各種学校・専修学校（P29_003が16015または16016）を除外
filtered_features = [
    feat for feat in data["features"]
    if feat["properties"].get("P29_003") not in ("16015", "16016")
]

# 新しいGeoJSONとして保存
filtered_geojson = {
    "type": "FeatureCollection",
    "features": filtered_features
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(filtered_geojson, f, ensure_ascii=False, indent=2)

print(f"フィルター済みデータを書き出しました：{output_path}")
