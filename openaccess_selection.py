import sys
import time

import pandas as pd
from pymed import PubMed

def extract_info(articleList):
    """
    Extracts relevant information from articleList and returns it as a pandas DataFrame.
       
    Parameters:
        - articleList (list): List of articles obtained from PubMed search.
        ['pubmed_id', 'title', 'abstract', 'keywords', 'journal', 'publication_date', 'authors', 'methods', 'conclusions', 'results', 'copyrights', 'doi', 'xml', 'pcmid']
    
    Returns:
        - pandas.DataFrame: DataFrame with relevant information extracted from articleList.
    """

    ### EXTRACT THE INFORMATION NEEDED FROM EACH ARTICLE IN PUBMED.

    articleInfo = []

    for article in articleList:
        pubmedId = article['pubmed_id'].partition('\n')[0]

        articleInfo.append({u'pubmed_id':pubmedId,
                            u'title':article['title'],
                            u'keywords':article['keywords'],
                            u'journal':article['journal'],
                            u'abstract':article['abstract'],
                            u'conclusions':article['conclusions'],
                            u'methods':article['methods'],
                            u'results': article['results'],
                            u'copyrights':article['copyrights'],
                            u'doi':article['doi'],
                            u'publication_date':article['publication_date'], 
                            u'authors':article['authors']})

    articlesPD = pd.DataFrame.from_dict(articleInfo)   
    return articlesPD

def find_article(pmid):

    # GENERATE 'pubmed' OBJECT TO RUN THE SEARCH LATER.
    pubmed = PubMed(tool = 'PubMedSearch')


    # CREATE AN EMPTY LIST TO STORE THE RESULTS
    articleList = []
        
    # DEFINE THE SEARCH QUERY
    query = f"pubmed pmc open access[filter] {pmid}"
    #print(pmid)

    # RUN THE SEARCH AND SPECIFY THE MAXIMUM NUMBER OF RESULTS YOU WANT
    # RETRY A MAXIMUM OF 10 TIMES
    MAX_RETRIES = 10
    num_retries = 0

    while num_retries < MAX_RETRIES:
        try:
            results = pubmed.query(query, max_results=1000) 
            
            # LOOP OVER THE RETRIEVED ARTICLES AND SAVE IT IN 'articleList'
            # ALSO STORE THE DATA OF PUBMEDAKE
            for article in results:
                articleDict = article.toDict()
                articleList.append(articleDict)
            
            # IF THERE WERE NO EXCEPTIONS, BREAK THE LOOP
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            num_retries += 1
            if num_retries == 9:
                print(f"Too many retries")
                break
            # WAIT BEFORE RETRYING
            time.sleep(1)

    return articleList

if __name__ == "__main__":
    f = open("dois_pubmed_v5.txt", "w")

    # Replace 'your_file.csv' with the path to your CSV file.
    file_path = 'registry_RRID_mentions_v3.xlsx'

    # Load the CSV file into a DataFrame
    df = pd.read_excel(file_path)

    count = 0

    for index, row in df.iterrows():
        print("Row:"+row["pmid"][5::])
        pmid = int(row["pmid"][5::])
        uri = row["uri"]
        exact = row["exact"]
        resource_type = row["Resource type"]
        print(uri)
        #pmid=35931085
        type(pmid)
        articleList = find_article(pmid)
        articlesPD = extract_info(articleList)
        try:
            copyright = articlesPD['copyrights'][0]
            doi = articlesPD['doi'][0]
            
            #f.write(str(pmid)+"\t"+doi.split('\n')[0]+"\n")
            f.write(uri+";"+exact+";"+resource_type+"\n")
            print(doi)
            count += 1
        except KeyError:
            print("Not open Access!")
        except TypeError:
            print("Error")

        time.sleep(1)

    f.close()
