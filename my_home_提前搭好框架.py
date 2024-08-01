'''我的主页'''
import time
import streamlit as st
import base64
from PIL import Image


page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的留言区', '跳转', '我的智慧词典'])
def page_1():
    '''我的兴趣推荐'''
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100,'加载完毕!')
    st.write("<span style='font-size:50px; color:black'>我喜欢的电影推荐:</span>", unsafe_allow_html=True)
    st.write("<span style='font-size:25px; color:red'>流浪地球</span>", unsafe_allow_html=True)
    st.image('流浪地球1.png')
    st.write("<span style='font-size:25px; color:red'>功夫熊猫</span>", unsafe_allow_html=True)
    st.image('功夫熊猫.png')
    st.write("<span style='font-size:25px; color:red'>哈利·波特</span>", unsafe_allow_html=True)
    st.image('哈利波特1.png')
    st.write("<span style='font-size:50px; color:black'>我喜欢的小说推荐:</span>", unsafe_allow_html=True)
    st.write("<span style='font-size:25px; color:red'>三体:</span>", unsafe_allow_html=True)
    st.image('三体.png')
    st.write("<span style='font-size:25px; color:red'>哈利·波特</span>", unsafe_allow_html=True)
    st.image('哈利波特2.png')
    '''我的爱好'''
    st.write("<span style='font-size:25px; color:red'>下象棋</span>", unsafe_allow_html=True)
    st.image('中国象棋.png')
    st.image('国际象棋.png')
    st.write("<span style='font-size:25px; color:red'>打羽毛球</span>", unsafe_allow_html=True)
    st.image('羽毛球.png')
    st.write("<span style='font-size:25px; color:red'>骑自行车</span>", unsafe_allow_html=True)
    st.write('骑自行车')
    st.image('自行车.png')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))



def page_3():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
def page_4():
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['优酷', '我的bilibili'])
    if go == '优酷':
        st.link_button('帮我充会员(dog', 'https://www.youku.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')

def page_5():
    '''我的智慧词典'''
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的留言区':
    page_3()
elif page == '跳转':
    page_4()
elif page == '我的智慧词典':
    page_5()
