- "How does your retrieval pipeline work?" 
    In doc lens we use celery and redis so that the uopload thread isnt blocked and status = queued appears and the retrieval task is sent to redis by a celery worker.
    the users question is embedded using the same model taht embedded the document bge. then bi encoder fethes similar chunks using cosine similarity 30 chunks come and after that we use reranking(cross encoder) to slim it down to top 5.after that we send this to the llm model which then generates the ans
- "What is Celery doing in your system and why?"
    Celery is being used as a task scheduler. it schedules the task so that it doesnt block the whole app pipeline
- "What is MinIO and why not just save files to disk?"
    the chunks/ embeddings are stred in minIo as it is s3 compatible and runs locally in docker.
    FastAPI saves the storage key (e.g. user-id/uuid/filename.pdf) in Postgres, and the actual bytes in MinIO. it will later help to switch to production aws server.

