# Pandas apply()

## 학습일

* 2026-07-08

## Goal

* `apply()`의 동작 원리를 이해한다.
* 사용자 정의 함수를 DataFrame 컬럼에 적용하는 방법을 익힌다.
* 반복문 대신 Pandas의 컬럼 연산을 활용하는 방법을 학습한다.

## Implementation

파일: `exercises/apply.py`

구현 내용

* 학생 데이터를 DataFrame으로 불러왔다.
* `get_grade(score)` 함수를 작성하여 점수에 따른 등급(A/B/C)을 반환하도록 구현했다.
* `get_pass(score)` 함수를 작성하여 합격 여부(Pass/Fail)를 반환하도록 구현했다.
* `apply()`를 이용하여 `grade`와 `result` 컬럼을 생성했다.

## 핵심 학습

* `apply()`는 컬럼의 각 요소에 함수를 반복 적용한다.
* `apply()`에는 함수의 실행 결과가 아니라 함수 자체를 전달해야 한다.
* `apply(get_grade())`가 아니라 `apply(get_grade)`를 사용해야 한다.
* `apply()`는 내부적으로 반복문을 수행하므로 코드가 더욱 간결하고 Pandas다운 형태가 된다.

## Learned

* 함수 호출과 함수 전달은 서로 다른 개념이다.
* 반복문으로 작성했던 조건 분기 로직을 `apply()` 하나로 대체할 수 있다.
* DataFrame의 컬럼은 `Series`이며, `Series.apply()`를 통해 컬럼 단위의 데이터 변환을 수행할 수 있다.

## 실무 활용

* 등급(A/B/C) 생성
* 합격 여부 생성
* 할인율 계산
* 위험도 분류
* 문자열 전처리
* 날짜 형식 변환

복잡한 데이터 변환 로직을 함수로 분리하여 재사용할 때 자주 활용된다.

## 프로젝트 개선 사항

기존

```python
grade = []

for score in df["score"]:
    ...
```

↓

개선

```python
df["grade"] = df["score"].apply(get_grade)
```

반복문을 제거하고 함수 기반의 Pandas 코드로 리팩터링하였다.

## Next

* `merge()`를 이용하여 여러 DataFrame을 결합하는 방법을 학습한다.
* 프로젝트에서 학생 정보와 전공 정보를 하나의 DataFrame으로 결합해 본다.
