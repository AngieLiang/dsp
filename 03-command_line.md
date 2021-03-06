# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>> * show current working directory path  
pwd  

>> * creating a directory  
mkdir dicname  

>> * deleting a directory  
rm -rf dicname

>> * creating a file using `touch` command  
touch filename  

>> * deleting a file  
rm filename  

>> * renaming a file  
mv oldname newname  

>> * listing hidden files  
alias hidden='ls -a | grep "^\."'

>> * copying a file from one directory to another  
cp filename1 filename2  

>> * Send file to printer  
lpr  

>> * Online manual (help) about command  
man  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> `ls` - Lists files in current directory.  
`ls -a` - Lists all files, including the ones whose filenames begin in a dot, which you do not always want to see.  
`ls -l` - Lists your files in 'long format', which contains lots of useful information.  
`ls -lh` - List files with human readable format with option.  
`ls -lah` - List all directory contents in human readable, long format.  
`ls -t` - Lists directory contents sorted by modification time.  
`ls -Glp` - `G` inhibits the display of group information, `l` displays the contents in long format, and `p` shows which files have an indicator such as '/'.  


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> `ls -r` - Displays files in reverse order.  
`ls -x` - Displays files as rows across the screen.  
`ls -q` - Displays all nonprinting characters as ?  
`ls -m` - Displays the names as a comma-separated list.  
`ls -f` - Interprets each name as a directory, not a file.  

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> `xargs` is a command on Unix and most Unix-like operating systems used to build and execute command lines from standard input.  
Example:  
`find /path -type f -print | xargs rm`  
In the above example, the `find` utility feeds the input of `xargs` with a long list of file names. `xargs` then splits this list into sublists and calls `rm` once for every sublist.

 

