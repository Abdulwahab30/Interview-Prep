## Doc lens


### Features
- Login/Signup
    Fast APi and JWT based authentication
- PDF upload
    user uploads PDF, it is parsed every page table figure and even images/ OCR are parsed with the help of docling.
    The pipeline is that firstly when chunks are created from a document using page as a bounding box so that each page has seperate chunka nad they dont overlap. when the chunks are resturned 0 it means we need OCR thats where the OCR engne is called. the figures are sent toa vision based LLM to generate search friendly descriptions
- Embeddings
    The chunks are then passed to BGE 384 model to be embedded and then sent to be stored in qdrant
- retrieval
    For retrieval we use Semantic vector search, Postgres has a built-in full-text search engine (to_tsvector + plainto_tsquery) that finds exact keyword matches with a GIN index.

    This project runs both searches in parallel and merges results with RRF:

        combined_score = Σ( 1 / (k + rank_in_list) )   for each result list
    Best of both worlds: semantic recall + keyword precision.

    After merging vector + FTS results you have up to 50 candidate chunks. A cross-encoder (cross-encoder/ms-marco-MiniLM-L-6-v2) reads each (question, chunk) pair together and scores how well they match.

    This is far more accurate than cosine similarity because the model sees both texts simultaneously and understands their relationship. The top-5 highest-scoring chunks go to the LLM.
- Celery and redis
    parsing and embedding trakes some time. The upload endpoint shouldnt block the browser that long, so fast api uploads and returns status = queued. A celery task is pushed to redis queue. A seperate celery worker processes the ingestion pipeline.
- MinIO
    Raw PDF bytes are stored in MinIO, an S3-compatible object store that runs locally in Docker.
    FastAPI saves the storage key (e.g. user-id/uuid/filename.pdf) in Postgres, and the actual bytes in MinIO
    The Celery worker downloads from MinIO when processing
    Uses the standard boto3 S3 client — switching to real AWS S3 in production requires only an env var change, no code changes

- i dont quite get about sqlAlchemy and alembic and honestly i am not so keen on redis and celery as i dont quite fully understand them.