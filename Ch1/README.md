# [DACON] 전력사용량 예측 AI 경진대회

--- 
# Index
[1. Introduction]()   
[2. Project Outline]()   
[3. Usage & Reproduction]()   
[4. Directory Structure]()   
[5. References]()     
[6. Retrospect]()    

---
# 1. Introduction

https://dacon.io/competitions/official/235736/overview/description

### ▪️Date :  2024.01.21 - 2024.01.28

### ▪️Leaderboard
▶ Public Score 

---
# 2. Project Outline

## ▪️대회 개요
> 건물 정보와 기후 정보를 활용한 전력사용량 예측
> 각 데이터에는 *num*, *date_time*,*기온(°C)*, *풍속(m/s)*, *습도(%)*, *강수량(mm)*,*일조(hr)*, *비전기냉방설비운영*, *태양광보유* 존재

## ▪️평가 방법 : SMAPE

## ▪️대회 데이터셋
> 60개의 건물들의 2020년 6월 1일부터 2020년 8월 31일까지의 데이터

> Train.csv (122400,10)
> - num : 건물번호
> - date_time : 60개 건물들의 2020년 6월 1일 부터 2020년 8월 24일까지의 데이터 (1시간 단위)
> - 전력사용량(kWh)
> - 기온(°C)
> - 풍속(m/s)
> - 습도(%)
> - 강수량(mm)
> - 일조(hr)
> - 비전기냉방설비운영
> - 태양광보유

> Test.csv (10080, 9)
> - num : 건물번호
> - date_time : 60개 건물들의 2020년 8월 25일 부터 2020년 8월 31일까지의 데이터 (3시간 단위)
> - 기온(°C)
> - 풍속(m/s)
> - 습도(%)
> - 강수량(mm, 6시간) : 강수량은 6시간 단위로 제공
> - 일조(hr, 3시간)
> - 비전기냉방설비운영
> - 태양광보유

> Sample_submission.csv (10080, 2)
> - num_date_time : 건물번호+시간
> - answer : 전력사용량 예측량


## ▪️전처리

## ▪️모델

## ▪️결과

---
#3. Discussion

---
#4. Reference



