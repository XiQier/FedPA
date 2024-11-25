import pandas as pd
import os
import csv
from sklearn.model_selection import train_test_split

# 读取 CSV 文件
df = pd.read_csv('./dataset/KuaiRand-Pure/new_user_features.csv')

df = df[['user_id', 'follow_user_num']]

df1 = pd.read_csv('./dataset/KuaiRand-Pure/new_video_features.csv')
df1 = df1[['video_id']]
df.to_csv('./new_user_features.csv', index=False)
df1.to_csv('./new_video_features.csv', index=False)
#
# train_data_dir = './dataset/KuaiRand-Pure/data_divide/private_users_random_0.6_0.2_train.csv'
# val_data_dir = './dataset/KuaiRand-Pure/data_divide/private_users_random_0.6_0.2_val.csv'
# test_data_dir = './dataset/KuaiRand-Pure/data_divide/private_users_random_0.6_0.2_test.csv'
#
# df = df[['user_id', 'video_id', 'is_click']]
# # 随机划分数据集
# train_val_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
# train_df, val_df = train_test_split(train_val_df, test_size=0.25, random_state=42)
#
# # 保存到新的 CSV 文件
# train_df.to_csv(train_data_dir, index=False)
# val_df.to_csv(val_data_dir, index=False)
# test_df.to_csv(test_data_dir, index=False)
# os.makedirs('./dataset/KuaiRand-Pure/_selected_user_feature_dict.txt',exist_ok=True)
# os.makedirs('./dataset/KuaiRand-Pure/_selected_video_feature_dict.txt',exist_ok=True)
