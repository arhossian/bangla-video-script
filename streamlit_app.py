import openai
import streamlit as st
import os

openai.api_key = st.secrets["openai_api_key"]

st.set_page_config(page_title="Bangla YouTube Script Generator", layout="centered")
st.title("🇧🇩 বাংলা ইউটিউব স্ক্রিপ্ট জেনারেটর")
st.markdown("প্রম্পট দিন, বাংলা স্ক্রিপ্ট পেয়ে যান!")

prompt = st.text_input("🔸 আপনার ভিডিওর বিষয় লিখুন (উদাহরণ: 'আত্ম-নিয়ন্ত্রণের গুরুত্ব'):", "")

if st.button("✍️ স্ক্রিপ্ট তৈরি করুন") and prompt:
    with st.spinner("স্ক্রিপ্ট তৈরি হচ্ছে, একটু অপেক্ষা করুন..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "তুমি একজন পেশাদার ইউটিউব স্ক্রিপ্ট লেখক। বাংলায় সহজ, অনুপ্রেরণামূলক স্ক্রিপ্ট লেখো।"},
                    {"role": "user", "content": f"{prompt} বিষয়ে একটি ২-৩ মিনিটের বাংলা ইউটিউব স্ক্রিপ্ট লেখো।"}
                ],
                temperature=0.7
            )
            script = response['choices'][0]['message']['content']
            st.success("✅ স্ক্রিপ্ট তৈরি হয়েছে!")
            st.text_area("📜 নিচে আপনার স্ক্রিপ্ট:", script, height=300)

            if not os.path.exists("scripts"):
                os.makedirs("scripts")
            with open("scripts/generated_script.txt", "w", encoding="utf-8") as f:
                f.write(script)
        except Exception as e:
            st.error(f"❌ সমস্যা হয়েছে: {e}")
