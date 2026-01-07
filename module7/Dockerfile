# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy your code
COPY Hana_mod7_1.py .

# Run the program
CMD ["python", "Hana_mod7_1.py"]


# RUN IN TERMINAL :
# docker buildx build --load -t hana_ex1:1.0.0 .

# to save my image:
# docker save hana_ex1:1.0.0 -o hana_ex1.tar

#to load my image
# docker load -i hana_ex1.tar