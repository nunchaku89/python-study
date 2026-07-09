# NumPy Broadcasting & Pandas Column Operations

## 학습일

* 2026-07-08

## Goal

* NumPy Broadcasting의 개념을 이해한다.
* Pandas에서 새로운 컬럼을 생성하는 방법을 익힌다.
* 기존 데이터를 이용하여 새로운 정보를 계산하는 방법을 학습한다.
* 반복문을 이용하여 조건별 새로운 컬럼을 생성할 수 있다.

## Implementation

파일: `exercises/column_operations.py`

구현 내용

* 학생 데이터를 DataFrame으로 생성했다.
* `bonus` 컬럼을 생성하여 모든 학생에게 5점의 가산점을 부여했다.
* `ratio` 컬럼을 생성하여 점수를 100점 기준 비율로 변환했다.
* `message` 컬럼을 생성하여 이름 뒤에 `" 학생"` 문자열을 추가했다.
* 반복문과 조건문을 이용하여 `grade` 컬럼(A/B/C)을 생성했다.

## 핵심 학습

* NumPy Broadcasting은 하나의 연산을 배열의 모든 요소에 적용하는 기능이다.
* Pandas는 Broadcasting을 이용하여 DataFrame 전체 컬럼을 한 번에 계산할 수 있다.
* 새로운 컬럼은 `df["컬럼명"] = 값` 형태로 생성한다.
* Python 리스트를 DataFrame 컬럼에 할당하면 자동으로 Series로 변환된다.

## Learned

* 반복문 없이 컬럼 전체에 동일한 계산을 적용할 수 있다.
* 기존 컬럼을 이용하여 새로운 정보를 생성하는 것이 데이터 분석의 핵심 과정이다.
* 조건에 따른 새로운 컬럼도 현재까지 학습한 Python 문법만으로 구현할 수 있다.
* 이후 `apply()`를 배우면 동일한 기능을 더욱 Pandas답게 구현할 수 있다.

## 실무 활용

* 부가세 포함 금액 계산
* 할인율 적용 가격 계산
* BMI 계산
* 합격 여부 생성
* 등급(A/B/C) 생성
* 장학금 대상 여부 생성

기존 데이터를 새로운 정보로 변환하는 대부분의 작업에서 활용된다.

## NumPy ↔ Pandas 연결점

| NumPy          | Pandas                            |
| -------------- | --------------------------------- |
| `scores + 5`   | `df["bonus"] = df["score"] + 5`   |
| `scores / 100` | `df["ratio"] = df["score"] / 100` |
| Broadcasting   | Column Operations                 |

## Next

* `apply()`를 이용하여 반복문 없이 컬럼 단위의 조건 처리를 구현한다.
* 현재 프로젝트의 `grade` 생성 로직을 `apply()` 기반으로 리팩터링한다.
