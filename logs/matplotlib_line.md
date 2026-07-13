# Visualization - Line Chart

## 학습일

* 2026-07-13

## Goal

* Line Chart를 이용하여 시간에 따른 데이터의 변화를 시각화한다.
* 추세(Trend)를 해석하는 방법을 학습한다.
* 시계열(Time Series) 데이터에 적합한 그래프를 이해한다.

## Implementation

파일

* `exercises/matplotlib_line.py`

구현 내용

* 월별 매출 데이터를 Line Chart로 시각화하였다.
* `marker`와 `linewidth` 옵션을 사용하여 가독성을 높였다.
* 운동 기록(주차별 체중 변화)을 Line Chart로 시각화하였다.
* 제목과 축 이름을 추가하고 `tight_layout()`으로 레이아웃을 정리하였다.

## 핵심 학습

* Line Chart는 시간의 흐름에 따른 데이터 변화를 표현하는 그래프이다.
* `marker`를 사용하면 각 데이터 지점을 쉽게 확인할 수 있다.
* `linewidth`를 조정하여 그래프의 가독성을 높일 수 있다.
* 시간에 따른 증가, 감소, 유지 등의 추세를 쉽게 파악할 수 있다.

## Learned

* Bar Chart는 범주를 비교하는 데 적합하다.
* Histogram은 데이터 분포를 확인하는 데 적합하다.
* Pie Chart는 전체 대비 비율을 표현하는 데 적합하다.
* Scatter Plot은 변수 간의 관계를 확인하는 데 적합하다.
* Line Chart는 시간에 따른 추세를 분석하는 데 적합하다.
* 데이터의 특성에 따라 적절한 그래프를 선택하는 것이 중요하다.

## 프로젝트 적용

Student Score Analysis 프로젝트에는 시간 정보가 없어 직접 적용하기 어렵다.

향후 Sales Analysis 프로젝트에서 월별 매출과 같은 시계열 데이터를 시각화하는 데 활용할 예정이다.

## 실무 활용

Line Chart는 다음과 같은 데이터를 분석할 때 자주 사용된다.

* 월별 매출
* 일별 방문자 수
* 주간 운동 기록
* 주가 변화
* 서버 응답 시간 변화

## Next

Sales Analysis 프로젝트를 시작하여 지금까지 학습한 분석 및 시각화 기법을 종합적으로 적용한다.
