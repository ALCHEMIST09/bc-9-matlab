# bc-9-matlab

The project involves creating a mini-matlab clone, a REPL, without using any third-party libraries for lexing and parsing, or even doing mathematical computations. It there relies heavily on creating simple parses using string functions and regular expressions, and also
being able to do advanced list manipulation operations using both in-built and custom functions.

The project makes use of one main base class, [CMD](https://docs.python.org/3/library/cmd.html), which is an in-built python module. The CMD class has a pre_defined structure for declaring methods for classes that extend it, making it become a serious hindrance to the developer since, it can only accept one argument per method.

By overidding the 'default()' method of the base class in your classes, you can implement custom functionality that moves away from rigid structure of the parent class.
