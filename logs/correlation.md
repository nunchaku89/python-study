# Visualization - Correlation Analysis

## 학습일

* 2026-07-13

## Goal

* 상관계수(Correlation Coefficient)를 계산하는 방법을 학습한다.
* 상관관계와 인과관계의 차이를 이해한다.
* Scatter Plot과 상관계수를 함께 해석하는 방법을 익힌다.

## Implementation

파일

* `exercises/correlation.py`

구현 내용

* `Series.corr()`를 이용하여 공부 시간과 시험 점수의 상관계수를 계산하였다.
* `DataFrame.corr()`를 이용하여 운동 시간과 체지방률의 상관관계 행렬을 확인하였다.
* 상관계수를 바탕으로 양의 상관관계와 음의 상관관계를 해석하였다.

## 핵심 학습

* 상관계수는 두 변수 간의 선형 관계를 -1에서 1 사이의 값으로 표현한다.
* `Series.corr()`는 두 변수의 상관계수를 계산한다.
* `DataFrame.corr()`는 여러 변수의 상관관계를 한 번에 계산한다.
* Scatter Plot은 관계를 시각적으로 확인하고, 상관계수는 이를 수치로 표현한다.

## Learned

* 상관관계가 높더라도 인과관계를 의미하지 않는다.
* 분석 결과는 데이터가 보여주는 사실과 분석자의 해석을 구분해야 한다.
* 상관관계는 변수 간의 관계를 탐색하는 도구이며, 원인을 증명하는 도구는 아니다.

## 프로젝트 적용

현재 Student Score Analysis 프로젝트에는 연속형 변수가 부족하여 상관관계 분석을 적용하기 어렵다.

향후 Sales Analysis와 Public Data Analysis 프로젝트에서는 상관관계 분석과 Scatter Plot을 함께 활용할 예정이다.

## 실무 활용

상관관계 분석은 다음과 같은 상황에서 자주 사용된다.

* 광고비와 매출
* 공부 시간과 시험 점수
* 운동 시간과 체지방률
* 기온과 전력 사용량

## Next

Line Chart를 이용하여 시계열(Time Series) 데이터를 시각화한다.
