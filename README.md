# 文章要約アプリ
## 概要
アップロードされた文章の要約を出力する。

## 実行画面
- 文章の要約を出力
<img src="https://github.com/HibikiYokoyama/FashionIdentificationApp/assets/89569080/438c6b75-a7c1-4af5-8d98-7d0f033ebb76" width="1000">

- 文章が長い場合、警告を表示
<img src="https://github.com/HibikiYokoyama/FashionIdentificationApp/assets/89569080/438c6b75-a7c1-4af5-8d98-7d0f033ebb76" width="1000">

## 各コードの概要
- **run_app.py**  
-アプリ実行用プログラム

## モデルの訓練に使用したデータセット
-  **ThreeLineSummaryDataset（https://github.com/KodairaTomonori/ThreeLineSummaryDataset）** の一部をスクレイピングして使用

## 使用ライブラリ
- **streamlit 1.29.0**
- **transformers 4.36.2**
- **torch 2.1.2**
- **sentencepiece 0.1.99**

## 実行コマンド
```bash
streamlit run run_app.py
```
