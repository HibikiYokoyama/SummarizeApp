import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
import re

# 追加訓練済みT5とトークナイザの読み込み
t5_model = T5ForConditionalGeneration.from_pretrained('./models')
t5_tokenizer = T5Tokenizer.from_pretrained('sonoisa/t5-base-japanese', legacy=False)
t5_model.eval()

# Streamlit UIの設定
st.title('文章要約アプリ')
text = st.text_area("ここに文章を入力してください", height=250)
if st.button('要約') and text:
    try:
        tokens = t5_tokenizer.encode("summarize: " + text, add_special_tokens=False)
        if len(tokens) > 512:
            st.warning("入力されたテキストが長すぎるため、一部のテキストが読み込まれていない可能性があります。")

        # 入力テキストのトークナイズ
        inputs = t5_tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
        # 要約の生成
        summary_ids = t5_model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        s = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # 重複文もしくは最後の文が句点で終わってない場合、それを削除
        s_list = re.split(r'(?<=。)', s)
        dup_chk = set()
        summary = [s for s in s_list if s and (s not in dup_chk) and not dup_chk.add(s)]
        # 句点で終わってない場合削除
        if summary and summary[-1][-1] != '。':
            summary.pop()

        # 要約結果の表示
        st.write(*summary)
    except Exception as e:
        st.error(f"要約中にエラーが発生しました: {e}")
