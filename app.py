import streamlit as st
st.set_page_config(layout="wide")
st.title("✍️ LLM End-to-End Project 🤖")
st.subheader("Now you can craft perfect blogs with the help of AI-BlogCraft is your New AI Blog Companion")
blog="Jesus Christ is one of the most influential figures in history and the central figure of Christianity. Christians believe that He is the Son of God who came to Earth to teach love, compassion, forgiveness, and faith. Jesus was born in Bethlehem and spent much of His life teaching people about God's kingdom and helping those in need. His teachings, recorded in the Bible, emphasize kindness, humility, and caring for others. Christians believe that Jesus was crucified, died, and rose again after three days, offering salvation and eternal life to those who believe in Him. His message continues to inspire billions of people around the world."
with st.sidebar:
     st.title("Input Your Blog Details")
     st.subheader("Enter Details of the Blog you want to Generate")
     
     blog_title = st.text_input("Blog Title")
     blog_keywords = st.text_area("Blog Keywords (comma separated)")
     num_words = st.slider("Number of Words", min_value=50, max_value=2000, step=100)
     num_images = st.number_input("Number of Images", min_value=0, max_value=50, step=1)
     submit_button = st.button("Generate Blog")
if submit_button:
     st.image("https://tse2.mm.bing.net/th/id/OIP.tnZWCdb8MDNX5hynWW0BHAHaEK?rs=1&pid=ImgDetMain&o=7&rm=3")
     st.write(blog)



