# 0x07. Python - Test-driven development

## Meaning of Unit Testing
According to [Wikipedia](https://en.wikipedia.org/wiki/Unit_testing), unit testing is a software testing method by which individual units of source code—sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures—are tested to determine whether they are fit for use. 

Testing is crucial in the software development phase. It helps ensure easy debugging, agile code, and enhanced reusability. Performing tests that cover all use cases helps prevent a codebase from breaking — minimizing exposure to vulnerabilities.[Mattermost](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/) In this lesson, we explored testing of softwares in development using Python modules.


## Python Testing Modules

### doctest - Test interactive Python examples
The [doctest](https://docs.python.org/3/library/doctest.html) module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. The following are some of the ways to use doctest:

- To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
- To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
- To write tutorial documentation for a package, liberally illustrated with input-output examples.

### unittest - Unit testing framework
This module supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

## Reference Resources
- [Wikipedia](https://en.wikipedia.org/wiki/Unit_testing)
- [Mattermost](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)
- [Python Doctest Documentation](https://docs.python.org/3/library/doctest.html)
- [Python Unit Test Documentation](https://docs.python.org/3/library/unittest.html)
- [Python Tutorial: Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI)
