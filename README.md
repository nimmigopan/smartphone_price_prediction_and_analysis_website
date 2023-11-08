# smartphone_price_prediction_and_analysis_website

Steps:-
## [1] Web Scraping using 'Selenium'
- "web_scrapping_using_selenium.py" contain code to scrape the HTML content of a web page "smartprix.com", including potentially dynamically loaded content through a "Load More" mechanism.
It utilizes Selenium for web automation to interact with the webpage and extract the desired data.
#### What is Smartprix.com?
"Smartprix.com" an Indian online Shopping Comparison site that provides the latest gadgets including mobiles, laptops, electronics, TVs, home appliances, and audio products, and their prices across various 
online shopping websites like Amazon, Flipkart, Samsung, Croma etc. In this project, data related to smartphones are scrapped using 'selenium'.
#### What is Selenium?
"Selenium" is a Python library and framework used for web automation and web scraping. It is used to automate interactions with a web page, such as navigating to the site, clicking on elements, and scraping its content, which is often used for web scraping and data extraction tasks. Here Selenium is used to interact with a web browser and perform actions on 'https://www.smartprix.com/mobiles' to extract data from this website.
- The scraped HTML is saved to a file 'smartphone.html' for further processing or analysis.

**"Converting 'smartphone.html' to 'scraped_data.csv'.ipynb"** file contain code to convert scrapped data to store in a Pandas DataFrame and CSV file.
- BeautifulSoup is used to parse the HTML content. BeautifulSoup is a Python library used for parsing HTML and XML documents.
- The code extracts various pieces of information from each container, such as the smartphone model name, price, and rating. It also handles cases where the rating is missing by using a try-except block.
- After extracting the data for multiple smartphones, the code uses the Pandas library to create a DataFrame with columns for each type of information.
- Finally, the code saves the DataFrame to a CSV file named 'scraped_data.csv'. This CSV file contains the scraped data in a structured format.
- The result is a DataFrame with information about smartphones, including their model names, prices, ratings, and detailed specifications. This data is stored in a CSV file for further analysis or use.
   
![uncleaned scrapped data](https://github.com/nimmigopan/smartphone_price_prediction_and_analysis_website/assets/35449494/119499b9-4b04-4f45-a333-0c8200ea1523)

- model: The name or model of the smartphone.
- price: The price of the smartphone in Indian Rupees (₹).
- rating: The rating of the smartphone.
- sim: Information about the SIM card options and connectivity features.
- processor: Details about the smartphone's processor, including the model and core specifications.
- ram_rom: Information about the RAM (Random Access Memory) and ROM (Internal Storage) of the smartphone.
- battery: Details about the smartphone's battery, including capacity and fast charging support.
- display: Information about the smartphone's display, including size, resolution, and features.
- camera: Details about the smartphone's camera setup, including rear and front camera specifications.
- memory_card: Information about memory card support, including the maximum capacity.
- operating_system: The operating system running on the smartphone.

   
 ## [2] Data Cleaning
   Performed Data Cleaning at different levels.

**"working on 'scraped_data.csv' to 'cleaned_data1.csv'.ipynb"** :-Basic data Accessing of 'scraped_data.csv' by using pandas library.
- head(), shape
- Removing Unnecessary columns
- Checking information about the DataFrame using info()
- Checking Missing Values using isnull().sum()
- Check for duplicate rows using the duplicated().sum() method and remove them with the drop_duplicates() method.
- Convert 'price' column to integer values instead of strings.
- Removed rows where the 'price' is less than 3500, assuming these are feature phones.
- Cleaned Dataframe saved to 'cleaned_data1.csv' using the to_csv() method.
- The result is a cleaned dataset containing smartphone data without duplicate rows, with the 'price' column converted to integers, and only smartphones with prices greater than 3500.

**Working on 'cleaned_data1.csv'.ipynb"** :-
- removed some more feature phones by manual data accessing
- checked each columns and noted down if any validity, completeness, tidness and consistent issues are there
- performed some shifting operations to solve validity issues
- some manual fillings are done in place of missing values
- after the first level of cleaning, tidiness issue still remains
- data stored to 'cleaned_data2.csv'

**"Working on 'cleaned_data2.csv'.ipynb"** :-
- Created new column 'brand_name' from 'model' using string functions (str.split(), str.get())
- Created new binary columns ('has_dual_sim,' 'has_5G,' 'has_NFC,' 'has_IR_Blaster') to represent the features present in the 'sim' column.
- Extracted information from the 'processor' column into four new columns: 'processor_name,' 'processor_brand,' 'no_of_cores,' and 'processor_speed.'
- Addressed missing and inconsistent values in the 'no_of_cores' column.
- Converted the 'processor_speed' column to float and handled missing values.
- Splitted the 'ram_rom' column into 'ram' and 'rom' columns.
- Handled the missing values and converted the columns into appropriate data types.
- Created a 'fast_charging_available' column to indicate whether fast charging is supported.
- Extracted the battery capacity information.
- Extracted information about screen size, resolution, and refresh rate into separate columns.
- Created new columns for the number of rear and front cameras, as well as primary rear and front camera resolutions from 'camera' column.
- Created a new column 'extended_memory_available' to indicate whether extended memory support is available.
- Extracted the 'memory extended upto' information and handled missing values.
- Standardized operating system versions and addressed various data validity issues.
- Converted appropriate columns to the desired data types, such as integer or float.
- Second level cleaned DataFrame is saved to a new CSV file named 'cleaned_data3.csv'.

**Working on 'cleaned_data3.csv'.ipynb"** :-
- In this level i focused on making the dataset more concise and manageable for further analysis, which involves categorizing and simplifying certain features.
- Categorized the operating systems into two main categories: 'Android' and 'iOS. Now there is only these two categories.
- Brands with more than one occurrence are kept, while brands with only one phone are removed from the dataset.
- Simplified the 'pixels_in_width' and 'pixels_in_height' columns into a single 'resolution' category. The 'resolution' column is created by applying the 'resolution' function, which categorizes screen 
   resolutions into different categories like 'FWVGA,' 'HD,' 'Full HD,' etc.
- Droped unnecessary columns such as 'pixels_in_width,' 'pixels_in_height,' 'total_no_of_cameras,' and 'extended_memory_available' to simplify the dataset.
- The final cleaned dataset is saved to a new CSV file named 'final_cleaned_data.csv'.

## [3] EDA, Feature Engineering

   **"Performing EDA & missing value imputation.ipynb"**
- Performed Exploratory Data Analysis (EDA) on the dataset, which involves analyzing the relationships between various columns and the target column 'price.'
- Various Univariate and Bivariate analysis are done that provides valuable insights into the relationships and distributions within the dataset.
- The final dataset is saved to a new CSV file named 'final_data_for_modelling.csv'.

  ![cleaned data](https://github.com/nimmigopan/smartphone_price_prediction_and_analysis_website/assets/35449494/aa399b5f-6780-4b8b-8cfe-22955149d029)

## [4] Analytics Module
- After data gathering, Cleaning and Preprocessing, now data is ready for modelling.
- Streamlit is used to create a web application for data visualization and analysis. 
- Imports necessary libraries and sets up the Streamlit page configuration.
- Used Seaborn and Matplotlib to create several visualizations, including bar plots, scatter plots, and a combination of brand, processor brand, RAM, ROM, refresh rate, screen resolution, and processor speed 
   vs. price.
- Displayed these visualizations using the st.pyplot() function within Streamlit columns and subheaders.
- This visualization is providing insights into how various features are related to the price of mobile phones.

  some sample visualizations are shown below:
  
![overall analysis](https://github.com/nimmigopan/smartphone_price_prediction_and_analysis_website/assets/35449494/f952bdf9-6a8c-4355-ae50-4ba9f846f7de)


## [5] ML Model Selection
**Model Selection.ipynb"**
- Imported necessary libraries and modules for building predictive models, including NumPy, pandas, and scikit-learn's various tools.
- Loaded dataset using pd.read_csv.
- Splitted your dataset into training and testing sets using the train_test_split function from scikit-learn.
- Prepared the feature matrix (X) and the target variable (y).
- Transformed the target variable using np.log1p (logarithmic transformation) to improve its distribution.
- Created a ColumnTransformer and a preprocessing pipeline. The preprocessing pipeline includes standard scaling for numerical features and one-hot encoding and ordinal encoding.
- Imported various regression models, including Linear Regression, Ridge, RidgeCV, Lasso, Decision Tree, Random Forest, Gradient Boosting, AdaBoost, Extra Trees, Support Vector Machine (SVR), and XGBoost. These 
   models can be used to predict the 'price' of phones.
- Imported the 'mean_absolute_error' function from scikit-learn's metrics module. This metric measures the mean absolute difference between the predicted and actual values. It is used to assess the performance 
   of regression models.
-  Definined a function that assesses the performance of different machine learning models using K-fold cross-validation and returns a DataFrame with model names, R-squared scores, and MAEs.
- The model with maximium R2 score and minimum 'mae' is selected.
- "Random Forest Regressor" is selected.
- Created a pipeline that includes preprocessing and the Random Forest Regressor.
- Saved the preprocessing pipeline and the trained model into separate pickle files ('pipeline.pkl' and 'df.pkl').

## [6] Prediction Module
- Built a Streamlit application for price prediction based on various mobile phone specifications.
- If You fill input fields for different phone specifications, and upon clicking the "predict" button, by using the trained model, the phone's price is estimated.
- The application allows users to input various phone specifications, such as brand, dual SIM, 5G support, NFC support, IR blaster, processor brand, number of cores, processor speed, RAM, ROM, fast charging availability, battery capacity, screen size, screen resolution, refresh rate, number of rear and front cameras, primary camera pixels, memory extended up to, and operating system. After inputting these details, users can click the "predict" button to receive a predicted price for the specified phone.


![price prediction module](https://github.com/nimmigopan/smartphone_price_prediction_and_analysis_website/assets/35449494/3bd74d9a-44c7-4474-9dff-8bbf4b7324c8)



