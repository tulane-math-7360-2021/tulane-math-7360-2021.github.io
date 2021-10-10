import os

if __name__ == "__main__":
    student_names = [
        "Daniela-Florez",
        "Cong-Zhao",
        "Viraj-Puri",
        "Nadim-Hashmeh",
        "Danting-Li",
        "Zhipeng-Chen",
        "Abigail-Zion",
        "Haoqi-Chen",
        "Christian-Frederiksen",
        "Zehao-Wang",
        "Alan-Braeley",
        "Keyan-Chen",
        "Jose-Silvestre",
        "Rebekah-Albach",
        "Travis-McDonald",
        "Haiyu-Niu",
        "Yuwei-Bao",
        "Oliver-Orejola",
        "Paul-Pluscht"
    ]

    git_repos = os.getcwd()
    git_link = "https://github.com/tulane-math-7360-2021/Math-7360-XXXX-XXXX.git"
    for student_name in student_names[1:]:
        git_repo = git_repos + '/Math-7360-' + student_name
        if not os.path.isdir(git_repo):
            git_clone_cmd = 'git clone ' + git_link.replace("XXXX-XXXX", student_name)
            os.system(git_clone_cmd)
        else:
            git_pull_cmd = 'git pull'
            os.chdir(git_repo)
            os.system(git_pull_cmd)

        commit_cmd = "git commit -m 'add hw1 grade'"
        os.chdir(git_repo)
        os.system('pwd')
        os.system(commit_cmd)
        os.system('git push')

