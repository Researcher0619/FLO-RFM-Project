import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_csv("Datasets/flo_data_20k.csv")
df_ = df.copy()


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)

    print("##################### Types #####################")
    print(dataframe.dtypes)

    print("##################### Head #####################")
    print(dataframe.head(head))

    print("##################### Tail #####################")
    print(dataframe.tail(head))

    print("##################### NA #####################")
    print(dataframe.isnull().sum())

    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    print(dataframe.describe().T)


check_df(df)

import datetime as dt

df["order_num_total_ever_both"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df.head()
df["customer_value_total_ever_both"] = df["customer_value_total_ever_online"] + df["customer_value_total_ever_offline"]
df.head()


df.describe().T
df["order_channel"].nunique()
df.columns

df.columns

A = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]
df[A] = df[A].apply(pd.to_datetime)

df.groupby(["order_channel", "interested_in_categories_12"]).agg({"order_num_total_ever_both": lambda x: x.sum(),
                                                                  "customer_value_total_ever_both": lambda x: x.sum(),
                                                                  "master_id": lambda x: x.sum()}).head(10)

# En fazla kazancı getiren ilk 10 müşteri(top 10 customers with the most profits):

df[["master_id", "customer_value_total_ever_both"]].sort_values(by="customer_value_total_ever_both").head(10)

# En fazla siparişi veren ilk 10 müşteriyi(Top 10 customers with the most orders)

df[["master_id", "order_num_total_ever_both"]].sort_values(by="order_num_total_ever_both").tail(10)


# Veri ön hazırlık sürecini fonksiyonlaştırınız(Functioning of data preparation process).

def veriyi_hazirlama(Dataframe ):
    Dataframe["order_num_total_ever_both"] = Dataframe["order_num_total_ever_online"] + Dataframe[
        "order_num_total_ever_offline"]


    Dataframe["customer_value_total_ever_both"] = Dataframe["customer_value_total_ever_online"] + Dataframe["customer_value_total_ever_offline"]





    Dataframe.describe().T

    Dataframe["order_channel"].nunique()

    Dataframe.columns


    A = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]

    Dataframe[A] = Dataframe[A].apply(pd.to_datetime)


    Dataframe.groupby(["order_channel", "interested_in_categories_12"]).agg({"order_num_total_ever_both": lambda x: x.sum(), "customer_value_total_ever_both": lambda x: x.sum(), "master_id": lambda x: x.sum()}).head()

    # En fazla kazancı getiren ilk 10 müşteri(top 10 customers with the most profits):

    En_fazla_kazanc =Dataframe[["master_id", "customer_value_total_ever_both"]].sort_values(by="customer_value_total_ever_both", ascending=False).head(10)

    # En fazla siparişi veren ilk 10 müşteriyi (Top 10 customers with the most orders)

    En_fazla_siparis = Dataframe[["master_id", "order_num_total_ever_both"]].sort_values(by="order_num_total_ever_both", ascending=False).head(10)

    return Dataframe, En_fazla_kazanc, En_fazla_siparis


Dataframe, En_fazla_kazanc, En_fazla_siparis=veriyi_hazirlama(df_)

En_fazla_kazanc
Dataframe
En_fazla_siparis


#RFM Metriklerinin Hesaplanması / Calculating RFM Metrics

# Recency : Müşternin Sıcaklığı yani analizin yapıldığı tarih - ilgili müşterinin son satın alma yaptığı tarih
# Frequency : Müşterinin yaptığı toplam satın alma
# Monetary : Müşterinin yaptığı satın almalar neticesinde bıraktığı toplam parasal değerdir.

#Müşteri özelinde Recency, Frequency ve Monetary metriklerini / RFM Metrics for each customer
df["last_order_date"].max()
df.head()
today_date = dt.datetime(2021, 6, 1 )
type(today_date)

rfm = df.groupby("master_id").agg({"last_order_date": lambda last_order_date: (today_date - last_order_date.max()).days,
                                   "order_num_total_ever_both": lambda x: x.sum(),
                                   "customer_value_total_ever_both": lambda x: x.sum()})
rfm.head()
rfm.columns = ["recency", "frequency", "monetary"]
rfm.columns
rfm.shape

#Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çeviriniz.

rfm.describe().T


rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] =pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5])


rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))
rfm.head()



seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

#müşterilerinden(champions, loyal_customers) ve kadın kategorisinden alışveriş
# yapan kişiler özel olarak iletişim kurulacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına kaydediniz


new_product=pd.DataFrame()

df["master_id"].reset_index(inplace=True, drop=True)
rfm["segment"].reset_index(inplace=True, drop=True)
df["interested_in_categories_12"].reset_index(inplace=True, drop=True)

new_product=pd.concat([df["master_id"],rfm["segment"],df["interested_in_categories_12"]], axis=1)

new_product.to_csv("new_product.csv")
rfm.to_csv("rfm_oz.csv")

discount = rfm.loc[((rfm.segment == "hibernating") | (rfm.segment == "at_Risk") | (rfm.segment == "new_customers")), "segment"]