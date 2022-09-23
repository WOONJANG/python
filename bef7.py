from bs4 import BeautifulSoup
from requests import * 
from re import * #정규식코드 사용위한 모듈
from random import *

#크롤링에 사용되는 파라미터 page view 번호
pno_data=["69382","70931","69388","69389"]

#해당 page view 배열을 순차적으로 접근 할 수 있도록 반복문 실행
for pno in pno_data:
    #해당 파라미터에 배열값을 입력시켜 배열이 끝날 때 까지 크롤링 함
    url="https://pages.coupang.com/p/"+pno+"?from=home_C2&traid=home_C2&trcid=11186418"
    html =get(url)
    html.raise_for_status()
    code = BeautifulSoup(html.text,"lxml")
    product = code.find("ul", attrs={"id":"products"})
    lis=product.find_all("li")

    for no in lis:
        name=no.find("div", attrs={"class":"name"}) #상품명
        cost=no.find("strong", attrs={"class":"price-value"}) #가격
        count=no.find("span",attrs={"class":"rating-total-count"}) #상품평
        img=no.find("img") #썸네일 이미지
        pd_img="https:"+img["lazy-load"]
        #img["lazy-load"] : attrs에서 해당 속성을 가져오지 못함 정상적인 속성값이 아닌 임의 속성값이므로 로드하지못함
        #임의생성된 속성값은 [] 배열형태로 로드하면 쉽게 가져올 수 있음
        
        '''
        #해당 상품 이미지를 모두 로드
        code = randrange(1000,9000) #새로운 이미지명을 random으로 생성
        imgload = get(pd_img)       #해당 URL로 이미지를 가져옴
        with open("product{0}.jpg".format(code),"wb") as i:
            i.write(imgload.content) #해당 경로에 이미지를 모두 저장시킴
        '''
            
        
        #상품평
        if count:
            rate = count.get_text()
            rate_txt=sub(r"[(,)]","",rate) #sub정규식코드, 모듈을 로드해야 사용가능
        else:
            rate_txt = "등록된 평점이 없습니다."    
        
        print(rate_txt)
        
        #상품명
        name_txt = name.get_text()
        pd_txt = name_txt.strip() #줄바꿈 및 공백 제거
        pd_txt = pd_txt.replace(", "," ") #상품명에 , 구분자 제거
        print(pd_txt)
        
        #가격
        money = cost.get_text()
        #replace(",","",1) : 1개만 수정
        #replace(",","") : 해당 단어의 모든 단어를 수정
        money_txt=money.replace(",","")
        print(money_txt)
    '''
    print(name.get_text())
    print(cost.get_text())
    print(count.get_text())
    '''

