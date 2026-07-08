# List & Dictionary

## 학습일

* 2026-07-07

## Goal

* 리스트(List)와 딕셔너리(Dictionary)를 이용해 데이터를 구조화하는 방법을 익힌다.
* 여러 개의 객체를 리스트 안에 저장하고 반복문으로 처리하는 방법을 이해한다.
* Pandas DataFrame의 기반이 되는 자료구조를 이해한다.

## Implementation

파일: `exercises/list_dictionary.py`

구현 내용

* 학생 정보를 리스트 안의 딕셔너리 형태로 저장했다.
* 모든 학생의 이름과 점수를 출력했다.
* 90점 이상인 학생만 필터링하여 출력했다.
* 학생들의 평균 점수를 계산했다.
* 반복문을 이용하여 최고 점수를 받은 학생을 찾았다.

핵심 학습

* 하나의 학생은 Dictionary로 표현하고, 여러 명의 학생은 List로 관리했다.
* 반복문과 조건문을 조합하여 원하는 데이터를 조회하고 계산했다.
* 최고 점수를 찾는 알고리즘을 직접 구현하며 데이터 탐색 과정을 이해했다.

## Learned

* List는 여러 개의 데이터를 순서대로 저장하는 자료구조이다.
* Dictionary는 하나의 객체를 Key-Value 형태로 표현하는 자료구조이다.
* List 안에 Dictionary를 저장하면 여러 개의 객체를 효율적으로 관리할 수 있다.
* 반복문을 이용하면 조건 검색, 집계(평균), 최대값 탐색 등을 구현할 수 있다.
* Pandas의 DataFrame은 이러한 List와 Dictionary를 기반으로 생성될 수 있다.

## Next

* List Comprehension을 학습하여 반복문을 더 간결하고 Python답게 작성하는 방법을 익힌다.
* List Comprehension이 Pandas의 데이터 변환과 어떤 관련이 있는지 이해한다.
