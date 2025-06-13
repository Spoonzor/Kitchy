curl -X POST http://localhost:8000/api/accounts/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "seghiry", "password": "L33trainrirzor!-"}'

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0NTk0MDY0LCJpYXQiOjE3NDQ1OTM3NjQsImp0aSI6IjY5OTQ4NmI4YzA5YjQxZGY4YWRkM2M0ODgyODU3ZGI5IiwidXNlcl9pZCI6MX0.yzahfJrLUtktbWkk_6euTwsOSi2163mEFdgxDxj7UQw


curl -X PUT http://localhost:8000/api/inventory/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0NTk0MDY0LCJpYXQiOjE3NDQ1OTM3NjQsImp0aSI6IjY5OTQ4NmI4YzA5YjQxZGY4YWRkM2M0ODgyODU3ZGI5IiwidXNlcl9pZCI6MX0.yzahfJrLUtktbWkk_6euTwsOSi2163mEFdgxDxj7UQw" \
  -d '{"name": "Pommes", "quantity": 10, "expiration_date": "2024-01-01", "category": "Fruits", "location": "Cuisine", "barcode": "1234567890123"}'


  {
  "name": "Pommes",
  "quantity": 5,
  "expiration_date": "2024-01-01",
  "category": "Fruits",
  "location": "Cuisine",
  "barcode": "1234567890123"
}