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

    git_link = "https://github.com/tulane-math-7360-2021/Math-7360-XXXX-XXXX.git"
    for student_name in student_names:
        git_repo = './Math-7360-' + student_name
        if not os.path.isdir(git_repo):
            git_clone_cmd = 'git clone ' + git_link.replace("XXXX-XXXX", student_name)
            os.system(git_clone_cmd)