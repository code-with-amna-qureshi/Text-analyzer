import streamlit as st
import base64

# Setting background image
def set_bg(image_file):
    with open(image_file, "rb") as file:
        img = file.read()
    b64_img = base64.b64encode(img).decode()
    bg_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{b64_img}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_image, unsafe_allow_html=True)

# Call the function with your local image file
set_bg("text checker/softcolor.jpg")

st.title("📜  Text Analyzer")
st.write("This is a simple text analyzer that counts words, characters, spaces, vowels, and allows word replacement. ✍️")

# Text input
text = st.text_area("Enter text here 📝")

if st.button("Analyze 🔍"):
    if text:
        words = len(text.split())
        characters = len(text)
        spaces = text.count(' ')
        vowels = sum(text.lower().count(v) for v in 'aeiou')

        st.write(f"**Word Count:** {words}")
        st.write(f"**Character Count:** {characters}")
        st.write(f"**Space Count:** {spaces}")
        st.write(f"**Vowel Count:** {vowels}")
    else:
        st.warning("Please enter some text to analyze!")

# Word replacement
search_word = st.text_input("Enter the word to search for 🔍")
replace_word = st.text_input("Enter the word to replace it with 🔄")

if st.button("Replace Word"):
    if text and search_word:
        updated_text = text.replace(search_word, replace_word)
        st.write("**Updated Text:**")
        st.write(updated_text)
    else:
        st.warning("Please enter text and the word to search for!")

st.write("---")
st.write("Developed by Amna Qureshi 💻✨")



