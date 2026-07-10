def create_report(result):
    return f"""
==============================
      Refactoring Report
==============================
평균 : {result['average']:.2f}

최대값 : {result['max']}

최소값 : {result['min']}

결측치 : {result['missing']}

전공별 평균
{result['major_mean']}

등급 분포
{result['grade_count']}
"""