# Pipeline de datos climáticos con RAG en Azure

Proyecto end-to-end de ingeniería de datos: extracción de datos de una API pública,
orquestación con Airflow, arquitectura Medallion en Databricks con Spark,
transformaciones con dbt y sistema de preguntas y respuestas con RAG.

## Estado actual
- [x] Fase 0: extracción desde Open-Meteo API → JSON local (script Python + manejo de errores)

## Roadmap
- [ ] Fase 1: aterrizaje en Azure Data Lake (ADLS Gen2)
- [ ] Fase 2: orquestación con Airflow (DAG diario)
- [ ] Fase 3: Databricks + Spark + Medallion (Bronze/Silver/Gold)
- [ ] Fase 4: dbt (modelos, tests, documentación)
- [ ] Fase 5: RAG (LangChain + Chroma + LLM)
- [ ] Fase 6: FastAPI + CI con GitHub Actions