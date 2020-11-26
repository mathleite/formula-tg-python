<h1 align="center">Formula-TG ~Python</h1>

<p align="center">
    <a href="https://github.com/mathleite/formula-tg-python">
        <img src="https://github.com/mathleite/formula-tg-python/workflows/C.I/badge.svg" alt="Workflow badge">
    </a>
</p>

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