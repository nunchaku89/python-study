# NumPy Indexing & Slicing / Pandas loc & iloc

## 학습일

* 2026-07-08

## Goal

* NumPy 배열에서 Indexing과 Slicing을 사용할 수 있다.
* Pandas의 `iloc`과 `loc`의 차이를 이해한다.
* 위치(Position)와 라벨(Label)을 기준으로 데이터를 선택하는 방법을 익힌다.
* NumPy와 Pandas의 데이터 접근 방식이 연결되는 원리를 이해한다.

## Implementation

파일: `exercises/numpy_indexing.py`

구현 내용

* NumPy 배열에서 첫 번째, 마지막 요소를 조회했다.
* NumPy Slicing을 이용하여 원하는 범위의 데이터를 추출했다.
* 학생 데이터를 DataFrame으로 생성했다.
* `iloc`을 이용하여 특정 행과 특정 셀의 데이터를 조회했다.
* DataFrame의 인덱스를 변경한 후 `loc`과 `iloc`의 차이를 비교했다.

핵심 학습

* NumPy와 Python의 Slicing은 **시작 포함(Start Inclusive), 끝 제외(End Exclusive)** 규칙을 따른다.
* `iloc`은 행과 열의 **위치(Position)** 를 기준으로 데이터를 선택한다.
* `loc`은 **인덱스(Label)** 를 기준으로 데이터를 선택한다.
* DataFrame의 인덱스를 변경하면 `loc`과 `iloc`의 동작 방식이 달라진다.

## Learned

* NumPy 배열과 Pandas DataFrame은 모두 Indexing과 Slicing을 지원하지만 접근 기준이 다르다.
* `iloc[행, 열]` 문법을 이용하여 원하는 셀에 직접 접근할 수 있다.
* `loc`은 의미 있는 인덱스를 사용할 때 강력한 기능을 제공한다.
* 데이터 선택(Data Selection)은 이후 데이터 수정, 집계, 결합의 기초가 되는 핵심 기능이다.

## 실무 활용

* CSV나 데이터베이스에서 읽어온 데이터의 특정 행이나 범위를 선택할 때 사용한다.
* 고객 ID, 주문번호 등 의미 있는 인덱스를 설정한 후 `loc`으로 빠르게 데이터를 조회할 수 있다.
* `iloc`은 데이터 검증, 샘플 추출, 특정 위치 수정 등에 자주 활용된다.

## NumPy ↔ Pandas 연결점

| NumPy        | Pandas        |
| ------------ | ------------- |
| `scores[0]`  | `df.iloc[0]`  |
| `scores[:3]` | `df.iloc[:3]` |
| `scores[-1]` | `df.iloc[-1]` |
| 위치 기반 접근     | `iloc`        |
| 라벨 기반 접근     | `loc`         |

## Next

* NumPy와 Pandas의 통계 함수(`mean`, `median`, `max`, `min`, `std`)를 비교하며 데이터를 요약하는 방법을 학습한다.
