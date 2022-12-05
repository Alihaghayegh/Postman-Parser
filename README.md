# Postman Parser
- This module opens the Postman Collection json and parse it and return the cURL
Pass the collection path to main function, and it returns a list of curls.
***********************************************************************************
* At first create an instance of Postman_parser class :
```python
postman = Postman_parser()
```
* Postman_parser class has method called postman_to_curl .
```python
curls = postman.postman_to_curl("your postman collection address")
```
* Pass the complete Postman collection address on your machine and this method returns a list of curl commands.
```python
print(curls)
```