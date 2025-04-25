Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

# Step by step
1. Initiera dbt-projekt, lägg in databas, debugga och se så allt fungerar som det ska.
2. Definera sources, dbt_project.yml, schema osv: sources: 
                                                    - name: job_ads
                                                    schema: staging
                                                    tables: 
                                                        - name: stg_data_ads
                                                        identifier: data_field_job_ads

3. Hämta rådatan - source('job_ads', 'stg_data_ads'), definera vilka kolumner du vill ha med
4. Skapa dims - unika id med generate_surrogate_key
5. Skapa facts - Använd generate_surrogate_key igen till id för dims,
    joina alla dim-tabeller
 
