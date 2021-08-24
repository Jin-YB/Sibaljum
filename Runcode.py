import easyocr

reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
# 언어 설정 및 gpu -> cpu 변경
result = reader.readtext(' ', detail=0, paragraph=True)  
# 공백에 이미지 경로(폴더.파일이름), detail 위치좌표 데이터 제외, paragraph 문자열 데이터 하나의 리스트로 다 담아서 저장
