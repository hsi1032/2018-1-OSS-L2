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
당신의 fork에 push 하고 pull request를 제출하세요 [submit a pull request][pr].

우리는 이를 검토할 것이며, 몇몇 변화, 개량, 대안을 제시할 수 도 있을 것입니다.
당신의 pull request가 허용될 가능성을 높여주는 몇몇 요소들이 있습니다:

* 모든 알고리즘들은 **Python 3**로 작성되어야 합니다.
(몇몇 알고리즘들은 여전히 _python 2_ 로 작성되어져 있습니다. 당신은 이를 전환 함으로써 기여를 시작할 수 도 있습니다.
[those][issue120] to _Python 3_.)
* 깔끔하고 이해할 수 있는 코드를 작성해주세요.
* 코드에 대해 올바르게 주석 처리 해 주시고, 간단하게 알고리즘이 [docstrings][docstr]에서 수행하는 작업을 설명해 주세요.
* 당신은 최소한의 예시를 사용함으로써 출력 값에 대하여 설명하실 수도 있습니다.
* 알고리즘에 대하여, 두가지의 test cases를 포함 할 수 있도록 해주세요.
* [good commit message][commit]를 .


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
