<div align=center>

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/6mini/sixat&count_bg=%23AAAAAA&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Hits&edge_flat=false)](https://github.com/6mini/sixat)

![image](https://user-images.githubusercontent.com/79494088/147577233-bd0c1762-159f-4162-afa0-7aac6e8cfc1f.png)

<img src="https://img.shields.io/badge/Apache Spark-E25A1C?style=flat-square&logo=Apache Spark&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Apache Airflow-017CEE?style=flat-square&logo=Apache Airflow&logoColor=white"/></a>
<img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat-square&logo=Amazon S3&logoColor=white"/></a>


# Welcome to SIXAT 🙋🏻‍♂️

</div>

- 모빌리티 데이터 활용 대용량 데이터 실시간 처리 프로젝트: 'SIXAT'
- [블로그 포스팅 바로가기](https://6mini.github.io/project/2021/12/09/sixat1/)

# 문제 정의
- 대용량 데이터에서의 아키텍쳐를 설계하고 파이프라인을 구축하는 목적으로의 프로젝트이다.
- 모빌리티 데이터를 활용하여 이동 시간 혹은 택시 요금을 예측 한다는 가설을 세웠다.
- 무거운 머신러닝과 같은 프로세스는 오프라인 배치 프로세싱으로 학습하고, 이동 시간 및 택시 요금은 실시간으로 예측하는 파이프라인을 만들 것이다.

# 파이프라인

![image](https://user-images.githubusercontent.com/79494088/146979504-a57c3146-37e3-41f8-8232-ae52f62feaff.png)

- 현재는 스파크를 통한 대용량 데이터 분산 처리 및 에어플로우를 이용한 오케스트레이션까지만 구현했다.
- 데이터로 뉴욕 TRC 트립 기록 데이터를 이용한다.(매달 택시와 리무진 기록을 발표하며, 10년 이상의 택시와 모빌리티 서비스가 기록되어 있고, 매년 20GB 정도의 데이터셋이 쌓인다.)
- 수집된 데이터를 스파크 SQL을 통해 프리프로세싱을 진행하고, 정리한 데이터로 스파크 MLlib을 통해 머신러닝 모델링을 진행 후 저장했다.
- 스파크로 구현한 모든 과정을 자동화할 수 있도록 에어플로우 테스크로 구현하였다.

# 중간 회고
- 대용량의 데이터를 빠르게 처리하는 기술인 분산 처리 시스템을 익히고 싶었는데, 사실 공부하기 전엔 굉장히 벽이 높아 보였지만 공부하고 보니 다루는게 생각보다 까다롭지 않았고, 트러블 슈팅도 쉽게 해결되어서 프로젝트 자체를 진행함에 굉장히 만족하는 중이다.
- 에어플로우도 마찬가지로 잘만 다룬다면, 스케쥴링에 있어서 활용도가 높을 것 같다는 생각을 했다.
- 앞으로 카프카와 플링크를 통해 실시간으로 처리하는 것을 진행할텐데, 기대가 많이 된다.