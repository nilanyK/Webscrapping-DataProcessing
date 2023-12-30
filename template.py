# Import necessary libraries
import streamlit as st

# Define functions for different pages
def home_page():
    st.title("Sustainable Nike Shoes Marketplace")
    st.write("Welcome to our marketplace for sustainable Nike shoes.")
    st.image("nike_logo.png", caption="Sustainable Nike Shoes")

def browse_page():
    st.title("Browse Shoes")
    st.write("Explore our collection of sustainable Nike shoes.")
    # Add code to display the list of shoes and their details

def about_page():
    st.title("About Us")
    st.write("Learn more about our mission and commitment to sustainability.")
    # Add information about the marketplace and sustainability efforts

def contact_page():
    st.title("Contact Us")
    st.write("Get in touch with us for any inquiries or collaboration opportunities.")
    # Add contact form or contact information

# Create navigation bar
navigation = ["Home", "Browse Shoes", "About Us", "Contact Us"]
choice = st.sidebar.selectbox("Navigate", navigation)

# Display the selected page
if choice == "Home":
    home_page()
elif choice == "Browse Shoes":
    browse_page()
elif choice == "About Us":
    about_page()
elif choice == "Contact Us":
    contact_page()

# Add custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #e6f7ff;
        }
        .sidebar .sidebar-content {
            background-color: #66ff66;
        }
        .main .block-container {
            background-color: #ffffff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 1rem;
            border-radius: 0.375rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
