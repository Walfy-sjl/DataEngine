'''
Action2: 统计全班的成绩
班里有5名同学，现在需要你用Python来统计下这些人
在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，
得出名次进行成绩输出（可以用numpy或pandas）
'''

import numpy as np
import pandas as pd

class ClassGrade:
    def numpyMethod(self):
        student = np.dtype({
            'names': ['姓名', '语文', '数学', '英语', 'Total'],
            'formats': ['U32', 'i', 'i', 'i', 'i']
        })
        students = np.array([
            ("张飞", 68, 65, 30, 0),
            ("关羽", 95, 76, 98, 0),
            ("刘备", 98, 86, 88, 0),
            ("典韦", 90, 88, 77, 0),
            ("许诸", 80, 90, 90, 0)
        ], dtype=student)
        chinese = students[:]['语文']
        math = students[:]['数学']
        english = students[:]['英语']
        students[:]['Total'] = students[:]['语文'] + students[:]['数学'] + students[:]['英语']
        print(students)
        print('班级各学科中的平均成绩、最小成绩、最大成绩、方差、标准差:----------------')
        print('{} | {} | {} | {} | {}   | {}'.format('科目', '平均成绩', '最小成绩', '最大成绩', '方差', '标准差'))
        self.numpyprint("语文", chinese)
        self.numpyprint("数学", math)
        self.numpyprint("英语", english)
        print(np.sort(students, order='Total')[::-1])

    def numpyprint(self, name, grade):
        print('{} | {}   | {}     | {}       | {}  | {}'.format(name,
                                                                np.mean(grade), np.min(grade), np.max(grade),
                                                                format(np.var(grade), ".1f"),
                                                                format(np.std(grade), ".1f")))

    def pandasMethod(self):
        df = pd.DataFrame({"姓名": ["张飞", "关羽", "刘备", "典韦", "许诸"], \
                           "语文": [68, 95, 98, 90, 80], \
                           "数学": [65, 76, 86, 88, 90], \
                           "英语": [30, 98, 88, 77, 90]})
        # 基于当前列生成新列的计算方法。
        df['Total0'] = df.sum(axis=1)
        df['Total1'] = df['语文'] + df['数学'] + df['英语']
        # df['Total3'] = df.apply(lambda x: x.sum(), axis=1)
        df['Total2'] = df.apply(lambda x: x['语文'] + x['数学'] + x['英语'], axis=1)
        print('DataFrame:----------------')
        print(df)
        # print(df.describe())
        print('班级各学科中的平均成绩、最小成绩、最大成绩、方差、标准差:----------------')
        print('{} | {} | {} | {} | {}   | {}'.format('科目', '平均成绩', '最小成绩', '最大成绩', '方差', '标准差'))
        self.pandasprint("语文", df)
        self.pandasprint("数学", df)
        self.pandasprint("英语", df)
        df.sort_values(by='Total1', ascending=False, inplace=True)
        df['rank'] = range(1, 6)
        print(df)

    def pandasprint(self, name, df):
        # print(name, '\t', df[name].mean(), '\t', df[name].min(), '\t', df[name].max(), '\t',
        #       format(df[name].var(), ".1f"), '\t', format(df[name].std(), ".1f"))
        print('{} | {}   | {}     | {}       | {}  | {}'.format(name,
                                                                df[name].mean(), df[name].min(), df[name].max(),
                                                                format(df[name].var(), ".1f"),
                                                                format(df[name].std(), ".1f")))


if __name__ == "__main__":
    grade1 = ClassGrade()
    print('-------numpy method--------------')
    grade1.numpyMethod()
    print('-------pandas method--------------')
    grade1.pandasMethod()
