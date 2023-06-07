# Python765Final

## Habiba Aziz | Final Project
## Introduction to Computational Social Science
Can HDI and GDP levels be used as criteria to check which countries are more susceptible to cancer incidences/deaths? Can text data obtained from web scraping provide us an overview of public sentiment on cancer?

## Abstract
Cancer has no frontiers and no prejudices; it can happen to anyone when a single cell in a person’s body becomes abnormal (becomes genetically mutated). Scientists are still trying to pinpoint the root causes of this disease as well as a viable treatment. This study was conducted to look at the time series analysis of cancer incidences and deaths around the world based on GDP and HDI levels and to look at the present-day public perception about it. Data from ‘our world in data’ revealed that cancer incidences are unbiased of country, but the death rates are higher in developing countries. Additionally, 20 countries from the dataset, 10 developed and 10 developing were picked to see the incidence rates.  Decision tree classifier on cancer death rate by ages identified that the data was picked randomly. Text data scraped from google scholar articles demonstrated that from 2002 – 2017, only a handful of studies linking cancer with HDI and GDP were performed. Tweets from the present were used to understand the current public opinion on cancer.

## Introduction

Human Development Index (HDI) level is a scale that consists of a compound degree of pointers along three magnitudes: life expectancy, educational accomplishment, and availability of resources desirable for an adequate way of living. Gross Domestic Product (GDP) is mainly used to measure the healthiness of a country’s economy, and it is described as the financial value of merchandises and amenities produced in a country’s vicinity during an explicit period of time. Cancer is a disease that causes most of that cases of morbidity and mortality among patients in the world and these numbers keep on increasing as the years pass by (Bray et al. 2012). Disparities in the weight of cancer have been well-documented, and prior studies were focused on variances within countries, with an uneven load of prevailing cancers in countries categorized as high HDI, whereas infection related cancers remain to outweigh in countries with lower levels of HDI (Arnold et al.2017). Socioeconomic status is associated with cancer patients’ survival and it is vital to expand awareness of risk influences and primary detection (Ghoncheh and Mirzaei and Salehiniya 2012).   

## Analytical approach 

For this project, my objective was to check whether cancer incidences and death rates were related to HDI and GDP around the globe. Data sets were gathered from the website ‘Our world in data’, and later few datasets were merged using pandas dataframe in jupyter notebook (kernel python 3.6). Precautions were taken while merging the data sets, and data was cleaned for duplicate values in order to meet the criteria for time series analysis.  Cancer Incidences per 100,000 cases of neoplasm (A new and abnormal growth of tissue in some part of the body, which is considered a characteristic of cancer) from 2002 - 2017 was used to describe the population of the study. Furthermore, GDP, HDI, and cancer deaths for these years were analyzed using various visualization techniques that are discussed in the results section. Additionally, to get a clear idea on the relationship between cancer and HDI/GDP, data from 10 developed countries (Norway, Switzerland, Ireland, Germany, Australia, Iceland, United Kingdom, United States, Finland, and  Japan.) and 10 developing countries (Pakistan, Yemen, Liberia, Guinea, Congo, Mozambique, Afghanistan, Zimbabwe, Syria, and Iraq) was picked from the dataset based on UN HDI ranking-2019 to support the study. Moreover, correlation was applied on the desired dataset.
The dataset on cancer deaths by age was used to see the classification of cancer deaths for the 20 countries from 2002 - 2017.  A supervised machine learning technique named Decision Tree Classifier module from sklearn.tree was used to check the categorization of cancer deaths by age around those 20 countries over the period of 15 years.   
Web scraping techniques were used to mine data contained, which provided information about attributes based on a theme (Huanga, Morillo and Ferri 2019). About 100 pages of text data from google scholar ranging from 2002 - 2017 was mined using BeautifulSoup module, for research topics based on Cancer incidence/death and its relationship to HDI and GDP. Different modules from natural language toolkit (nltk) were used to clean the text data. LDA (Latent Dirichlet Allocation) topic model was applied on the filtered text data, number of topics, K were initially set as 20 with alpha value as 0.01 per 10 words and 20 topics were weighted.
SNA (Social Network Analysis) was carried out using tweets from Twitter using hashtags on cancer. Tweets were filtered using nltk modules, and a list of words with the most recurrence (co-occurring words/bigrams) was created. After this step, tweets were used to visualize network of bigrams. Furthermore, sentiment analysis on cancer tweets was observed to see cancer relationship with GDP and HDI.   

[Data 765-final-haziz.docx](https://github.com/habibaaziz/Python765Final/files/11672664/Data.765-final-haziz.docx)







