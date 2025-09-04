import streamlit as st
from scrape import scrape_website,split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_ollama
st.title("AI webscraper")
url = st.text_input("Enter the URL of the website you want to scrape:")

if st.button("Scrape"):
    st.write("Scraping the website...")

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content

    with st.expander("View Scraped Content"):
        st.text_area("Scraped Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want")

    if st.button("parse content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)

# to run streamlit run main.py
