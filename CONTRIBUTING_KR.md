# 기여 활동

저희는 누구나로부터의 pull request도 환영할 준비가 되어있습니다. 이 저장소에 기여 함으로써, 당신은 [code of conduct]
를 준수하는 것에 동의 한것입니다.(CODE_OF_CONDUCT.md).

## 시작하기 

* 우선 이 저장소를 [fork][fork] 하시고, 이를 사용하기 위해서 해주세요:

    git clone git@github.com:your-username/algorithms.git  

* 그리고 당신의 변화들을 만들기 위한 branch를 만들어주세요. 예를 들어:  
  * add_XXX 만약 당신이 새로운 알고리즘이나 자료 구조를 추가 했을 경우.  
  * fix_XXX 만약 당신이 어떤 알고리즘이나 자료 구조에서 고쳐야할 bug를 발견했을 경우.  
  * test_XXX 만약 당신이 test/s를 작성한 경우.  

당신은 다음과 같이 기여할 수 있습니다:
- repo에 새로운 알고리즘들을 성립하세요. 단, 그것이 정확한 섹션 아래에 있도록 하세요(e.g. [array](array), [dp](dp), etc).
만약 어떤 섹션에도 포함이 되지 않을 경우, 이를 위한 새로운 섹션을 만드세요. 단, 당신의 알고리즘이 확실히 작동함을
확인하세요.  
- 존재하는 알고리즘을 최적화하거나 향상시켜주세요.
- 문제에 대한 다른 해결법을 추가해주세요.
- 버그들을 찾거나 고쳐주세요.
- 더 다은 알고리즘들을 설명하기 위해 예시들을 추가해주세요.
- 실험 예시들을 추가해주세요.

## Pull Requests
Push to your fork and [submit a pull request][pr].

We will review and may suggest some changes or improvements or alternatives.
Some things that will increase the chance that your pull request is accepted:

* All algorithms should be written in **Python 3**.
(There are a few algorithms still in _Python 2_ syntax. You can start by converting
[those][issue120] to _Python 3_.)
* Write clean and understandable code.
* Properly comment the code and briefly explain what the algorithm is doing in the [docstrings][docstr].
* You may also explain the output using a minimal example.
* Try to also include a couple of test cases for the algorithm.
* Write a [good commit message][commit].


## Issues
Submit a [new issue][newissue] if there is an algorithm to add, or if a bug was found in an existing algorithm. Before submitting a new issue please review the [existing issues][issues] to avoid creating duplicates. Also, consider resolving current issues or contributing to the discussion on an issue.

## Collaborators
You can ask for any help or clarifications from the collaborators.  
[Keon Kim](https://github.com/keon)

[Rahul Goswami](https://github.com/goswami-rahul)

[Ankit Agarwal](https://github.com/ankit167)

[Hai Hoang Dang](https://github.com/danghai)

[Saad](https://github.com/SaadBenn)

[fork]: https://help.github.com/articles/fork-a-repo/
[docstr]: https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings
[commit]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[pr]: https://github.com/keon/algorithms/compare/
[newissue]: https://github.com/keon/algorithms/issues/new
[issue120]: https://github.com/keon/algorithms/issues/120
[issues]: https://github.com/keon/algorithms/issues/
