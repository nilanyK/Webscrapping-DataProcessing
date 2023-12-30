import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Sustainable Nike Sneaker Marketplace",
    page_icon="👟",
    layout="centered",
)

# Define Sneaker Categories
sneaker_categories = {
    "Nike Air Force 1": "Category 1 Description",
    "Nike Blazer": "Category 2 Description",
    "Nike Dunk": "Category 3 Description",
    "Nike Mag": "Category 4 Description",
    "Nike Air Max 1": "Category 5 Description",
}

import os



# Main Page
st.title("Sustainable Nike Sneaker Marketplace")

# Display Categories with Images
col1, col2, col3, col4, col5 = st.columns(5)

for category, description in sneaker_categories.items():
    with col1:
        base_path = os.path.abspath(os.path.dirname(__file__))
        image_path = os.path.join(base_path, "images", f"{category}.jpg")
        st.image(image_path, caption=category, width=300, use_column_width=True)
        st.write(description)

# Category Selection
selected_category = st.selectbox("Select a category", list(sneaker_categories.keys()))

# Placeholder for category-specific information
st.write(f"Displaying {selected_category} sneakers")

# Add a link to navigate to the next page
if st.button("Explore"):
    st.write("Redirecting to the filter page...")
    # You can add a redirection or load another page here

# Filter Page
if "Explore" in st.session_state:
    st.title(f"Explore {selected_category} Sneakers")

    # Filter Sidebar
    st.sidebar.title("Filter Options")
    gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Kids"])
    colors = st.sidebar.multiselect("Colors", ["Green", "White", "Black", "Blue"])
    sizes = st.sidebar.multiselect("Sizes", ["US 7", "US 8", "US 9", "US 10"])

    # Display Filtered Sneakers
    st.write(f"Filtered by: Gender - {gender}, Colors - {colors}, Sizes - {sizes}")
    # You can display the filtered sneakers here based on the selected options
