''' 
The typical workflow is to write the data into columnar data files. 
These data files are then uploaded to a storage system and from there, 
they can be copied into the data warehouse. In case of Amazon Redshift, 
the storage system would be S3, for example.
 '''

 
# Write the pandas DataFrame to parquet
film_pdf.to_parquet("films_pdf.parquet")

# Write the PySpark DataFrame to parquet
film_sdf.write.parquet("films_sdf.parquet")


