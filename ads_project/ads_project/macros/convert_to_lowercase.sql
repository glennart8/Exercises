-- convert_to_lowercase.sql
{% macro convert_to_lowercase(column_name) %}
    LOWER({{ column_name }})
{% endmacro %}
