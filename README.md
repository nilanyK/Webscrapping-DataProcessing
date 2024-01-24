ESILV - Machine Learning for NLP - Project 2024 <br>
[KARUNATHASAN Nilany](https://www.linkedin.com/in/nilany-karunathasan-7b49691ba/) <br>
[SAMBATH Sïndoumady](https://www.linkedin.com/in/s%C3%AFndoumady-sambath-a7519a209/) <br>
<br>

<br>
<h1 align="center">Sustainable Nike Sneaker Marketplace 👟</h1>
<br>
<br>
<div style="text-align: center;">
    <span style="display: inline-block; margin-right: 20px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Vinted_logo.png" alt="Trustpilot Logo" width="100"/>
    </span>
    <span style="display: inline-block; margin-right: 20px;">
        <img src="https://getlogovector.com/wp-content/uploads/2020/10/vestiaire-collective-logo-vector.png" alt="Yelp Logo" width="100"/>
    </span>
</div>




### Overview
This repository contains all files related to the first project of the course Machine Learning for NLP. This project focuses on enhancing information retrieval on the NFCorpus dataset, a collection of medical abstracts from PubMed publications. The primary goal was to beat the performance of the baseline BM25 model. We also developped a custom TF-IDF based retrieval system and a Streamlit app to provide an interactive interface for users to retrieve relevant documents.
 
## Table of Contents
- [Files](#files)
- [Installation](#installation)
- [Project Highlights](#project-highlights)
- [Data Collection and Preparation](#data-collection-and-preparation)
- [Contributors](#contributors)
  
## Files

The project repository contains the following main files :

- **NLP_PROJECT2_KARUNATHASAN_SAMBATH.ipynb** : A Jupyter Notebook containing all the code generated for the project. (also accessible via the colab link)

- **app.py** : The Python script for the Streamlit app, which allows users to explore data insights, view sentiment analysis results, and interact with the QA system.


### Installation
Our interactive application allows users to explore data insights, view sentiment analysis results, and interact with the QA system. <br>
<br>
**Streamlit App** <br>
     **• Public Access** <br>
       You can acces the app through this link : https://project1nlpesilv.streamlit.app/ <br>
     **• Local Access** <br>
     - Clone this GitHub repository to your local machine using the following command: 
       ```
       git clone https://github.com/nilanyK/nlp_esilv.git
       ```
       <br>
     - Change to the project directory: 
       ```
       cd PROJECT2
       ```
       <br>
     - Run the Streamlit app by executing `app.py` : 
       ```python
       streamlit run app.py
       ```
       <br>
     - The output will display the link on which the server is running.  Click on it if it doesn't directly open the link.
   <br>
   <br>

## Project Highlights

- **Marketplace Data Scraping**: Utilized web scraping functionalities for Vinted and Vestiaire Collective to gather diverse and up-to-date inventory information.

- **Nike Price Scraping**: Incorporated scraping functionalities to obtain the average price of Nike sneakers directly from the official Nike website.

- **Customized Search on Vinted and Vestiaire Collective**: Enhanced both data scraping to support specific searches with parameters such as gender, color, and size.

- **Carbon Footprint Estimation**: Calculated an approximate carbon footprint for each second-hand item using geopy and predefined emission rates.

- **Profit Calculation**: Provided users with profit calculation for each item by comparing the second-hand price with the average original Nike price.

- **Streamlit App (Coming Soon)**: The next step is to develop a Streamlit app to offer users a user-friendly interface for exploring second-hand Nike sneakers.

### Data Collection and Preparation
Data was scraped from Trustpilot and Yelp. Rigorous data cleaning and preparation were performed to ensure the quality and consistency of the dataset.

### Contributors
[KARUNATHASAN Nilany](https://www.linkedin.com/in/nilany-karunathasan-7b49691ba/) <br>
[SAMBATH Sïndoumady](https://www.linkedin.com/in/s%C3%AFndoumady-sambath-a7519a209/) <br>





