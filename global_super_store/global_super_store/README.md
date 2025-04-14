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


# staging/ – Här förbereder vi materialet (t.ex. putsar tegelstenarna)
    - Läser vi in rådata från källan (t.ex. raw_orders)
    - Rensar och standardiserar kolumnnamn
    - Kastar bort skräp eller gör tydliga typomvandlingar (ex. CAST(sales AS float))

# intermediate/ – Här bygger vi strukturen (golv, väggar)
    - Sammanställningar
    - Gruppningar
    - Joinar mellan olika tabeller

# marts/ – Här inreder vi och gör det snyggt för slutanvändaren (dashboarden, analysen)
    - Innehåller bara det som behövs
    - Presenteras i ett affärsspråk (t.ex. "customer_segment" = VIP/Regular)

    - staging	        Rå → renad data	        Standardisering, typomvandling
    - intermediate	    Beräkningar, joinar	    Affärslogik, återanvändning
    - marts	            Klar för dashboard	    Färdig till användare/BI