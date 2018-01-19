# How to Contribute

`isbnlib` has a very small code base, so it is a good project to begin your
adventure in open-source.

> **NOTE**: By contributing you agree with the [license terms](LICENSE-LGPL.txt)
  (**LGPL v3**) of the project.


## Main Steps

1. Make sure you have a [GitHub account](https://github.com/signup/free)
2. Submit a ticket for your issue or idea
   ([help](https://www.youtube.com/watch?v=TJlYiMp8FuY)),
   on https://github.com/xlcnd/isbnlib_porbase/issues,
   (if possible wait for some feedback before any serious commitment... :)
3. **Fork** the repository on GitHub and **clone it locally**
   ([help](https://help.github.com/articles/fork-a-repo)).
4. `pip install -r requirements-dev.txt` (at your local directory).
5. Do your code... (**remember the code must run on python 2.6, 2.7, 3.3, 3.4, 3.5, 3.6
   and be OS independent** It is easier if you start to write in python 3 and then
   adapt for python 2) (you will find [Travis](https://travis-ci.org) very handy for
   testing with this requirement!)
6. Write tests for your code using `nose` and put then in the directory `isbnlib_porbase/test`
7. Pass **all tests** and with **coverage > 90%**.
   Check the coverage in [Coveralls](https://coveralls.io) or locally with the command
   `nosetests --with-coverage --cover-package=isbnlib_porbase`.
8. **Check if all requirements are fulfilled**!
9. **Push** your local changes to GitHub and make there a **pull request**
   ([help](https://help.github.com/articles/using-pull-requests/))
   **using `dev` as base branch** (by the way, we follow the *fork & pull* model with this small change).

> **NOTE**: *Travis*, *coverage* and *flake8*, have already
configuration files adapted to the project.

## Style

Your code **must** be [PEP8](http://legacy.python.org/dev/peps/pep-0008/) compliant
and be concise as possible (use `yapf` then check it with
`flake8` and `pylint`).

Use doc strings ([PEP257](http://legacy.python.org/dev/peps/pep-0257/))
for users and comments (**few**) as signposts
for fellow developers. Make your code as clear as possible.


## Red Lines

**Don't submit pull requests that are only comments to the code that is
already in the repo!**

**No** doc tests! Remember point 6 above.

**Don't** submit pull requests without checking point 8!



## Important

If you don't have experience with these issues, don't be put off by these requirements,
see them as a learning opportunity. Thanks!
