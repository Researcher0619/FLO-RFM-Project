# FLO-RFM Project
 RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
Business Problem
FLO wants to divide its customers into segments and determine marketing strategies according to these segments. For this purpose, the behaviors of the customers will be defined and groups will be formed according to these behavior clusters.

Dataset Story
The dataset consists of information obtained from the past shopping behaviors of customers who made their last purchases as OmniChannel (both online and offline shopper) in 2020 - 2021.

Variables
   ## master_id: Unique client number
   ## order_channel : Which channel of the shopping platform is used (Android, ios, Desktop, Mobile, Offline)
   ## last_order_channel : The channel where the last purchase was made
   ## first_order_date : Date of the customer's first purchase
   ## last_order_date : The date of the customer's last purchase
   ## last_order_date_online : The date of the last purchase made by the customer on the online platform
   ## last_order_date_offline : The date of the last purchase made by the customer on the offline platform
   ## order_num_total_ever_online : The total number of purchases made by the customer on the online platform
   ## order_num_total_ever_offline : Total number of purchases made by the customer offline
   ## customer_value_total_ever_offline : The total price paid by the customer for offline purchases
   ## customer_value_total_ever_online : The total price paid by the customer for their online shopping
   ## interested_in_categories_12 : List of categories the customer has shopped in the last 12 months
   
   
TASKS
TASK 1: Data Understanding and Preparation
        # 1. Read the flo_data_20K.csv data.
        #2. In the dataset
                  # a. top 10 observations,
                  # b. variable names,
                  # c. descriptive statistics,
                  # D. null value,
                  # e. Variable types, review.
        # 3. Omnichannel means that customers shop from both online and offline platforms. Total for each customer
        # create new variables for number of purchases and spend.
        # 4. Examine the variable types. Change the type of variables that express date to date.
        # 5. Look at the breakdown of the number of customers, average number of products purchased, and average spend in shopping channels.
        # 6. Rank the top 10 customers with the most revenue.
        # 7. Rank the top 10 customers with the most orders.
        # 8. Functionalize the data provisioning process.
TASK 2: Calculating RFM Metrics
TASK 3: Calculating RF and RFM Scores
TASK 4: Segment Definition of RF Scores
TASK 5: Time for action!
        # 1. Examine the recency, frequency and monetary averages of the segments.
        # 2. With the help of RFM analysis, find the customers in the relevant profile for 2 cases and save the customer IDs to the csv.
                # a. FLO includes a new women's shoe brand. The product prices of the brand it includes are above the general customer preferences. Therefore, the brand
                It is desired to contact the customers in the profile that will be interested in # promotion and product sales. From their loyal customers(champions,loyal_customers),
                # People who shop from the women category with an average of 250 TL or more are the customers who will be contacted privately. Id numbers of these customers to csv file
                # save as new_brand_target_customer_id.cvs.
                # b. Up to 40% discount is planned for Men's and Children's products. Good past customer but long-standing customer interested in categories related to this sale
                # customers who should not be lost who do not shop, those who are asleep and new customers are specifically targeted. Enter the ids of the customers in the appropriate profile into the csv file discount_target_customer_ids.csv
                Save it as #.


