import requests as req
import json
import timeit


url = "https://bg.annapurnapost.com/api/search?page={}&title={}"



def get_totalPage(data):
    '''
        get total page to scrape about related searched term.
    '''
    total_page = data['data']['totalPage']
    print(f'\n total page number {total_page}')
    return total_page



def get_result(url, search_term, total_page):
    '''
        scrape all the articles in json format, write in json file, show the article threshold, display total number of article.
    '''
    article_threshold = 30
    total_article = 0
    total_page = total_page + 1

    for i in range(1, total_page):
        print(f"\npagination {i}")
        res = req.get(url.format(i,search_term))
        data = res.json()

        try:
            if res.status_code == 200:
                if data["status"] == 'success':
                    article_no = len(data['data'].get('items'))
                    article_threshold -= article_no
                    total_article += article_no

                    # writing json data in file
                    with open('articlefile.json', 'a', encoding='utf-8') as f:
                        print(f"writing the file")
                        json.dump(data['data']['items'], f, ensure_ascii=False, indent=4)
                        f.write(',')
                    
                    if not article_threshold<=0: 
                        print(f"article threshold remaining is {article_threshold}")
                    
                    

        
        except:
            print(f"error occured for page {i}")
            continue
    
    f.close()

    print("-----------------------------------------------")
    print(f"total article_no scraped is {total_article}")

   
   


if __name__=="__main__":
    search_term = input("Enter search term: ")

    res = req.get(url.format(1,search_term))
    data = res.json()

    total_page = get_totalPage(data)
    get_result(url, search_term, total_page)