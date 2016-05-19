from auth import *
'''
def followee_all()
for i in xrange((followees_num - 1) / 20 + 1):
    if i == 0:
        user_url_list = soup.find_all("h2", class_="zm-list-content-title")
        for j in xrange(min(followees_num, 20)):
            yield User(user_url_list[j].a["href"], user_url_list[j].a.string.encode("utf-8"))
    else:
        post_url = "http://www.zhihu.com/node/ProfileFolloweesListV2"
        _xsrf = soup.find("input", attrs={'name': '_xsrf'})["value"]
        offset = i * 20
        hash_id = re.findall("hash_id&quot;: &quot;(.*)&quot;},", r.text)[0]
        params = json.dumps({"offset": offset, "order_by": "created", "hash_id": hash_id})
        data = {
            '_xsrf': _xsrf,
            'method': "next",
            'params': params
        }
        header = {
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0",
            'Host': "www.zhihu.com",
            'Referer': followee_url
        }

        r_post = requests.post(post_url, data=data, headers=header)

        followee_list = r_post.json()["msg"]
        for j in xrange(min(followees_num - i * 20, 20)):
            followee_soup = BeautifulSoup(followee_list[j], "lxml")
            user_link = followee_soup.find("h2", class_="zm-list-content-title").a
            yield User(user_link["href"], user_link.string.encode("utf-8"))
'''
