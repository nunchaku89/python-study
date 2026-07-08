# List Comprehension

## 학습일

* 2026-07-07

## Goal

* List Comprehension을 이용해 반복문을 간결하게 작성하는 방법을 익힌다.
* 조건을 포함한 List Comprehension을 작성할 수 있다.
* List Comprehension이 데이터 변환에 어떻게 활용되는지 이해한다.

## Implementation

파일: `exercises/list_comprehension.py`

구현 내용

* 숫자 리스트의 각 요소를 제곱한 새로운 리스트를 생성했다.
* 조건을 이용하여 20 이상인 숫자만 추출했다.
* 학생 정보(List of Dictionary)에서 이름만 추출한 리스트를 생성했다.
* 90점 이상 학생의 이름만 추출했다.
* 학생 정보를 문자열 형태(`이름 : 점수`)로 변환하는 방법을 실습했다.

핵심 학습

* 기존 리스트를 반복하면서 새로운 리스트를 생성하는 작업을 List Comprehension으로 간결하게 표현할 수 있음을 확인했다.
* 데이터를 변환할 때는 원본 리스트를 덮어쓰기보다 새로운 변수에 저장하는 것이 유지보수와 가독성 측면에서 유리하다는 점을 배웠다.
* List Comprehension은 **새로운 데이터를 생성하는 용도**이며, `print()`처럼 반환값이 없는 작업에는 적합하지 않다는 점을 이해했다.

## Learned

* List Comprehension은 반복문과 `append()`를 대체하는 Python다운 표현 방식이다.
* 조건(`if`)을 함께 사용하여 원하는 데이터만 추출할 수 있다.
* 데이터를 변환할 때는 `student_names`, `high_score_students`처럼 의미 있는 변수명을 사용하는 것이 좋다.
* 원본 데이터를 보존하면 이후 다른 분석이나 추가 가공을 수행하기 쉽다.

## Pandas 연결점

* List Comprehension은 기존 데이터를 새로운 형태로 변환하는 사고방식을 익히는 과정이다.
* 이 개념은 Pandas에서 컬럼 선택, 조건 필터링, 데이터 변환을 이해하는 기반이 된다.
* 예를 들어 `student["score"] >= 90`이라는 조건은 이후 Pandas에서 `df[df["score"] >= 90]`과 같은 형태로 확장된다.

## Next

* 예외 처리(Exception Handling)를 학습하여 잘못된 입력이나 파일 오류에 안전하게 대응하는 방법을 익힌다.
* 이후 NumPy를 학습하기 위한 Python 기초를 마무리한다.
