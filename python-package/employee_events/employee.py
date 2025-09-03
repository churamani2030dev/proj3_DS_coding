# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from .sql_execution import execute

import pandas as pd


# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self):
        # Query 3:
        # Select full name and id for all employees
        query = f"""
            SELECT
                (first_name || ' ' || last_name) AS full_name,
                {self.name}_id AS id
            FROM {self.name}
        """
        return execute(query)

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id):
        # Query 4:
        # Select the full name of the employee with matching id
        query = f"""
            SELECT
                (first_name || ' ' || last_name) AS full_name
            FROM {self.name}
            WHERE {self.name}_id = {id}
        """
        return execute(query)

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returned containing the execution of
    # the sql query
    def model_data(self, id):

        query = f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """

        rows = execute(query)  # list of tuples, e.g., [(pos_sum, neg_sum)]
        return pd.DataFrame(rows, columns=["positive_events", "negative_events"])
