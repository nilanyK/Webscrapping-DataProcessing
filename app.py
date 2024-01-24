import streamlit as st
import pandas as pd
import os


def main():
    st.set_page_config(layout="wide", page_title="Sustainable Nike Sneaker Marketplace 🌿", page_icon=":shoe:")

    # Add CSS for background color and styling
    st.markdown(
    """
    <style>
        body {
            background: #f9f9f9;  /* Lighter background */
            font-family: 'Arial', sans-serif;
        }

        .container {
            width: 80%;
            margin: 0 auto;
        }

        .title {
            font-size: 40px; /* Bigger font size */
            text-align: center;
            padding: 20px;
            color: #2c3e50; /* Darker shade for title */
        }

        .mission-text {
            font-size: 20px; /* Slightly larger font */
            text-align: center;
            padding: 20px;
            color: #34495e; /* Darker text color for mission */
        }

        .nav-button:hover {
            background-color: #95a5a6; /* Hover effect for buttons */
            color: white;
        }

        .sneaker-card {
            padding: 20px;
            border: none; /* Removing border */
            border-radius: 10px;
            margin: 10px;
            background: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Deeper shadow for 3D effect */
            transition: box-shadow 0.3s ease-in-out; /* Smooth transition for shadow */
        }

        .sneaker-card:hover {
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* Shadow effect on hover */
        }

        .savings-display {
            font-weight: bold;
            color: #27ae60; /* Green color for savings info */
            font-size: 18px;
            animation: fadeIn 2s; /* Animation for savings display */
        }

        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #ecf0f1; /* Scrollbar track color */
        }

        ::-webkit-scrollbar-thumb {
            background: #7f8c8d; /* Scrollbar thumb color */
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #bdc3c7; /* Hover effect for scrollbar thumb */
        }
    </style>
    """,
    unsafe_allow_html=True,
)


        # Use a single row layout for the image and buttons
    row = st.container()

    # Add the Nike logo to the first column (top-left corner)
    row.image("nike.png", use_column_width=False, width=50)
    
    

    # Render the title
    st.markdown("<h1 class='title'>Sustainable Nike Sneaker Marketplace 🌿</h1>", unsafe_allow_html=True)

    # Render the mission text
    st.markdown("<p class='mission-text'>Empowering users to make environmentally conscious and economically informed choices when purchasing sneakers. 🌍</p>", unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #d8e6e1;'>", unsafe_allow_html=True)


    # Mapping for gender, color, and size (you can add this part based on your mapping)
    gender_mapping = {"homme": 1231, "femme": 1904, "fille": 1255, "garcon": 1256}
    color_mapping = {
        "noir": 1, "blanc": 12, "gris": 3, "bleu": 9, "rose": 5,
        "rouge": 7, "marine": 27, "jaune": 8, "orange": 11, "multicolore": 15,
        "vert": 10, "violet": 6, "turquoise": 17, "bordeaux": 23, "bleu clair": 26,
        "lila": 25, "corail": 22, "beige": 4, "kaki": 16, "doré": 14,
        "argenté": 13, "menthe": 30, "marron": 2, "moutarde": 29, "vert foncé": 28,
        "crème": 20, "abricot": 21
    }
    size_mapping_femme = {
        "34": 1364, "34.5": 1580, "35": 55, "35.5": 1195, "36": 56, "36.5": 1196,
        "37": 57, "37.5": 1197, "38": 58, "38.5": 1198, "39": 59, "39.5": 1199,
        "40": 60, "40.5": 1200, "41": 61, "41.5": 1201, "42": 62, "42.5": 1579,
        "43": 63, "43.5": 1573, "44": 1574, "44.5": 1575, "45": 1576, "45.5": 1577,
        "46": 1578
    }
    size_mapping_homme = {
        "38": 776, "38.5": 777, "39": 778, "39.5": 779, "40": 780, "40.5": 781,
        "41": 782, "41.5": 783, "42": 784, "42.5": 785, "43": 786, "43.5": 787,
        "44": 788, "44,5": 789, "45": 790, "45,5": 791, "46": 792, "46,5": 793,
        "47": 794, "47,5": 795, "48": 1190, "48,5": 1621, "49": 1191, "50": 1327,
        "51": 1622, "52": 1623
    }
    size_mapping_fille_garcon = {
        "15 et moins": 657, "16": 585, "17": 586, "18": 587, "19": 588, "20": 589,
        "21": 590, "22": 591, "23": 592, "24": 593, "25": 594, "26": 595, "27": 596,
        "28": 597, "29": 598, "30": 599, "31": 600, "32": 601, "33": 602, "34": 603,
        "35": 604, "36": 605, "37": 606, "38": 607, "39": 608, "40": 609
    }

    # List of available shoe models
    shoe_models_csv = ["Nike_AirForce1", "NikeAirmax1", "NikeBlazer", "NikeDunk", "NikeMag"]
    shoe_models = ["Nike Air Force 1", "Nike Airmax 1", "Nike Blazer", "Nike Dunk", "Nike Mag"]

    # User inputs for filters
    selected_model = st.selectbox("Select Sneaker Model:", shoe_models)
    
    if selected_model == "Nike Air Force 1":
        selected_model = shoe_models_csv[0]
    elif selected_model == "Nike Airmax 1":
        selected_model = shoe_models_csv[1]
    elif selected_model == "Nike Blazer":
        selected_model = shoe_models_csv[2]
    elif selected_model == "Nike Dunk":
        selected_model = shoe_models_csv[3]
    elif selected_model == "Nike Mag":
        selected_model = shoe_models_csv[4]

    gender = st.selectbox("Select gender:", ["Men", "Women", "Kid"])

    color = st.selectbox("Select color:", [""] + list(color_mapping.keys()))

    # Dynamically set the size options based on the selected gender
    if gender == "Men":
        available_sizes = [""] + list(size_mapping_homme.keys())
    elif gender == "Women":
        available_sizes = [""] + list(size_mapping_femme.keys())
    elif gender == "Kid":
        available_sizes = [""] + list(size_mapping_fille_garcon.keys())
    else:
        available_sizes = [""]  # Default to an empty list if no gender is selected

    size = st.selectbox("Enter size:", available_sizes)

    if st.button("Search"):
        # Load the corresponding CSV files from the folder
        folder_path = os.path.dirname(os.path.abspath(__file__))  # Use the current directory
        csv_files = [file for file in os.listdir(folder_path) if file.startswith(f"FINAL_AllData_{selected_model}.csv")]
        
        if csv_files:
            # Load the first CSV file as an example
            csv_file_path = os.path.join(folder_path, csv_files[0])
            df = pd.read_csv(csv_file_path, sep=",")

            # Apply filters
            filtered_df = df[(df["Gender"] == gender) & (df["Color"] == color.upper()) & (df["Size"] == size)]         

            st.markdown("<hr style='border: 1px solid #d8e6e1;'>", unsafe_allow_html=True)

            # Use columns for a responsive layout
            result_columns = st.columns(3)

            for i, (_, row) in enumerate(filtered_df.iterrows()):
                with result_columns[i % 3]:
                    # Adjust the width of the image and caption
                    st.container()
                    with st.container():
                        st.image(row['Image Source'], width=300, caption="")
                        st.markdown(f"<p style='font-weight: bold; font-size: 20px;'>{row['Title'].upper()}</p>", unsafe_allow_html=True)
                    
                    st.write(f"<p style='font-size: 18px;'>{row['Price']:.2f} €</p>", unsafe_allow_html=True)
                    st.markdown(f"<p> 🌍 You are saving <span style='font-weight: bold; color: #2ecc71;'>{row['Carbon Profit (kg CO2)']:.2f} kg CO2</span> </p>", unsafe_allow_html=True)

                    st.markdown(f"<p>💸 You are making a profit of <span style='font-weight: bold; color: #2ecc71;'>{row['Profit Made']:.2f} €</span></p>", unsafe_allow_html=True)

                    st.markdown(f"[Open Article]({row['Link']})", unsafe_allow_html=True)

                    st.write(f"\n")
                    st.markdown("</div>", unsafe_allow_html=True)
                    # Add a line between each row
                    st.markdown("<hr style='border: 1px solid #d8e6e1;'>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
