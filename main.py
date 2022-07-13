
from time import time
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('私の超入門')
st.write("本文")

#### progress(進歩) iteration(反復)#######
'start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

##### progress(進歩)#####

#### checkbox #######
img = Image.open('kim.jpg')

if st.checkbox("show image"):
    st.image(img, caption="kimura", use_column_width=True)

st.write('display Image')
#### checkbox #######

#### Selectbox #######
option = st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は、',option, 'です。'

#### Selectbox #######

#### Textbox #######
'あなたの趣味はなんですか？'
text = st.text_input('趣味は？')
'私の趣味は、',text,'です。'
#### Textbox #######

#### Slider #######''
slider = st.slider('スライダー',1,100,50)
'あなたの',slider,'です。'
#### Slider #######

#### SideBar Slider #######''

sslider = st.sidebar.slider('サイドバースライダー',1,100,50)
'あなたの',sslider,'です。'

#### SideBer Slider #######



#### expander #######

#left_column, right_column = st.beta_columns(2)

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右からむです')

#Please replace st.beta_columns with st.columns.
#st.beta_columns will be removed after 2021-11-02.

#### Column #######





#df = pd.dataframe({'一列目':[1, 2, 3, 4],'二列目':[120, 75, 44, 200]})
#https://note.nkmk.me/python-pandas-dataframe-values-columns-index/
# https://ai-inter1.com/pandas-dataframe_basic/
# 

#dict1=dict(Row1=[1,21,31], Row2=[2,22,32], Row3=[3,23,33])
#df = pd.DataFrame(data=dict1)

df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['col_0', 'col_1', 'col_2', 'col_3'],
                  index=['row_0', 'row_1', 'row_2'])

# st.write(df)
#st.dataframe(df.style.highlight_min(axis=1),width = 300, height= 250)

st.table(df.style.highlight_max())

dff = pd.DataFrame(
    np.random.rand(20,3),
    columns=["aa","bb","cc"]
)

st.dataframe(dff)
st.line_chart(dff)
st.area_chart(dff)
st.bar_chart(dff)

dfff= pd.DataFrame(
    np.random.rand(100, 2) / [50,50]+[35.69,139.70],
    columns= ["lat","lon"]
)

st.dataframe(dfff)
st.map(dfff)
"""
#  松
## 竹
###  梅
#### 並
"""
"""
 python
import numpy as np
import pandas as pd

"""
