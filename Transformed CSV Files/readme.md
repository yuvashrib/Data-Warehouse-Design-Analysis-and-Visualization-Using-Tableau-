This folder contains the trasformed csv files
The data was split into different files according to the star schema.
Each entity represents a dimension table, and they contain data that will be used to populate the corresponding tables in the Oracle database.
To ensure data integrity and establish relationships between tables, a unique ID key column was included in each entity file, which will serve as the primary key for that table. These unique IDs will also be used as foreign keys in the main fact table.
Each entity file contains unique values, ensuring that there are no duplicate records within each dimension table. This uniqueness is essential for maintaining the integrity of the data and facilitating proper data analysis and querying in the database.
Organizing data into separate files with unique IDs lays a robust foundation for efficient data management, ensuring accuracy, consistency, and scalability for analysis and reporting.
