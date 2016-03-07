# acci2csdict
AutoCAD color index to csharp 6.0 dictionary converter

## usage

python acci2csdict.py

## requirements

python2.7 and well formatted input file acci.in

```
$ head acci.in && echo ... && tail acci.in
0       0       0       0       0       0       0
FF      0       0       1       255     0       0
FF      FF      0       2       255     255     0
0       FF      0       3       0       255     0
0       FF      FF      4       0       255     255
0       0       FF      5       0       0       255
FF      0       FF      6       255     0       255
FF      FF      FF      7       255     255     255
41      41      41      8       65      65      65
80      80      80      9       128     128     128
...
68      0       19      246     104     0       25
68      45      4E      247     104     69      78
4F      0       13      248     79      0       19
4F      35      3B      249     79      53      59
33      33      33      250     51      51      51
50      50      50      251     80      80      80
69      69      69      252     105     105     105
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
