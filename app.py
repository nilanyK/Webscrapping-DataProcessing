import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from geopy.distance import geodesic
from geopy.geocoders import Nominatim


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

import os

import hydralit_components as hc
import streamlit as st

import state
from pages_views.compare import ComparePage
from pages_views.document_collection import DocumentCollection
from pages_views.howto import HowToPage
from pages_views.rag import RetrievalAugmentedGeneration
from pages_views.sidebar import CompareSidebarWithSnowflakeSettings, HowToSidebar, CompareSidebarWithTagFilter

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

def get_vinted_data(query, gender=None, color=None, size=None):
    # Resolve gender, color, and size IDs based on user input
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
    gender_id = gender_mapping.get(gender.lower(), None)
    color_id = color_mapping.get(color.lower(), None)
    size_id = None
    if gender_id == 1904:  # Femme
        size_id = size_mapping_femme.get(size, None)
    elif gender_id == 1231:  # Homme
        size_id = size_mapping_homme.get(size, None)
    elif gender_id in (1255, 1256):  # Fille or Garcon
        size_id = size_mapping_fille_garcon.get(size, None)

    # Constructing the base URL with gender_ids, color_ids, and size_ids
    base_url = "https://www.vinted.fr/catalog?brand_ids[]=53&"
    if gender_id:
        base_url += f"catalog[]={gender_id}&"
    if color_id:
        base_url += f"color_ids[]={color_id}&"
    if size_id:
        base_url += f"size_ids[]={size_id}&"

    my_url = f"{base_url}search_text={query.replace(' ', '%20')}"

    driver = webdriver.Firefox()
    driver.get(my_url)

    # Handle cookie acceptance
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
        )
        cookie_button.click()
    except:
        print("Cookie button not found or timed out")

    data = {"Title": [], "Price": [], "Brand": [], "Size": [], "Link": [], "Image Source": [], "Localisation": []}

    while True:
        try:
            # Wait for the articles to load on the current page
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'feed-grid'))
            )

            # Find the new articles on the current page
            article_body = driver.find_element(By.CLASS_NAME, 'feed-grid')
            articles = article_body.find_elements(By.CLASS_NAME, "feed-grid__item")

            for article in articles:
                try:
                    title_element = article.find_element(By.CLASS_NAME, 'new-item-box__overlay')
                    title = title_element.get_attribute('title')

                    # Extracting data from the title attribute
                    price_start = title.find('prix') + len('prix&nbsp;:')
                    price_end = title.find('&nbsp;€', price_start)
                    price = title[price_start:price_end].strip()

                    brand_start = title.find('marque') + len('marque&nbsp;:')
                    brand_end = title.find(',', brand_start)
                    brand = title[brand_start:brand_end].strip()

                    size_start = title.find('taille') + len('taille&nbsp;:')
                    size_end = title.find(',', size_start)
                    size = title[size_start:size_end].strip()

                    href = title_element.get_attribute('href')

                    # Extract image source from the correct elements
                    div_element = article.find_element(By.CLASS_NAME, 'new-item-box__image')
                    img_element = div_element.find_element(By.CLASS_NAME, 'web_ui__Image__content')
                    img_src = img_element.get_attribute('src')

                    # Extract localisation information from article's href link
                    driver.execute_script("window.open('', '_blank');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(href)

                    try:
                        localisation_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//div[@class="details-list__item" and @data-testid="item-details-location"]/div[@class="details-list__item-value"]'))
                        )
                        localisation = localisation_element.text
                    except:
                        localisation = None

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                    data["Title"].append(title)
                    data["Price"].append(price)
                    data["Brand"].append(brand)
                    data["Size"].append(size)
                    data["Link"].append(href)
                    data["Image Source"].append(img_src)
                    data["Localisation"].append(localisation)

                except ValueError:
                    pass

            next_page_link = driver.find_element(By.CLASS_NAME, "web_ui__Pagination__next").get_attribute('href')

            driver.get(next_page_link)

        except NoSuchElementException:
            # If the "Next Page" is not found, break out of the loop
            break

    driver.quit()
    return pd.DataFrame(data)

def process_dataframe(df):
    data = {
        'Title': [],
        'Price': [],
        'Brand': [],
        'Size': [],
        'Link': [],
        'Image Source': [],
        'Localisation': []
    }

    for index, row in df.iterrows():
        title_components = row['Title'].split(', ')
        data['Title'].append(title_components[0])

        price_components = title_components[1].split(':')
        if len(price_components) > 1:
            price = price_components[1].strip().replace('€', '').replace('\xa0', '')
            data['Price'].append(float(price.replace(',', '.')) if price else None)
        else:
            data['Price'].append(None)

        brand_components = title_components[2].split(':')
        data['Brand'].append(brand_components[1].strip().upper() if len(brand_components) > 1 else None)

        size_components = title_components[3].split(':')
        data['Size'].append(size_components[1].strip() if len(size_components) > 1 else None)
        data['Link'].append(row['Link'])
        data['Image Source'].append(row['Image Source'])
        data['Localisation'].append(row['Localisation'])

    return pd.DataFrame(data)

from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Initialize geocoder
geolocator = Nominatim(user_agent="vinted_carbon_footprint")

def calculate_approximate_carbon_footprint(location):
    try:
        # Geocode the location to get coordinates
        location_info = geolocator.geocode(location, timeout=10)

        if location_info:
            location_coordinates = (location_info.latitude, location_info.longitude)

            # Coordinates of Paris, France
            paris_coordinates = (48.8566, 2.3522)

            # Calculate the distance between the location and Paris using geopy
            distance_km = geodesic(location_coordinates, paris_coordinates).kilometers

            # Assume a constant emission rate per kilometer 
            emission_rate_per_km = 0.2  
            # Calculate the approximate carbon footprint
            carbon_footprint = distance_km * emission_rate_per_km

            return carbon_footprint

    except (ValueError, TypeError, GeocoderTimedOut):
        # Handle cases where geocoding fails or times out
        return None


from selenium import webdriver

from selenium.webdriver.common.by import By

def accept_cookies(driver):
    try:
        # Accept cookies
        accept_cookies_button = driver.find_element(By.CLASS_NAME, 'btn-primary-dark')
        accept_cookies_button.click()
    except:
        pass  

def get_nike_prices(search_query):
    driver = webdriver.Firefox()
    
    try:
        # Go to nike.fr and accept cookies
        driver.get("https://www.nike.com/fr/")
        accept_cookies(driver)

        # Construct the URL with the search query
        url = f"https://www.nike.com/fr/w?q={search_query.replace(' ', '%20')}"

        # Navigate to the URL with the search query
        driver.get(url)

        # Wait for the prices to load 
        driver.implicitly_wait(10)

        # Retrieve prices
        price_elements = driver.find_elements(By.CLASS_NAME, 'product-price')
        prices = [float(price.text.replace('€', '').replace(',', '.')) for price in price_elements]

        # Calculate the average price
        average_price = sum(prices) / len(prices)

        return average_price

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()


def calculate_profit_made(row, average_nike_price):
    try:
        item_price = float(row['Price'])
        profit_made = average_nike_price - item_price
        return profit_made

    except ValueError:
        return None
    



# Function to create Streamlit app
def vinted_streamlit_app():
    st.set_page_config(
        page_title="Sustainable Nike Sneaker Marketplace",
        page_icon=os.path.join(os.path.dirname(__file__), "images", "favicon.png"),
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("<h1 style='text-align: center; background-color: #000045; color: #ece5f6'>K-A-T-E One</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; background-color: #000045; color: #ece5f6'>Knowledge, Access, and Technology for ESG</h4>", unsafe_allow_html=True)

    menu_data = [
        {'id': 1, 'label': "How To", 'key': "md_how_to", 'icon': "fa fa-home"},
        {'id': 2, 'label': "Sneaker Marketplace", 'key': "md_sneaker_marketplace"},
        {'id': 3, 'label': "Document Collection", 'key': "md_document_collection"},
        {'id': 4, 'label': "Semantic Q&A", 'key': "md_rag"}
    ]

    # Set the page based on the menu
    state.set_page_id(int(hc.nav_bar(
        menu_definition=menu_data,
        hide_streamlit_markers=False,
        sticky_nav=True,
        sticky_mode='pinned',
        override_theme={'menu_background': '#4c00a5'}
    )))

    # Check the current page and display the corresponding content
    if state.get_page_id() == 1:
        # Display How To Page
        st.sidebar.header("📌 About the Project")
        st.sidebar.markdown("""
        In the evolving landscape of e-commerce, our project aims to address the growing demand for sustainable options within niche markets, specifically focusing on second-hand Nike sneakers.

        The project involves the development of a dedicated interface that allows users to explore pre-owned Nike sneakers. How can we empower users to make sustainable and economical choices when purchasing second-hand Nike sneakers?

        Through web scraping, we will gather data from popular platforms like Vinted and Vestiaire Collective to create a comprehensive database. Features such as profit calculation and the estimation of the carbon footprint associated with shipping will be proposed.

        The price comparison feature entails evaluating the average original price scraped directly from Nike's data against the second-hand price. Additionally, the carbon footprint comparison provides users with insights into the environmental impact associated with shipping second-hand items compared to ordering directly from Nike.

        👨‍💻 Authors : [Nilany KARUNATHASAN](https://www.linkedin.com/in/nilany-karunathasan-7b49691ba?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) and [Sïndoumady SAMBATH](https://www.linkedin.com/in/s%C3%AFndoumady-sambath-a7519a209?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)
        """)
        st.sidebar.markdown("<hr style='margin: 10px;'>", unsafe_allow_html=True)

    elif state.get_page_id() == 2:
        # Display Sneaker Marketplace
        st.sidebar.header("🔍 Search Filters")
        query = st.sidebar.text_input("Enter your sneaker query:")
        gender = st.sidebar.selectbox("Select gender:", ["homme", "femme", "fille", "garcon"])
        color = st.sidebar.selectbox("Select color:", [""] + list(color_mapping.keys()))

        # Dynamically set the size options based on the selected gender
        if gender == "homme":
            available_sizes = [""] + list(size_mapping_homme.keys())
        elif gender == "femme":
            available_sizes = [""] + list(size_mapping_femme.keys())
        elif gender in ["fille", "garcon"]:
            available_sizes = [""] + list(size_mapping_fille_garcon.keys())
        else:
            available_sizes = [""]  # Default to an empty list if no gender is selected

        size = st.sidebar.selectbox("Enter size:", available_sizes)

        if st.sidebar.button("Search"):
            st.sidebar.info("Searching... Please wait.")
            vinted_data = get_vinted_data(query, gender=gender, color=color, size=size)
            processed_data = process_dataframe(vinted_data)

            # Get Nike prices and calculate profit made
            average_nike_price = get_nike_prices(query)
            processed_data.sort_values(by='Price', inplace=True)
            # Adding columns to the DataFrame for the approximate carbon footprint and Nike's fixed value
            processed_data["Approximate Carbon Footprint (kg CO2)"] = processed_data["Localisation"].apply(calculate_approximate_carbon_footprint)
            processed_data["Approximative Carbon Print from Ordering on Nike (kg CO2/ton)"] = 405  

            # Adding a column for Carbon Profit
            processed_data["Carbon Profit (kg CO2)"] = processed_data["Approximative Carbon Print from Ordering on Nike (kg CO2/ton)"] - processed_data["Approximate Carbon Footprint (kg CO2)"]
            # Calculate profit made for Vinted data
            processed_data['Average price of the product on Nike'] = average_nike_price
            processed_data['Profit Made'] = processed_data.apply(lambda row: calculate_profit_made(row, average_nike_price), axis=1)

            # Display results in a Google Shopping-style layout
            st.sidebar.subheader("👟 Search Results")

            # Use columns for a responsive layout
            result_columns = st.sidebar.columns(3)

            for i, (_, row) in enumerate(processed_data.iterrows()):
                with result_columns[i % 3]:
                    # Adjust the width of the image and caption
                    st.sidebar.image(row['Image Source'], width=150, caption=row['Title'])
                    st.sidebar.write(f"**Size:** {row['Size']}  \n**Price:** €{row['Price']:.2f} 💰")
                    st.sidebar.write(f"**Carbon Print:** {row['Carbon Profit (kg CO2)']:.2f} kg CO2 🌍")
                    st.sidebar.write(f"**Profit:** €{row['Profit Made']:.2f}  \n**Approx. Nike Price:** €{average_nike_price:.2f} 💸")

                    # Add a line between each row
                st.sidebar.markdown("<hr style='margin: 10px;'>", unsafe_allow_html=True)



if __name__ == "__main__":
    vinted_streamlit_app()