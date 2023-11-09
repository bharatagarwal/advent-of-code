In Part 2, I had originally given the regex for `flank_checker` as 

```python3
r'([a-z]+)./1'
```

However, this led to an excess number of matches, compared to the answer expected.

After modifying it to 

```python3
r'([a-z]./1)'
```

I got the correct answer.

The excess matches were along the lines of:

```python3
<re.Match object; span=(4, 9), match='nrjnr'>
<re.Match object; span=(11, 16), match='kggkg'>
<re.Match object; span=(8, 13), match='zdlzd'>
```
This was matching one or more characters between the pivot. The requirement was specifically:
> It contains at least one letter which repeats with exactly one letter between them, like `xyx`, `abcdefeghi` (`efe`), or even `aaa`.

`zd l zd` does not work, because it needs to be like `zlz`. `dlz` doesn't match the condition.
