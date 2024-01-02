# 服の種類分類アプリ
## 概要
アップロードされた服の画像を分析して、その服の種類を予測します。

予測される服の種類は以下の46種類です。

1: アノラック,2: ブレザー,3: ブラウス,4: ボンバージャケット,5: ボタンダウンシャツ,6: カーディガン,
7: フランネル,8: ホルターネック,9: ヘンリーネック,10: フーディー,11: ジャケット,12: ジャージ,13: パーカ,
14: ピーコート,15: ポンチョ,16: セーター,17: タンクトップ,18: Tシャツ,19: トップス,20: タートルネック,
21: カプリパンツ,22: チノパン,23: キュロット,24: ショートパンツ,25: ガウチョパンツ,26: ジーンズ,
27: ジェギンス,28: ジョッパーズ,29: ジョガーパンツ,30: レギンス,31: サロン,32: ショートパンツ,
33: スカート,34: スウェットパンツ,35: スウェットショーツ,36: トランクス,37: カフタン,38: コート,
39: カバーアップ,40: ドレス,41: ジャンプスーツ,42: カフタン,43: 着物,44: ワンジー,45: ローブ,46: ロンパース

## 実行画面
- 予測される服の種類の上位5件を表示
<img src="https://github.com/HibikiYokoyama/FashionIdentificationApp/assets/89569080/438c6b75-a7c1-4af5-8d98-7d0f033ebb76" width="1000">


## 各コードの概要
- **run_app.py**  
-アプリ実行用プログラム  
- **train_model.py**  
-モデル訓練用プログラム  
-データセットを配置すると動く

## モデルの訓練に使用したデータセット
-  **DeepFashion**: https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html

## 使用ライブラリ
- **streamlit**
- **torch**
- **torchvision**
- **PIL**
- **tqdm**

## 実行コマンド
```bash
streamlit run run_app.py
```
