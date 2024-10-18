# -*- coding: utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 데이터 로드 (캐시 사용)
@st.cache_data
def load_data():
    train = pd.read_csv('./dataset/train.csv')
    return train

def main():
    # 페이지 제목 
    st.title("Loan Prediction Dashboard")

    data = load_data()

    # 데이터프레임 생성
    st.subheader("Dataset")
    st.dataframe(data.head())

    # 데이터 요약
    st.subheader("Data Summary")
    st.write(data.describe())

    # 대출 목적 분포
    st.subheader("대출 목적 분포")

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=data, x='loan_intent', ax=ax, color='skyblue')
    ax.set_title('Loan Intent Distribution')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # x축 레이블 회전

    # Streamlit에 그래프 출력
    st.pyplot(fig)

    # 대출 등급별 연체율 
    st.subheader("대출 등급별 연체 횟수")
    
    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(8, 6))

    # loan_grade에 따라 loan_status에 대한 countplot
    sns.countplot(data=data, x='loan_grade', hue='loan_status', ax=ax)
    ax.set_title('Loan Default Rate by Loan Grade', fontsize=16)
    ax.legend(title='Loan Status', labels=['Approved', 'Rejected'])

    # 그래프 출력
    st.pyplot(fig)
   
    # 신용 등급별 대출 상태 분포
    st.subheader("신용 등급별 대출 상태 분포 (박스플롯)")

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(8, 6))

    # 박스플롯 그리기: 대출 등급별로 대출 금액의 분포를 loan_status에 따라 나눔
    sns.boxplot(data=data, x='loan_grade', y='loan_amnt', hue='loan_status', ax=ax)

    # 그래프 제목 및 레이블 설정
    ax.set_title('Loan Amount Distribution by Loan Grade and Status', fontsize=15)
    ax.set_xlabel('Loan Grade', fontsize=10)
    ax.set_ylabel('Loan Amount', fontsize=10)
    
    # 그래프 출력
    st.pyplot(fig)
        

if __name__ == "__main__":
    main() 

