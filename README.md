# Formula-TG ~Python

### Setup
1. ```docker
   docker-compose up --build -d
   ```
2. ```bash
   pip install -r requirements.txt
   ``` 
#### Lint Python files with Mypy
```
~$ mypy src/ test/
```

#### Run Tests
```
~$ python -m unittest
```

#### Simplify Your Life (`lint + tests`) script
```
~$ ./simplify-my-life.sh
```