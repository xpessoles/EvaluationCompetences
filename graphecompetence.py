# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:05:28 2021

@author: xpess

Graphe pour une compétence
"""

import matplotlib.pyplot as plt
ti_comp  = "B2-3"
notes = [10, 25, 75, 50, 100]
dates = ["01/01/2021", "01/02/2021", "01/03/2021", "01/04/2021", "01/05/2021"]
type_eval = ["Colle", "DS", "DDS", "DS", "DS"]


notes_DS = [25, 50, 100]
dates_DS = ["01/02/2021", "01/04/2021", "01/05/2021"]

notes_colles = [10]
dates_colles = ["01/01/2021"]

notes_DDS = [75]
dates_DDS = ["01/03/2021"]

labels = dates
val = notes
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()


ax.bar(labels, val, width)

ax.bar(dates_DS, notes_DS, width, label='DS')
ax.bar(dates_colles, notes_colles, width, label='Colles')
ax.bar(dates_DDS, notes_DDS, width, label='DDS')


ax.plot(labels, val)
ax.scatter(labels, val)


ax.set_ylabel('Scores')
ax.set_title(ti_comp)
ax.legend()

plt.show()