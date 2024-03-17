# 맥용 한글파일이름이 윈도우에서 자모가 분리된 형태로 보이는 것을 모아주는 프로그램
# 조합형 문자열을 완성형 문자열로 변환해주면 됨
# 프로그램을 실행한 후 파일이름 스트링을 복사해서 입력으로 넣어주면 됨
# 출력으로 나오는 스트링을 복사해서 파일이름으로 붙여 넣으면 완료

import unicodedata


def convert_to_complete_hangul(text):
    return unicodedata.normalize('NFC', text)


if __name__ == '__main__':
    text_combination = input("변환할 텍스트를 입력하세요: ")
    text_complete = convert_to_complete_hangul(text_combination)
    print(text_complete)
