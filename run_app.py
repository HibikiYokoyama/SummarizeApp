import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
import re

t5_model = T5ForConditionalGeneration.from_pretrained('./models')
t5_tokenizer = T5Tokenizer.from_pretrained('sonoisa/t5-base-japanese', legacy=False)
t5_model.eval()

st.title('文章要約アプリ')
text = st.text_area("ここに文章を入力してください", height=250)
if st.button('要約') and text:
    try:
        tokens = t5_tokenizer.encode("summarize: " + text, add_special_tokens=False)
        if len(tokens) > 512:
            st.warning("入力されたテキストが長すぎるため、一部のテキストが読み込まれていない可能性があります。")

        inputs = t5_tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = t5_model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        s = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        s_list = re.split(r'(?<=。)', s)
        dup_chk = set()
        summary = [s for s in s_list if s and (s not in dup_chk) and not dup_chk.add(s)]
        if summary and summary[-1][-1] != '。':
            summary.pop()

        st.write(*summary)
    except Exception as e:
        st.error(f"要約中にエラーが発生しました: {e}")
