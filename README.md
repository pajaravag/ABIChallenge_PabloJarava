# ABIChallenge_PabloJarava
Test to the role of MLOps

In this repository, I aim to demonstrate how to deploy a machine learning model as an API hosted on the Google Cloud Platform. The model predicts whether someone survived the Titanic disaster, as outlined in the guidelines.

In this repository, I utilize FastAPI as a framework to illustrate how to create endpoints for posting and retrieving responses from an API. The model, unfortunately, was not trained properly and lacks validation due to my focus on deployment rather than consistency.

As part of this process, I have implemented an ETL  process to ensure that each output from the requests can be seamlessly migrated with any database engine. To achieve this, we employ a Tortoise project as an ORM to handle the task efficiently.

This environment is encapsulated within its own Docker Image.

## Execution

Running tests can be performed either locally or by submitting a POST request to the GCP artifact.

## Database Migration

For migrating the database, run the following commands:

```bash
docker-compose up -d --build
```

Init as follows:

```bash
docker-compose exec api aerich init -t src.db.TORTOISE_ORM
```

Create the migration as follows:

```bash
docker-compose exec api aerich init-db
```

You should see the following migration inside a new file within `migrations/models`
