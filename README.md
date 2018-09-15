#### Project notes

This project is an attempt to record the genealogy of my family in a central online location.  The initial commit is based on the family tree constructed by my father, Norman Elliott [see here](figs/ne_genealogy.png).

The hope is that this will be revised and extended in the future.

It may look weird if you are not used to it.  The format is [markdown](https://en.wikipedia.org/wiki/Markdown), which supports links but is much easier for humans to write than html.  It allows easy incorporation of a variety of material including photos, text, and external web pages.

I have suppressed the birth dates for living individuals, even though I consider this information to be hopelessly exposed to the internet already.

To start exploring, you could look at [my page](g1/thomas_anthony_elliott.md), or browse the folders.

#### Standard notation

There are three sections for each entry.

The first has six invariant lines:  generation as e.g. gen=g6, name in bold, born (b), died (d), father (f), mother (m).  These lines and identifiers are present even if there is no data.  

If a person was known by some familiar name it is added as {name}.  For a woman, her married (husband's) name is given in parentheses.

In the second section are listed marriages (I chose o as the symbol for that, to be distinguished from m for mother), and then children in a list.  If there's a second marriage they are just listed in order.

The third section is for any other data or references (or even pictures of people or their gravestones), and for discussion of discrepancies.

#### Database

I have written a Python script to collect all the data (scrape) from the directories here and write it to a single text file [here](database/db.txt).  It looks like this:

```g1
Thomas Anthony Elliott
Thomas Anthony Elliott 1955-*
Norman Elliott
Jean Francis Foster
g1/thomas_anthony_elliott.md
```

I wrote another Python script to search for a particular individual and then print out ancestors to a given depth.  [in progress]  It looks like this:

```
> python search.py "Jean"
Jean Francis Foster
    James Heflin Foster
        William Long Foster
            James Martin Foster
                James Martin Foster
                Mary Eleanor Long (Foster)
            Mary Eleanor Long (Foster)
                William Long Foster
                *
        Launa Mims Davis
            Lewis Richard Davis
                James C. Davis
                *
            Alabama Frances Mims (Davis)
                Seaborn Mims
                Elizabeth Hubbard Saunders (Mims) {Betsy}
    Gene Fowler
        Thompson Ernest Fowler
            Thompson Fletcher Fowler
                Levi Fowler
                Dinelah Huff (Fowler)
            Mildred Maria Kuykendall (Fowler) {Minnie}
                Abner Kuykendall
                Maria Duff (Kuykendall)
        Abigail Augusta Johnson (Fowler)
            Robert Mortimer Johnson
                William Johnson
                *
            Abby Ann West (Johnson)
                David West
                Lucinda Latimer (West)
>
```

The same output for my father's side shows how much work there is left to do:

```
> python search.py "Norman"
Norman Elliott
    James Edgar Elliott
        David Marion Elliott
            Alanson Elliott
                David Elliott
                *
            Sarah Fisher (Elliott)
                *
                *
        Clara Etta Main
            Lewis W. Main
                *
                *
            Lydia Catherine Roberts (Main)
                *
                *
    Jessie Metcalf
        Alberti Metcalf
            Edward Metcalf
                *
                *
            Mary Jane Thorpe (Metcalf)
                *
                *
        Lenora Fisher
            Henry J. Fisher
                *
                *
            Oceana Jackson (Fisher)
                *
                *
>
```

The only name I have beyond what he uncovered, is Alanson Elliott's father, and he already knew that too.

####  Some highlights:

I have found both parents for 9/16 of the g5 generation.  Altogether I have data for about 50 individuals beyond g5.

I have confirmation that Alanson Elliott's father David's father was a well-known David Elliott with a family extending to about 1651.  It is believed that Daniel Elliott was transported to the colonies after being on the losing side (he fought for the crown) in one of the battles the Scots fought against Cromwell in 1651.  His son is famous for testimony at the witchcraft trials in Salem.

As you may know, T.F. Fowler had the very good sense to spend the Civil War in California.  His second son with his first wife was born there.

I found Mama Gussie's mother's family.  Her mother was Abby Ann West and her grandfather was Major David West.  He fought with Andy Jackson at the battle of New Orleans.

Our ancestors include an Abner Kuykendall who is not the famous one of Stephen Austin's Old 300, but who was also a Texas Pioneer and fought in the Texas Revolution.  The famous Abner Kuykendall and ours share a gg grandfather.

I connected James Martin Foster (James Heflin's grandfather) with her mother, a Hollingsworth.  J.M.'s brother Flavel was killed at the Battle of Chancellorsville, 1864.  Several more ancestors were in the Confederate army.

I have Fowler, Hollingsworth and Kuykendall back to the immigrants in the 1600s.  One was here in 1646.  His name was Jacob Luursen van Kuykendall.  Actually, he was Jacob Luursen and he came from Kuykendall, Netherlands, but that's another story.