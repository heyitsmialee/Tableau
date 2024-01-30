# [DACON] Semiconductor thilnfilm thickness analysis

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

[https://dacon.io/competitions/official/235736/overview/description](https://dacon.io/competitions/official/235554/overview/description)

### ▪️Date :  2024.01.14 - 2024.01.21

### ▪️Leaderboard
▶ Public Score 

---
# 2. Project Outline

## ▪️대회 개요
> 반도체 공정 능력 향상을 위한 반도체 소자의 두께 분석 알고리즘 개발
> 각 데이터에는 *박막의 두께*와 *파장에 따른 반사율 스펙트럼* 이 존재함
> 
## ▪️평가 방법 : MAE(Mean Absolute Error)

## ▪️대회 데이터셋
> 소자의 4개 Layer 별 두께
> 각 Layer 별 반사율 스펙트럼, 빛의 파장

> Train.csv (122400,10)
> - layer 의미 : 질화규소(layer_1)/이산화규소(layer_2)/질화규소(layer_3)/이산화규소(layer_4)
> - layer_1~4: 해당 박막의 두께
> - 0~225: 반사율 스펙트럼, 빛의 파장

> Test.csv (10080, 9)
> - id: 스펙트럼의 아이디
> - 0~225: 반사율 스펙트럼, 빛의 파장

> Sample_submission.csv (10080, 2)
> - id: 스펙트럼의 아이디
> - layer_1~4: 해당 박막의 두께


## ▪️전처리

## ▪️모델

## ▪️결과

---
#3. Discussion

---
#4. Reference
