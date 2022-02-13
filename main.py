import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)


'Done!!'


# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# ＃表示の画面内での分割

# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く') 
#FAQ的な

# text = st.text_input('あなたの趣味を教えてください')
# condition_s = st.slider('あなたの今の調子は?',0,100,50)
# 'あなたの趣味：',text
# 'コンディション:',condition_s

#condition_s = st.slider('あなたの今の調子は?',0,100,50)
#'コンディション:',condition_s
#バーで数字を表示し選択できる

#text = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味：',text
#自分で入力して表示する

#if st.checkbox('Show Image'):
#    img = Image.open('雲見三競.jpg')
#    st.image(img,caption='sample',use_column_width=True)
#チェックボックスにより、表示するしないを制御する。

#option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,11))
#)
#'あなたの好きな数字は、',option,'です。'
#選択式で選べる



#df = pd.DataFrame({
#    '1列目':[1,2,3,4],
#    '2列目':[10,20,30,40]
#})

#折線グラフ

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns= ['lat','lon']
#)
#st.map(df)


#map
#⇒地図にマッピング

#line_chart
#arie_chartなど
#displaychartに記載されている

#st.dataframe(df.style.highlight_max(axis=0))

#write
#dataframe
#table
#⇒APIrefarenceを参照


#"""

# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

