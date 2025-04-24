import pandas as pd
import json

def meshcode_to_latlon(code):
    code = str(code)
    if len(code) < 10:
        return None, None

    lat_base = int(code[0:2]) * 2 / 3
    lon_base = int(code[2:4]) + 100
    lat_base += int(code[4]) * 5 / 60
    lon_base += int(code[5]) * 7.5 / 60
    lat_base += int(code[6]) * 30 / 3600
    lon_base += int(code[7]) * 45 / 3600
    lat_base += (int(code[8]) * 30 / 3600) / 2
    lon_base += (int(code[9]) * 45 / 3600) / 2

    return round(lon_base, 6), round(lat_base, 6)

jcode_map = {
    10: "谷底低地", 12: "自然堤防", 13: "後背湿地", 14: "旧河道・旧池沼", 15: "三角州・海岸低地", 16: "砂州・砂礫州",
    17: "砂丘", 18: "砂丘・砂州間低地", 19: "干拓地", 20: "埋立地", 22: "河原",
    23: "河道"
}

df = pd.read_csv("ekijouka_filtered.csv")
features = []

for _, row in df.iterrows():
    lon, lat = meshcode_to_latlon(row["CODE"])
    if lon is None or lat is None:
        continue
    jcode = int(row["JCODE"])
    jdesc = jcode_map.get(jcode, "不明")
    level = int(row["LV"])
    features.append({
        "type": "Feature",
        "properties": {
            "risk": level,
            "JCODE": jcode,
            "type_jcode": jdesc
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat]
        }
    })

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open("ekijouka.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)
