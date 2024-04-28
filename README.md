# ABIChallenge_PabloJarava
Test to the role of MLOps



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
