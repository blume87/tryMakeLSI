import nazca as nd # Nazcaのインポート
nd.image('あさがおのロゴ.png', threshold=0.9, size=500, pixelsize=1.0, layer=12).put(0) # 画像の取り込み
nd.export_gds() # GDSファイルを出力