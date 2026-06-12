# BLE Sensor Sample

Qiitaで紹介したPythonとBleakを使ってBaldrTerm温湿度センサーからBLE通信で温度・湿度・電波状況を取得するサンプルです。

## リンク
* Qiita:  
https://qiita.com/Choco-chip_melon-pan/items/0394b340c01c72a62400

* はてなブログ:  
https://choco-cjip.hatenablog.com/entry/2026/04/15/224309

## 確認済動作環境
- Windows 11
- Raspberry PI 3 Model B
- Python 3.12
- bleak

## インストール
```
pip install bleak
```

## 内容

* device_scan.py  
デバイスをスキャンしてデバイスIDを取得する。

* device_info.py  
デバイスIDを記述する。

* check_service.py  
サービスIDを確認する。

* check_notify.py  
広告モードで流れてくるデータを確認する。

* tmp_Linear_regression.py  
センサー画面の温度値と、広告モードで流れてくるデータの生値をもとに、最小二乗法で温度を計算する係数を求める。

* get_temp_and_hum.py  
BaldrTerm温湿度センサーからBLE通信で温度・湿度・電波状況を取得する

## ライセンス

MIT License