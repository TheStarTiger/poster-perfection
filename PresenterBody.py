import TensorPlay as tp
import numpy as np
import tensorflow as tf
from tensorflow import keras as kr
from pptx.util import Inches, Pt
from pptx import Presentation


head = [72, 1, 1, 0, "Arial Black", []]
subhead = [45, 0, 1, 0, "Arial", []]
subsec = [28, 0, 1, 0, "Georgia", []]
body = [28, 0, 0, 0, "Georgia", []]
subtitle = [20, 0, 0, 1, "Arial", []]
classific = [head, subhead, subsec, body, subtitle]

model = kr.Sequential([
  kr.layers.Dense(17, input_shape=(17, ), activation='relu'),
  kr.layers.Dense(5,input_shape=(5, ), activation='softmax')
])

model = kr.models.load_model('trained_text_model.h5')
pres_runs = []
input_data, prs1, avg_col = tp.pptx_data('thissatest.pptx', pres_runs)

# Assigning color schemes happens here, according to the average color and such
col_scheme = tp.color_scheme_translate(avg_col)
classific[0][-1] = col_scheme[0]
classific[1][-1] = col_scheme[1]
classific[2][-1] = col_scheme[2]
classific[3][-1] = classific[4][-1] = col_scheme[3]

np_assign = model.predict(input_data)



assert np_assign.shape[0] == np.array(pres_runs).shape[0]

#print(np_assign)


def implement_assigns(np_array):
    for index, val in enumerate(np_array):
        assigned = np.argmax(val)
        pres_runs[index].font.size = Pt(classific[assigned][0])
        #print(pres_runs[index].font.size)
        pres_runs[index].font.name = classific[assigned][4]
        # Body check for bolding to ensure subheads and highlighting remains
        if not (assigned == 3 and pres_runs[index].font.bold is True):
            pres_runs[index].font.bold = bool(classific[assigned][2])
        pres_runs[index].font.italic = bool(classific[assigned][3])
        pres_runs[index].font.underline = False
        pres_runs[index].font.color.rgb = classific[assigned][-1]
        #print("font is " + str(pres_runs[index].font.name))


implement_assigns(np_assign)
prs1.save('test2.pptx')


