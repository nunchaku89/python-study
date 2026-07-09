# Mini Project 1 - Student Score Analysis

## 학습일

* 2026-07-08

## Goal

* 지금까지 학습한 Python, NumPy, Pandas 기능을 실제 데이터 분석에 적용한다.
* CSV 파일을 읽고 데이터를 이해, 정제, 분석하는 전체 흐름을 경험한다.
* 분석 결과를 별도의 리포트로 저장하는 프로젝트 구조를 익힌다.

## Project Structure

```text
python-study/
├── data/
│   └── students.csv
├── projects/
│   └── student_analysis.py
├── reports/
│   └── student_report.csv
└── logs/
```

## Implementation

파일: `projects/student_analysis.py`

### Phase 1 - 데이터 이해

* CSV 파일을 읽어 DataFrame으로 생성했다.
* `head()`, `tail()`을 이용하여 데이터 구조를 확인했다.
* `info()`와 `describe()`를 이용하여 데이터 타입과 통계 정보를 확인했다.

### Phase 2 - 데이터 정제

* `isna()`를 이용하여 결측치를 확인했다.
* 평균 점수를 계산하여 `fillna()`로 결측치를 대체하는 방법을 적용했다.
* DataFrame의 자료형과 결측치 처리 방식을 확인했다.

### Phase 3 - 데이터 분석

* 평균 점수 계산
* 최고 점수 및 최저 점수 확인
* 90점 이상 학생 조회
* 전공별 평균 점수 계산

### Phase 4 - 결과 저장

* 분석 결과를 파일로 저장하는 기능을 구현했다.
* 원본 CSV를 수정하지 않고 별도의 리포트 파일을 생성해야 한다는 점을 학습했다.

## Learned

* 데이터 분석은 **이해 → 정제 → 분석 → 저장**의 순서로 진행하는 것이 일반적이다.
* `fillna()`는 원본을 변경하지 않으므로 결과를 다시 저장하거나 재할당해야 한다.
* `info()`는 정보를 출력하는 함수이며 반환값은 `None`이다.
* 원본 데이터와 분석 결과는 반드시 분리하여 관리해야 한다.
* 반복되는 조건별 계산은 이후 `groupby()`를 사용하면 더욱 간결하게 작성할 수 있다.

## 실무 개선 사항

* 원본 CSV에는 분석 결과를 기록하지 않는다.
* 분석 결과는 `reports/` 폴더에 별도의 CSV 또는 TXT 파일로 저장한다.
* 전공별 평균처럼 반복되는 계산은 `groupby()`를 활용하여 구현한다.
* 프로젝트 코드는 단계별 함수로 분리하면 유지보수와 테스트가 쉬워진다.

## 사용한 기술

* File I/O
* Exception Handling
* NumPy
* Pandas DataFrame
* Filtering
* Statistics
* Missing Value Handling

## Next

* Pandas `groupby()`를 이용한 그룹별 통계 분석을 학습한다.
* 여러 컬럼을 기준으로 데이터를 집계하는 방법을 익힌다.
* 프로젝트를 `groupby()`를 활용하는 방식으로 리팩터링한다.
