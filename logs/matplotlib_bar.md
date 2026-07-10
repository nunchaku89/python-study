# Matplotlib Basics - Bar Chart

## 학습일

* 2026-07-08

## Goal

* Matplotlib의 기본 사용법을 익힌다.
* 막대그래프(Bar Chart)를 생성하는 방법을 학습한다.
* 분석 결과를 시각화하여 데이터의 특징을 직관적으로 표현한다.

## Implementation

파일

* `exercises/matplotlib_bar.py`

구현 내용

* Matplotlib를 이용하여 전공별 평균 점수를 막대그래프로 표현했다.
* 그래프 제목(`title`)을 추가했다.
* X축(`xlabel`)과 Y축(`ylabel`) 이름을 추가했다.
* Student Score Analysis 프로젝트의 `analyze()` 결과를 이용하여 그래프가 자동 생성되도록 구현했다.

## 핵심 학습

* `plt.bar()`를 이용하여 범주형 데이터를 시각화할 수 있다.
* `title()`, `xlabel()`, `ylabel()`을 이용하여 그래프의 가독성을 높일 수 있다.
* 분석 결과(`groupby()` 결과)를 그대로 그래프로 연결할 수 있다.
* 데이터가 변경되어도 그래프가 자동으로 갱신되는 구조를 만들 수 있다.

## Learned

* 표보다 그래프가 데이터의 차이를 더 직관적으로 보여준다.
* 시각화는 분석의 마지막 단계가 아니라 분석 결과를 전달하는 중요한 수단이다.
* 프로젝트에서 하드코딩된 값 대신 분석 결과를 사용하면 재사용성이 높아진다.

## 프로젝트 적용

Student Score Analysis 프로젝트에서

* `analyze()` → 분석 수행
* `create_report()` → 보고서 생성
* `Matplotlib` → 그래프 생성

의 흐름을 구성하였다.

## 개선 사항

다음 리팩터링에서 아래 기능을 추가할 예정이다.

* `plt.tight_layout()` 적용
* `plt.savefig()`를 이용한 그래프 저장
* `output/` 폴더에 결과 이미지 자동 생성

## 실무 활용

막대그래프는 다음과 같은 데이터를 비교할 때 가장 많이 사용된다.

* 부서별 평균 연봉
* 지역별 매출
* 카테고리별 주문 수
* 전공별 평균 점수

## Next

* Histogram을 이용하여 점수 분포를 시각화한다.
* Student Score Analysis 프로젝트에 분포 그래프를 추가한다.
