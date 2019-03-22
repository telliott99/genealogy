### Scripting

#### Demo

The Python script **plot.py** can be invoked with any person's name (if they're in the database) to build a tree for them out to a specified depth.

```
> python plot.py "Gene" -b 1898 -d 10
g3  .  .  .  Gene Fowler 1898
..
```

These programs should run on both Mac and PC, as long as the path to the **scripts** directory is set correctly.  If you have the project downloaded to a Mac, you can make this work with just a little fiddling.

Launch Terminal to get a command line.  (From the Launchpad type "T" into the search box, choose Terminal).

You should get something like:

```
Toms-MacBook-Air-2:~ telliott_admin$ " 
```

The ``$`` and stuff before it are the "prompt".  Some people prefer a shorter version.  One way to do that is to enter this and hit RET:

```
Toms-MacBook-Air-2:~ telliott_admin$ export "PS1=> " 
> 
```

Now, "> " is your prompt.

We must tell Python where the project lives, or move to that directory.  We will do the latter here.  I enter the path for my installation:

```
> cd ~/Dropbox/Github/genealogy/scripts
```

``~`` is an alias for my home directory, ``/Users/telliott_admin``.

You should modify this for your own case.

The Terminal screen shows our input with a leading ``>``, which distinguishes user input:

```
> cd /Users/telliott_admin/Dropbox/Github/genealogy
>
```

Check where we are by entering the command ``pwd``.  Now the screen looks like this:

```
> cd /Users/telliott_admin/Dropbox/Github/genealogy/scripts
> pwd
/Users/telliott_admin/Dropbox/Github/genealogy/scripts
>
``` 

Next, run the script:

```
> python plot.py "Thomas Anthony Elliott" -d 2
g1  .  Thomas Anthony Elliott 1955
g2  .  .  Norman Elliott 1923
g3  .  .  .  James Edgar Elliott 1890
g3  .  .  .  Jessie Metcalf 1892
g2  .  .  Jean Francis Foster 1925
g3  .  .  .  James Heflin Foster 1889
g3  .  .  .  Gene Fowler 1898
>
```

``script.py`` has help:

```
> python plot.py -h
usage: plot.py [-h] [-b BORN] [-d DEPTH] [-l LINKS] name

Plot a family tree

positional arguments:
  name                  name of the individual

optional arguments:
  -h, --help            show this help message and exit
  -b BORN, --born BORN  birth year of the individual
  -d DEPTH, --depth DEPTH
                        depth of search
  -l LINKS, --links LINKS
                        provide links
> 
```

That's it.

The example uses the database which is output from ``dump.py``.  That script is also in the scripts folder.  You could run **dump.py** now like this. 

```
> python dump.py 
..
Rebecca Copp
b 1605
d 1660
f *
m *
o John Garde
g14/rebecca_copp.md

>

```

Most of the output has been clipped, this is the last entry.

If you want to save this version and then use it going forward instead of the one I provided, do this:

```
python dump.py > db.txt
```

The result is a file ``db.txt`` that you could copy to the database folder.