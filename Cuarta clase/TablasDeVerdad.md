# Tablas de verdad

Proposicion logica: una expresion que puede ser o verdadero o falso

p: hacer la tarea

q: lavar la ropa

## Conjuncion

|p|q|p and q|
|---|---|---|
|V|V| V|
|V|F| F|
|F|V| F|
|F|F| F|

## Disyuncion debil

|p|q|p or q|
|---|---|---|
|V|V|V|
|V|F|V|
|F|V|V|
|F|F|F|

## Negacion

|p| not p|
|---|---|
|V|F|
|F|V|
## Equivalencias logicas

### Morgan

```python
not (p and q) === not p or not q

not (p or q) === not p and not q
```

### Idempotencia

```python
p and p === p

p or p === p
```

### Absorcion

```python
p and (p or q) === p

p or (p and q) === p
```