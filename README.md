# 文章要約アプリ
## 概要
アップロードされた文章の要約を出力する。

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
