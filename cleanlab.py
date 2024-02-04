import csv
import os
import pandas as pd
import numpy as np

# !pip install "cleanlab[all]"
# [cleanlab documentation] https://docs.cleanlab.ai/stable/index.html
from cleanlab.filter import find_label_issues
from cleanlab.dataset import health_summary

os.environ["TOKENIZERS_PARALLELISM"] = "false"  # 병렬처리 off (warning 제거)


def health_summary(data, dataset_test) :
    """
        data (dataframe) : 원본 train (before inference)
        dataset_test (dataframe) : output (after inference)    
    """
    
    class_names=[0,1,2,3,4,5,6]
    health_summary(data['target'], np.array(dataset_test['probs']), class_names=class_names)
    
    

def find_label_issues(data, dataset_test, csv_file):
    """
        data (dataframe) : 원본 train (before inference)
        dataset_test (dataframe) : output (after inference). probs를 저장하는 코드로 baseline 수정 필요
        csv_file (str) : label issues 결과를 저장할 csv 파일 이름        
    """
    
    ordered_label_issues = find_label_issues(
        labels=data['target'],  # 데이터셋 라벨
        pred_probs=np.array(dataset_test['probs']),  # 정답 예측 확률
        return_indices_ranked_by='self_confidence',
    )

    # write mode로 csv 파일 open
    with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csvwriter = csv.writer(csvfile)

        if os.stat(csv_file).st_size == 0:
            csvwriter.writerow(['text', 'target(raw)', 'target(predict)'])

        for issue in ordered_label_issues:
            row_data = [
                dataset_test.iloc[issue]['text'],
                data.iloc[issue]['target'],
                dataset_test.iloc[issue]['target']
            ]
            csvwriter.writerow(row_data)


def main():
    csv_file = "mis_labeling.csv"               # label issues 결과를 저장할 csv 파일
    data = pd.read_csv("train.csv")             # 원본 train csv 파일
    dataset_test = pd.read_csv("output.csv")    # train csv evaluate 파일
    find_label_issues(data, dataset_test, csv_file)
    health_summary()
  
  
if __name__ == '__main__':
  main()