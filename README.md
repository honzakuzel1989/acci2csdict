# acci2csdict
AutoCAD color index to csharp dictionary converter

## usage

python acci2csdict.py

## requirements

python2.7 and input file acci.in

## examlpes

### 1
```
$ python acci2csdict.py
private static IDictionary<int, Color> acci2brush = new Dictionary<int, Color>()
{
[0] = Color.FromRgb(0, 0, 0),
[1] = Color.FromRgb(255, 0, 0),
[2] = Color.FromRgb(255, 255, 0),
[3] = Color.FromRgb(0, 255, 0),
[4] = Color.FromRgb(0, 255, 255),
[5] = Color.FromRgb(0, 0, 255),
[6] = Color.FromRgb(255, 0, 255),
...
[253] = Color.FromRgb(130, 130, 130),
[254] = Color.FromRgb(190, 190, 190),
[255] = Color.FromRgb(255, 255, 255),
};
```

### 2

```
$ python acci2csdict.py > csdict.out
```
