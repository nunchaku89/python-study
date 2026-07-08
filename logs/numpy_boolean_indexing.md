# NumPy Boolean Indexing

## 학습일

* 2026-07-08

## Goal

* Boolean Mask의 개념을 이해한다.
* Boolean Indexing을 이용하여 조건에 맞는 데이터를 추출한다.
* 여러 조건을 조합하여 데이터를 필터링하는 방법을 익힌다.
* NumPy와 Pandas의 필터링 방식이 동일한 개념임을 이해한다.

## Implementation

파일: `exercises/numpy_boolean_indexing.py`

구현 내용

* 90점 이상인 점수를 추출했다.
* 80점 이상 90점 이하인 점수를 추출했다.
* 80점 미만인 점수를 추출했다.
* 평균 이상의 점수를 추출했다.
* 점수 배열의 Boolean Mask를 이름 배열에도 적용하여 90점 이상 학생의 이름을 추출했다.

핵심 학습

* 비교 연산의 결과는 Boolean 배열(True/False)로 반환된다.
* Boolean 배열을 인덱스로 사용하면 조건에 맞는 데이터만 선택할 수 있다.
* 하나의 Boolean Mask를 여러 배열에 동일하게 적용할 수 있다.
* 여러 조건을 사용할 때는 `&` 연산자와 괄호를 함께 사용해야 한다.

## Learned

* NumPy의 Boolean Indexing은 반복문 없이 조건 검색을 수행할 수 있는 강력한 기능이다.
* Boolean Mask는 데이터를 선택하는 '필터' 역할을 한다.
* `scores.mean()`과 같이 NumPy가 제공하는 메서드를 활용하면 코드가 더 간결하고 의미가 명확해진다.
* 중간 결과(Boolean Mask)를 변수로 저장하면 재사용성과 가독성이 향상된다.

## 실무 활용

* 특정 조건에 맞는 데이터만 조회하거나 분석할 때 가장 많이 사용하는 기능이다.
* 예를 들어 90점 이상 학생, 특정 금액 이상의 주문, 특정 날짜 이후의 로그, 일정 심박수 이상의 운동 기록 등을 추출하는 데 활용된다.
* 동일한 Boolean Mask를 여러 컬럼에 적용하여 관련 데이터를 함께 조회할 수 있다.

## Pandas 연결점

* NumPy의 `scores[scores >= 90]`은 Pandas의 `df[df["score"] >= 90]`과 동일한 개념이다.
* Boolean Indexing은 Pandas DataFrame Filtering의 기반이 되는 핵심 개념이다.
* NumPy에서 익힌 Boolean Mask는 Pandas에서도 거의 동일한 방식으로 사용된다.

## Next

* Pandas DataFrame 생성과 기본 구조를 이해한다.
* Boolean Mask를 이용하여 DataFrame에서 원하는 행만 필터링하는 방법을 학습한다.
