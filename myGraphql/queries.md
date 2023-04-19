1. to select project by user-name

```yaml
query {
  findUser(userName: "wonchul1") {
    id
    projects {
      edges {
        node {
          id
          projectName
        }
      }
    }
  }
}
```

2. to select experiment by project-name

```yaml
query{
  findProject(userName: "wonchul1", projectName: "interojo") {
    id
    trainExperiments {
      edges {
        node {
          id
        }
      }
    }
  }
}
```

3. to see all logs by experiment

```yaml
query {
  findTrainExperiment(experiment: 1){
    trainLogs {
      edges {
        node {
          id
        }
      }
    }
  }
}
```
