### Gender Definer

Python package for detect a gender from cyrillic names and latin names

###### Github
```
https://gihub.com/yeghorkikhai/gender-definer
```

###### Installation pip
```
pip install gender-definer
```

###### Installation poetry
```
poetry gender-definer
```

### Example

```python
from genderdefiner import GenderDefiner

gd = GenderDefiner()

print(gd.define('Юля'))

# output:
#
# SubjectGender(gender='female', probability=0.7646426652337452)
#
```