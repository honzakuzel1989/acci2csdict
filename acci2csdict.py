#!/usr/bin/env python

#Vstupni soubor: acci.in
#Struktura vstupu: 256 radku se sedmi sloupci oddelenych tabulatorem (\t) - C&P z 
#   http://www.isctex.com/acadcolors.php nebo http://sub-atomic.com/~moses/acadcolors.html
#   s nasledujicim vyznamem 0xRed 0xGreen 0xBlue ColorIndex Red	Green	Blue
#Struktura vystupu:
#   private static IDictionary<int, Color> accci2brush = new Dictionary<int, Color>()
#   {
#     [ColorIndex] = Color.FromRgb(Red, Green, Blue),
#     //...
#   };

lines = []
inFile = 'acci.in'

with open(inFile) as f:
  lines = [line.rstrip('\n').rstrip('\r') for line in f.readlines()]

print "private static IDictionary<int, Color> acci2brush = new Dictionary<int, Color>()"
print "{"
  
for line in lines:
  items = line.split('\t')
  print "[{}] = Color.FromRgb({}, {}, {}),".format(*items[3:])

print "};"
