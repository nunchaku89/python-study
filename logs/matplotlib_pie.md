# Visualization - Pie Chart

## 학습일

* 2026-07-13

## Goal

* Pie Chart를 이용하여 데이터의 구성비를 시각화한다.
* `value_counts()` 결과를 그래프로 표현하는 방법을 학습한다.
* Pie Chart와 Bar Chart의 차이점을 이해한다.

## Implementation

파일

* `exercises/matplotlib_pie.py`

구현 내용

* 전공별 학생 수를 이용하여 Pie Chart를 생성하였다.
* `labels` 옵션으로 각 전공명을 표시하였다.
* `autopct`를 이용하여 비율을 표시하였다.
* `startangle`을 이용하여 그래프의 시작 위치를 조정하였다.
* Student Score Analysis 프로젝트의 `value_counts()` 결과를 이용하여 자동으로 Pie Chart를 생성하였다.

## 핵심 학습

* Pie Chart는 전체 대비 비율을 표현하는 그래프이다.
* `value_counts()` 결과를 바로 Pie Chart에 사용할 수 있다.
* Pie Chart는 구성비를 표현할 때 효과적이다.
* 데이터가 변경되어도 그래프가 자동으로 갱신되는 구조를 구현하였다.

## Learned

* Pie Chart는 범주의 비율을 직관적으로 표현한다.
* 범주가 많아질수록 Pie Chart의 가독성이 떨어질 수 있다.
* 정확한 수치 비교에는 Bar Chart가 더 적합하다.
* 목적에 맞는 그래프를 선택하는 것이 중요하다.

## 프로젝트 적용

Student Score Analysis 프로젝트에서

* 전공별 학생 비율을 Pie Chart로 시각화하였다.
* `value_counts()`와 Matplotlib를 연결하여 자동 시각화를 구현하였다.

## 실무 활용

Pie Chart는 다음과 같은 데이터를 표현할 때 자주 사용된다.

* 성별 비율
* 연령대 비율
* 지역별 고객 비율
* 브라우저 점유율
* 전공별 학생 비율

## Next

Scatter Plot을 이용하여 두 변수 간의 관계를 시각화한다.
