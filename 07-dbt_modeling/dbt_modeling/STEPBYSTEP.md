1.  
Kör dbt init
Lägg till anslutningsuppgifter i profiles.yml (ex: Snowflake, BigQuery etc)
Testa anslutningen med dbt debug
Strukturera projektmappen (models, macros, tests, etc)

2. 
Definiera källdata (sources)
Skapa sources.yml i mappen models/staging/<område>
Exempel:
    sources:
        - name: job_ads
            schema: staging
            tables:
            - name: stg_data_ads
                identifier: data_field_job_ads

3. 
Skapa stagingmodeller (stg_)
Hämta data med {{ source('job_ads', 'stg_data_ads') }}
Rensa kolumner: välj relevanta fält, döp om, normalisera, typkonvertera
Lägg gärna till tester på t.ex. id (unique, not_null)

4. 
Skapa dimensionstabeller (dim_)
Använd generate_surrogate_key() för att skapa stabila ID:n
Kombinera fält som identifierar entiteten (ex: id, name)

5.
Bygg på stg_ och dim_
Använd ref() för att joina in rätt dimensionstabeller
Lägg till surrogatnyckel även här om det behövs
Summera, gruppera, beräkna mått (antal, snitt, etc)
Säkerställ att joins inte duplicerar rader

# EXTRA
6. 
Lägg till tester
unique, not_null, accepted_values, etc
Använd dbt test för att verifiera att allt stämmer

7.
Fyll i description: i schema.yml för källor, modeller och kolumner
Kör dbt docs generate och dbt docs serve för att se resultatet

8. 
Automatisera (valfritt, men nice)
Lägg till CI/CD i GitHub/GitLab för automatiska tester
Använd dbt Cloud eller dbt Scheduler (eller Airflow) för att köra pipelines
Schemalägg fulla refreshes och inkrementella körningar