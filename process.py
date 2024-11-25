import pandas as pd
import os
import csv
from sklearn.model_selection import train_test_split

# 读取 CSV 文件
df = pd.read_csv('./KuaiRand-Pure/data/log_standard_4_22_to_5_08_pure.csv')

train_data_dir = './dataset/KuaiRand-Pure/data_divide/private_users_random_0.6_0.2_train.csv'
val_data_dir = './dataset/KuaiRand-Pure/data_divide/private_users_random_0.6_0.2_val.csv'
test_data_dir = './dataset/KuaiRand-Pure/data_divide/private_users_random_0.6_0.2_test.csv'

df = df[['user_id', 'video_id', 'is_click']]
# 随机划分数据集
train_val_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
train_df, val_df = train_test_split(train_val_df, test_size=0.25, random_state=42)

# 保存到新的 CSV 文件
train_df.to_csv(train_data_dir, index=False)
val_df.to_csv(val_data_dir, index=False)
test_df.to_csv(test_data_dir, index=False)
os.makedirs('./dataset/KuaiRand-Pure/_selected_user_feature_dict.txt',exist_ok=True)
os.makedirs('./dataset/KuaiRand-Pure/_selected_video_feature_dict.txt',exist_ok=True)
