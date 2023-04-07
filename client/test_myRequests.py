from myRequests import test 

if __name__ == '__main__':
    url = "http://localhost:5000/graphql"

    # query = """
    #         {
    #         allTrainLogs{
    #             edges{
    #             node{
    #                 epoch
    #                 log
    #                 createdAt
    #                 description
    #                 experiment {
    #                 experimentIndex
    #                 project {
    #                     projectName
    #                     authorName
    #                     createdAt
    #                     upatedAt
    #                     description
    #                 }
    #                 }
    #             }
    #             }
    #         }
    #         }
    #         """
    
    query = """
            {
                allProject
            }
            """
    print(test(url, query))