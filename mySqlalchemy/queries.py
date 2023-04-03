

'''
query{
  allTrainLogs{
    edges{
      node{
        epoch
        log
        createdAt
        description
        experiment {
          experimentIndex
          project {
            projectName
            authorName
            createdAt
            upatedAt
            description
          }
        }
      }
    }
  }
}
'''