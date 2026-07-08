# NumPy Array

## 학습일

* 2026-07-08

## Goal

* NumPy의 `ndarray`를 생성하고 기본 연산을 수행한다.
* NumPy 배열과 Python 리스트의 차이를 이해한다.
* 배열 전체를 대상으로 연산하는 벡터화(Vectorization) 개념을 익힌다.

## Implementation

파일: `exercises/numpy_array.py`

구현 내용

* `np.array()`를 사용하여 점수 배열을 생성했다.
* 평균(`mean()`), 최대값(`max()`), 최소값(`min()`), 합계(`sum()`)를 계산했다.
* 모든 점수에 5점을 더하는 연산을 수행했다.
* 모든 점수를 10% 증가시키는 연산을 수행했다.
* 90점 이상 여부를 Boolean 배열로 확인했다.

핵심 학습

* NumPy 배열은 Python 리스트와 달리 배열 전체에 연산을 적용할 수 있다.
* `scores + 5`와 `scores * 1.1`처럼 반복문 없이 벡터 연산을 수행할 수 있다.
* 비교 연산의 결과는 `True`와 `False`로 이루어진 Boolean 배열로 반환된다.
* NumPy 연산은 원본 배열을 변경하지 않고 새로운 배열을 반환한다.

## Learned

* `ndarray`는 데이터 분석을 위한 핵심 자료구조이다.
* NumPy는 반복문보다 벡터 연산을 사용하는 것이 일반적이며 성능도 우수하다.
* Python의 내장 함수 대신 NumPy 메서드(`mean()`, `sum()` 등)를 사용하는 것이 권장된다.
* Boolean 배열은 이후 데이터 필터링의 핵심 역할을 한다.

## 실무 활용

* 대량의 수치 데이터를 반복문 없이 빠르게 계산할 수 있다.
* 데이터 정규화, 점수 보정, 센서 데이터 처리 등에서 벡터 연산이 자주 사용된다.
* Boolean 배열은 조건에 맞는 데이터만 선택하는 필터링의 기반이 되며, Pandas에서도 동일한 개념으로 활용된다.

## Pandas 연결점

* NumPy의 `scores >= 90`은 Pandas의 `df["score"] >= 90`과 동일한 개념이다.
* NumPy의 벡터 연산은 Pandas의 컬럼 연산으로 자연스럽게 이어진다.
* 이후 Boolean Indexing을 학습하면 NumPy와 Pandas에서 동일한 방식으로 데이터를 필터링할 수 있다.

## Next

* NumPy의 Boolean Indexing을 학습한다.
* 같은 개념을 Pandas의 DataFrame Filtering에 적용하여 두 라이브러리의 공통된 데이터 처리 방식을 이해한다.
