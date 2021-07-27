# Section 3 - 17 Using Pig And Using Scripts

- `Pig` sits on top of MapReduce, and uses Pig Latin which looks alot like SQL. A very simple way of writing scripts.
- You can set up different relations on your data, so it is a more compact way of using MapReduce and translate that to MapReduce Tasks
- Pig can let you use your own user-defined functions for running your functions, with `Tez` for example.
- Pig running ontop of Tez may run 10x faster then just running it with MapReduce
- We can run the Pig script on either the MapReduce or TEZ. TEZ is much more effective way of  organizing these jobs with the use of a directed acyclic graphs.
- Unlike MapReduce which has mapper and then reducer and chain of it, TEZ will build a graph out the jobs and find the repeated task and their interdependencies and will find the optimal path to do that job. 10x faster than MapReduce.

## Running Pig

1) you can do it with Grunt (A command line interpreter) `pig` which will open the `grunt>` repl.
2) running it with pig script file name `pig <filename>`
3) and also running it with Ambari UI
