# 文章要約アプリ
## 概要
アップロードされた文章の要約を出力する。

## 実行画面
- 文章の要約を出力
> 文章には<https://news.yahoo.co.jp/articles/c8fa30978646961dd3d0d1e0676337d7953b882e>の記事内容を使用
<img src="https://github.com/HibikiYokoyama/SummarizeApp/assets/89569080/43c0fbf3-0066-49bb-a925-85a9c9bad245" width="800">

- 文章が長い場合、警告を表示
> 文章には<https://news.yahoo.co.jp/articles/2fcf8620adb9374d129589678ec92b519dc1b1f7>の記事内容を使用
<img src="https://github.com/HibikiYokoyama/SummarizeApp/assets/89569080/f1bb56ab-98f9-4e1f-9863-d06f1db7d6a7" width="800">

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
