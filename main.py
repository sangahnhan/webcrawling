import requests

indeed_result= requests.get("https://kr.indeed.com/취업?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l=서울&fromage=any&limit=10&sort&psf=advsrch&from=advancedsearch&vjk=25b0fa17d08dd0cd")

print(indeed_result)