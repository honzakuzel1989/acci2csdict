# acci2csdict
AutoCAD color index to csharp 6.0 dictionary converter

## usage

python acci2csdict.py

## requirements

python2.7 and well formatted input file acci.in

```
$ head -n 6 acci.in && echo ... && tail -n 3 acci.in
0       0       0       0       0       0       0
FF      0       0       1       255     0       0
FF      FF      0       2       255     255     0
0       FF      0       3       0       255     0
0       FF      FF      4       0       255     255
0       0       FF      5       0       0       255
...
82      82      82      253     130     130     130
BE      BE      BE      254     190     190     190
FF      FF      FF      255     255     255     255
```

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
...
[254] = Color.FromRgb(190, 190, 190),
[255] = Color.FromRgb(255, 255, 255),
};
```

### 2

```
$ python acci2csdict.py > csdict.out
$ head -n 6 csdict.out && echo ... && tail -n 3 csdict.out
private static IDictionary<int, Color> acci2brush = new Dictionary<int, Color>()
{
[0] = Color.FromRgb(0, 0, 0),
[1] = Color.FromRgb(255, 0, 0),
[2] = Color.FromRgb(255, 255, 0),
[3] = Color.FromRgb(0, 255, 0),
...
[254] = Color.FromRgb(190, 190, 190),
[255] = Color.FromRgb(255, 255, 255),
};
```
