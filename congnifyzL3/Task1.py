import streamlit as st
import pandas as pd
import plotly.express as px
from scraper import WebScraper

st.set_page_config(
    page_title="Web Scraper Dashboard",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Web Scraper Dashboard")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

if st.button("Start Scraping"):

    if url:

        try:

            scraper = WebScraper(url)

            st.success("Website Scraped Successfully!")

            st.header("Website Title")
            st.write(scraper.get_title())

            headings = scraper.get_headings()
            links = scraper.get_links()
            images = scraper.get_images()
            paragraphs = scraper.get_paragraphs()
            tables = scraper.get_tables()

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Headings", len(headings))
            c2.metric("Links", len(links))
            c3.metric("Images", len(images))
            c4.metric("Paragraphs", len(paragraphs))

            chart_data = pd.DataFrame({
                "Category": [
                    "Headings",
                    "Links",
                    "Images",
                    "Paragraphs"
                ],
                "Count": [
                    len(headings),
                    len(links),
                    len(images),
                    len(paragraphs)
                ]
            })

            fig = px.bar(
                chart_data,
                x="Category",
                y="Count",
                color="Category",
                title="Website Content Summary"
            )

            st.plotly_chart(fig, use_container_width=True)

            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "Headings",
                "Links",
                "Images",
                "Paragraphs",
                "Tables"
            ])

            with tab1:
                st.dataframe(headings)

            with tab2:
                st.dataframe(links)

                csv = links.to_csv(index=False)

                st.download_button(
                    "Download Links CSV",
                    csv,
                    "links.csv"
                )

            with tab3:
                st.dataframe(images)

            with tab4:
                st.dataframe(paragraphs)

            with tab5:

                if len(tables):

                    for i, table in enumerate(tables):
                        st.write(f"Table {i+1}")
                        st.dataframe(table)

                else:
                    st.info("No HTML Tables Found")

        except Exception as e:

            st.error(e)

    else:
        st.warning("Please Enter Website URL")