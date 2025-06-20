import streamlit as st
from datetime import datetime, timedelta

st.title("📅 X 検索コマンド自動生成ツール")
st.write("スルガ銀行サイクリングプロジェクト（@SURUGAbank_road）の投稿検索リンクを作ろう！")

account = "SURUGAbank_road"
search_type = st.selectbox("検索タイプを選んでね", ["特定の日付", "月間投稿", "キーワード検索", "キーワード＋期間検索"])

if search_type == "特定の日付":
    date = st.date_input("検索する日付を選んでね")
    if st.button("生成！"):
        since = date.strftime("%Y-%m-%d")
        until = (date + timedelta(days=1)).strftime("%Y-%m-%d")
        command = f"from:{account} since:{since} until:{until}"
        url = f"https://twitter.com/search?q=from%3A{account}%20since%3A{since}%20until%3A{until}&src=typed_query"
        st.code(command, language="text")
        st.markdown(f"[検索リンクはこちら]({url})")

elif search_type == "月間投稿":
    start = st.date_input("開始日")
    end = st.date_input("終了日")
    if start < end and st.button("生成！"):
        command = f"from:{account} since:{start} until:{end}"
        url = f"https://twitter.com/search?q=from%3A{account}%20since%3A{start}%20until%3A{end}&src=typed_query"
        st.code(command, language="text")
        st.markdown(f"[検索リンクはこちら]({url})")

elif search_type == "キーワード検索":
    keyword = st.text_input("キーワード（例: ライド）")
    if keyword and st.button("生成！"):
        command = f"from:{account} {keyword}"
        url = f"https://twitter.com/search?q=from%3A{account}%20{keyword}&src=typed_query"
        st.code(command, language="text")
        st.markdown(f"[検索リンクはこちら]({url})")

elif search_type == "キーワード＋期間検索":
    keyword = st.text_input("キーワード（例: ライド）")
    start = st.date_input("開始日")
    end = st.date_input("終了日")
    if keyword and start < end and st.button("生成！"):
        until = (end + timedelta(days=1)).strftime("%Y-%m-%d")
        command = f"from:{account} {keyword} since:{start} until:{until}"
        url = f"https://twitter.com/search?q=from%3A{account}%20{keyword}%20since%3A{start}%20until%3A{until}&src=typed_query"
        st.code(command, language="text")
        st.markdown(f"[検索リンクはこちら]({url})")
