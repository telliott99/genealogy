#### Database

I have written a Python script to collect all the data (scrape) from the directories here and write it to a single text file [here](../database/db.txt).  It looks like this:

```
Thomas Anthony Elliott
b 1955
d *
f Norman Elliott
m Jean Francis Foster
o Meenal Bhopatkar
o Joan Carlyn Olson
g1/thomas_anthony_elliott.md
```

I wrote another Python script to search for a particular individual and then print out ancestors to a given depth.  Currently, it looks like this:

```
> python plot.py -n "James Heflin" -d 4
g3 .  .  .  James Heflin Foster 1889
g4 .  .  .  .  William Long Foster 1861
g5 .  .  .  .  .  James Martin Foster 1831
g6 .  .  .  .  .  .  Flavel Foster 1801
g7 .  .  .  .  .  .  .  *
g7 .  .  .  .  .  .  .  Elizabeth Foster 1777
g6 .  .  .  .  .  .  Mary Amelia Hollingsworth 1802
g7 .  .  .  .  .  .  .  Jacob Hollingsworth
g7 .  .  .  .  .  .  .  Sarah Martin 1783
g5 .  .  .  .  .  Mary Eleanor Long 1842
g6 .  .  .  .  .  .  William Long
g7 .  .  .  .  .  .  .  *
g7 .  .  .  .  .  .  .  *
g6 .  .  .  .  .  .  Emily C. Boggs
g7 .  .  .  .  .  .  .  John Boggs
g7 .  .  .  .  .  .  .  Hannah Maria Cook 1802
g4 .  .  .  .  Launa Mims Davis 1865
g5 .  .  .  .  .  Lewis Richard Davis 1827
g6 .  .  .  .  .  .  James C. Davis 1801
g7 .  .  .  .  .  .  .  Lewis Cookson Davis 1757
g7 .  .  .  .  .  .  .  Sarah Sally Perkins 1777
g6 .  .  .  .  .  .  Elizabeth Davis 1805
g7 .  .  .  .  .  .  .  *
g7 .  .  .  .  .  .  .  *
g5 .  .  .  .  .  Alabama Frances Mims 1825
g6 .  .  .  .  .  .  Seaborn Jones Mims 1787
g7 .  .  .  .  .  .  .  Shadrach Mims 1764
g7 .  .  .  .  .  .  .  Elizabeth Kirkham 1751
g6 .  .  .  .  .  .  Elizabeth Hubbard Saunders 1792
g7 .  .  .  .  .  .  .  Ephraim Saunders
g7 .  .  .  .  .  .  .  Ann McCarty {Nancy}
>
```

We see only five missing values, for individuals who should be there (at this depth of search), but the names are not known.

The same output for my father's side shows how much work there is left to do.  The only name I have beyond what he uncovered is Alanson Elliott's father, and he already knew that too.

Here is the entire thing, at the command line we do:

```
> python plot.py -n "Thomas" -y 1955 -d 14 > full.txt
```

and see [this](../trees/full.txt) result.

This is mostly here so you can admire the very first part, the progression:

```
g1  .  Thomas Anthony Elliott 1955
g2 .  .  Norman Elliott 1923
g3 .  .  .  James Edgar Elliott 1890
g4 .  .  .  .  David Marion Elliott 1854
g5 .  .  .  .  .  Alanson Elliott 1815
g6 .  .  .  .  .  .  David Elliott 1784
g7 .  .  .  .  .  .  .  David Elliott 1744
g8 .  .  .  .  .  .  .  .  David Elliott 1716
g9 .  .  .  .  .  .  .  .  .  Daniel Elliott 1687
g10 .  .  .  .  .  .  .  .  .  . Daniel Elliott 1662
g11 .  .  .  .  .  .  .  .  .  .  . Daniel Elliott 1640
g12 .  .  .  .  .  .  .  .  .  .  .  . *
```