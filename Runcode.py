import easyocr

reader = easyocr.Reader(['ko', 'en'], gpu=False)
# 언어 설정 및 gpu -> cpu 변경
result = reader.readtext('sample.jpg', detail=0, paragraph=True)
# 공백에 이미지 경로(폴더.파일이름), detail 위치좌표 데이터 제외, paragraph 문자열 데이터 하나의 리스트로 다 담아주기
result_join = " ".join(result)
# 리스트로 나온거 한 문자열로 통합
print(result_join[0])
# 첫번째 글자 출력