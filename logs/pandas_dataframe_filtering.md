# Pandas DataFrame Filtering

## 학습일

* 2026-07-08

## Goal

* Pandas DataFrame의 구조를 이해한다.
* 원하는 컬럼을 선택하는 방법을 익힌다.
* Boolean Filtering을 이용하여 조건에 맞는 데이터를 조회한다.
* NumPy의 Boolean Indexing과 Pandas Filtering의 공통점을 이해한다.

## Implementation

파일: `exercises/pandas_dataframe_filtering.py`

구현 내용

* 학생 정보를 DataFrame으로 생성했다.
* 90점 이상 학생을 조회했다.
* CS 전공 학생을 조회했다.
* 평균 이상 학생을 조회했다.
* OR(`|`) 조건을 이용하여 Math 전공 또는 90점 이상 학생을 조회했다.
* 상품 데이터를 DataFrame으로 생성하고 재고 여부와 가격 조건을 이용하여 원하는 상품을 조회했다.

핵심 학습

* DataFrame은 행(Row)과 열(Column)로 구성된 표 형태의 자료구조이다.
* `df["column"]`을 이용하여 특정 컬럼을 선택할 수 있다.
* Boolean 조건을 이용하면 원하는 행만 필터링할 수 있다.
* 여러 조건을 사용할 때는 `&`, `|`와 괄호를 함께 사용해야 한다.

## Learned

* Pandas의 Filtering은 NumPy의 Boolean Indexing과 동일한 사고방식으로 동작한다.
* 컬럼에 대해 비교 연산을 수행하면 Boolean Series가 생성된다.
* Boolean Series를 DataFrame의 인덱스로 사용하면 조건에 맞는 데이터만 조회할 수 있다.
* 평균과 같은 집계 함수(`mean()`)를 조건과 함께 사용할 수 있다.

## 실무 활용

* 특정 조건에 맞는 고객, 상품, 주문, 로그 데이터를 조회할 때 가장 많이 사용하는 기능이다.
* 조건을 변수로 분리하면 코드의 가독성과 재사용성이 향상된다.
* DataFrame Filtering은 데이터 분석과 전처리 과정의 핵심 기능이다.

## NumPy 연결점

* NumPy의 `scores[scores >= 90]`은 Pandas의 `df[df["score"] >= 90]`과 동일한 개념이다.
* NumPy에서는 배열(Array)을 필터링하고, Pandas에서는 DataFrame의 행(Row)을 필터링한다.
* Boolean Mask를 이용한 데이터 선택 방식은 두 라이브러리에서 공통적으로 사용된다.

## Next

* Pandas에서 새로운 컬럼(Column)을 생성하고 수정하는 방법을 학습한다.
* 벡터 연산을 이용하여 반복문 없이 데이터를 변환하는 방법을 익힌다.
