![header](https://capsule-render.vercel.app/api?type=waving&height=200&fontSize=50&color=gradient&text=Data-Centric%20KLUE-TC&fontAlignY=26&desc=텍스트%20주제%20분류(Text%20Classification,%20TC)&descAlignY=49&descSize=23&fontColor=ffffff)

<td style="text-align:center; border-color:white" rowspan="3" width=660>
      <p align="center">
        <img src="/assets/klue-tc-img.png" width=600>    
      </p>
</td>  

### <p align="center"><code>Data-Centric KLUE-TC</code> 는</p> 
<p align="center">Data-Centric 관점으로,</p>
<p align="center">모델 구조의 변경없이 데이터의 변경만으로</p>
<p align="center">텍스트의 주제를 분류하는 NLP Task 입니다.</p>

<table align="center">
  <tr height="8px">
    <td align="center" style="text-align:center;" width="80px">
      <b>Wrap-up Report</b>
    </td>
    <td align="center" style="text-align:center;" width="80px">
      <b>개인 회고</b>
    </td>
  </tr>
  
  <tr height="40px">
    <td align="center" width="150px">
      <a href="/assets/TC_WrapUp_NLP_07.pdf"><img src="https://img.shields.io/badge/PDF-CC2927?style=flat-square&logo=microsoft&logoColor=white">
    </td>
    <td align="center" width="150px">
      <a href="https://www.notion.so/mayy2yy/Project-KLUE-TC-e6c475ce77364a99a014b70cdaf84c2c"><img src="https://img.shields.io/badge/notion-%23000000.svg?&style=flat-square&logo=notion&logoColor=white "/></a>
    </td>
  </tr>
</table>
<p align="center">(↑ 로고를 클릭하면 링크로 이동합니다)</p>
<br>
<br>

## 📖 Overview
### 1. 프로젝트 개요

사람은 무의식적으로 각 자연어 문장들이 어떤 주제로 이루어져 있는지 판단 후 내용을 파악하게 됩니다. <br>
그렇다면 사람이 아니라 **딥러닝 모델**은 어떨까요? 

자연어를 독해 및 분석 과정을 거쳐 주어진 task를 수행하기 위해서는 자연어의 주제에 대한 이해가 필수적입니다. <br>
`주제분류(Topic Classification)` task 중 `KLUE-TC` benchmark는 뉴스의 헤드라인을 통해 그 뉴스의 topic을 분류해내는 task입니다.<br>

- train
    
    기사 제목에 해당하는 `생활문화(Society)`, `스포츠(Sports)`, `세계(World)`, `정치(Politics)`, `경제(Economy)`, `IT과학(IT/Science)`, <br>`사회(Society)` 7개의 주제 중 하나의 라벨
    
- inference
    - <code>**input**</code> : 약 9100개의 뉴스 헤드라인과 url, 작성 날짜
    - <code>**output**</code> : 각 뉴스 헤드라인의 주제 (생활문화, 스포츠, 세계, 정치, 경제, IT과학, 사회 중 하나)
    - <code>**평가기준**</code> : 모든 label에 대해 중요도를 동일하게 부여하는 ***macro*** F1 Score

<br>

### 2. 목표
- Data-Centric 의 취지에 맞게, 베이스라인 모델의 수정 없이 오로지 **데이터의 수정으로만**의 모델의 성능 향상을 목표로 합니다.
- 주어진 text(뉴스 헤드라인)의 주제를 분류할 때, **7개의 중 가장 정확한 target(label) 하나를 예측**하는 것을 목적으로 합니다.

<br>

### 3. 평가 방법
평가 방법은 다음과 같습니다.
- 모든 label에 대해 중요도를 동일하게 부여하는 <code>_**macro**_ F1</code> score
<br>
<br>



## 🏅 리더보드 순위
- **public** `2위` → **private**(최종) `3위`🏅
<p align="center">
  <img width="900px" alt="image" src="/assets/tc-rank-img.png">
</p>
  <!--<img width="500" alt="image" src="https://github.com/seohyunee22/level2_klue-re_project/assets/152946581/1d226266-5c75-42fb-8e0d-ed9c4fca5632">   -->

<br>
<br>


## 💼 담당 업무
<table align="center">
  <tr height="200px">
    <td align="center" width="250px">
      <a href="https://github.com/seohyunee22"><img src="https://avatars.githubusercontent.com/seohyunee22"/></a>
    </td>
    <td align="left" style="text-align:left;" width="500px">
      1.  데이터 증강 <br>
      - <a href="https://github.com/Kyubyong/g2pK">g2p(to-Phoneme)</a> 노이즈 생성 <br>
      -  p2g(to-Grapheme) 노이즈 생성<br>
      - <a href="https://arxiv.org/abs/2108.13230">AEDA</a> <br>
      -  Back Translation<br><br>
      2. Label 교정<br>(<a href="https://docs.cleanlab.ai/stable/index.html">Cleanlab 라이브러리</a>를 이용한 <br>라벨링 이슈 탐지 및 교정)<br>      
    </td>
  </tr>
  <tr height="100px">
    <td align="center" width="250px">
    <a href="https://github.com/seohyunee22">[ 양서현_T6099 ]</a>
    </td>
    <td align="letf" width="500px">
     * g2p(Grapheme-to-Phoneme) : 글자를 발음나는 대로 적는 방법<br>
     * p2g(Phoneme-to-Grapheme) : g2p의 반대 <br>
    </td>
  <tr>
</table>
  
<br>
<br>

## 🛠️ Tech Stack
<img src="https://img.shields.io/badge/Pytorch-EE4C2C?style=flat-square&logo=Pytorch&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/scikitlearn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white">
<br><img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/notion-%23000000.svg?&style=flat-square&logo=notion&logoColor=white "/>
<br>
<br>

## 💡 프로젝트 수행

<table align="center">
 <tr height="40px">
    <td align="center" style="text-align:center;" width="250px">
      <b>01</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>02</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>03</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>04</b>
    </td>
  </tr>
  <tr height="50px">
    <td align="center" style="text-align:center;" width="250px">
      <b>EDA</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>Data Re-Labeling</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>Data Cleaning</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>Data Pre-processing</b>
    </td>
    <td align="center" style="text-align:center;" width="250px">
      <b>Data Augmentation</b>
    </td>
  </tr>
  <tr height="100px">
    <td align="left" style="text-align:left;" width="260px">
      - 학습 데이터 개요 <br>
      - 평가 데이터 개요<br>
      - input_text 길이 분석<br> 
      - noise 데이터 분석<br> 
    </td>
    <td align="left" style="text-align:left;" width="260px">
      - 전체 라벨 직접 검수<br>
      - CleanLab 라이브러리 이용<br>
    </td>
    <td align="left" style="text-align:left;" width="260px">
      - g2p 제거 <br>
      - UNK 토큰 제거<br>
      - 한자 제거 및 변환</b><br> 
    </td>
    <td align="left" style="text-align:left;" width="260px">
      - 형태소 기반 <br>Subword 토크나이징 <br>
    </td>
    <td align="left" style="text-align:left;" width="260px">
      - g2p 노이즈 데이터 생성 <br>
      - <a href="https://arxiv.org/abs/2108.13230">AEDA</a> <br>
      - <a href="https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=577">AI hub 뉴스 기사 <br>기계독해 데이터 추가</a> <br>
      - Back Translation <br>
    </td>
  </tr>
</table>
<br>
🔎 프로젝트 수행과정에 대한 자세한 내용은 <a href="https://www.notion.so/mayy2yy/Project-KLUE-TC-e6c475ce77364a99a014b70cdaf84c2c?pvs=4#ccf9c77e50594387b226d3b15bccd92c"><img src="https://img.shields.io/badge/notion-%23000000.svg?&style=for-the-badge&logo=notion&logoColor=white "/></a>(개인 회고, 클릭시 이동) 에서 확인하실 수 있습니다.


<br>
<br>

## 🎓 Reference
[1]  g2pK: g2p module for Korean, https://github.com/Kyubyong/g2pK<br>
[2]  cleanlab documentation, https://docs.cleanlab.ai/stable/index.html<br>
[3]  AI Hub 뉴스 기사 기계독해 데이터, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=577<br>
[4]  AEDA: An Easier Data Augmentation Technique for Text Classification. Akbar Karimi, Leonardo Rossi, Andrea Prati (2021).  *[arXiv preprint arXiv:2108.13230](https://arxiv.org/abs/2108.13230)*
