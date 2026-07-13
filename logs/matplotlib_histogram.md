# Visualization - Histogram

## 학습일

* 2026-07-13

## Goal

* 히스토그램(Histogram)의 목적과 활용 방법을 이해한다.
* 수치형 데이터의 분포를 시각적으로 확인하는 방법을 학습한다.
* Student Score Analysis 프로젝트에 점수 분포 그래프를 적용한다.

## Implementation

파일

* `exercises/matplotlib_histogram.py`

구현 내용

* `plt.hist()`를 이용하여 점수 분포를 시각화하였다.
* `bins` 옵션을 사용하여 데이터 구간을 조절하였다.
* 그래프 제목과 축 이름을 추가하였다.
* `tight_layout()`을 이용하여 레이아웃을 정리하였다.

## 핵심 학습

* Histogram은 범주 비교가 아니라 **데이터의 분포**를 확인하는 그래프이다.
* `bins` 값에 따라 데이터를 나누는 구간의 개수가 달라진다.
* `bins`가 커질수록 데이터의 세부 분포를 더 자세하게 확인할 수 있다.
* 데이터의 개수와 목적에 따라 적절한 `bins`를 선택하는 것이 중요하다.

## Learned

* Bar Chart와 Histogram은 목적이 다르다.
* Histogram을 통해 데이터가 어느 구간에 집중되어 있는지 확인할 수 있다.
* 점수 데이터에서는 성적이 특정 구간에 몰려 있는지 쉽게 파악할 수 있다.

## 프로젝트 적용

Student Score Analysis 프로젝트에서 `score` 컬럼을 이용하여 점수 분포 그래프를 생성할 수 있다.

향후 `score_distribution.png`를 자동 생성하도록 프로젝트를 확장할 예정이다.

## 실무 활용

Histogram은 다음과 같은 상황에서 자주 사용된다.

* 시험 점수 분포
* 고객 연령 분포
* 상품 가격 분포
* 주문 금액 분포
* 응답 시간(Response Time) 분포

## Next

Pie Chart를 이용하여 구성비를 시각화한다.
