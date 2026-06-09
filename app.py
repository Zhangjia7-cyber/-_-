import streamlit as st

ELEMENTS = {
    '火': {'color': '#FF6B35', 'name': '火元素', 'description': '热情、勇敢、充满活力'},
    '水': {'color': '#4ECDC4', 'name': '水元素', 'description': '温柔、感性、富有同理心'},
    '土': {'color': '#8B4513', 'name': '土元素', 'description': '踏实、稳重、注重实际'},
    '风': {'color': '#87CEEB', 'name': '风元素', 'description': '聪明、好奇、善于思考'}
}

QUESTIONS = [
    {
        'question': '当你遇到困难时，你通常会怎么做？',
        'options': [
            {'text': '直接面对，积极寻找解决方案', 'element': '火'},
            {'text': '先冷静分析，再制定计划', 'element': '风'},
            {'text': '寻求他人帮助和支持', 'element': '水'},
            {'text': '按部就班，逐步推进', 'element': '土'}
        ]
    },
    {
        'question': '你更喜欢哪种环境？',
        'options': [
            {'text': '热闹的聚会或活动', 'element': '火'},
            {'text': '安静的图书馆或书房', 'element': '风'},
            {'text': '温馨的家庭氛围', 'element': '水'},
            {'text': '自然的户外环境', 'element': '土'}
        ]
    },
    {
        'question': '朋友对你的评价最可能是？',
        'options': [
            {'text': '热情开朗，充满活力', 'element': '火'},
            {'text': '聪明睿智，善于分析', 'element': '风'},
            {'text': '善解人意，体贴周到', 'element': '水'},
            {'text': '可靠踏实，值得信赖', 'element': '土'}
        ]
    },
    {
        'question': '学习新技能时，你倾向于？',
        'options': [
            {'text': '快速上手，边做边学', 'element': '火'},
            {'text': '先理解原理，再实践', 'element': '风'},
            {'text': '在他人指导下学习', 'element': '水'},
            {'text': '循序渐进，打好基础', 'element': '土'}
        ]
    },
    {
        'question': '做决策时，你更看重？',
        'options': [
            {'text': '直觉和激情', 'element': '火'},
            {'text': '逻辑和理性', 'element': '风'},
            {'text': '他人的感受', 'element': '水'},
            {'text': '实际的结果', 'element': '土'}
        ]
    }
]

def main():
    st.set_page_config(page_title='元素人格测试仪', page_icon='🔮', layout='wide')
    
    st.title('🔮 元素人格测试仪')
    st.subheader('探索你的内在元素属性')
    
    if 'answers' not in st.session_state:
        st.session_state.answers = []
        st.session_state.current_question = 0
        st.session_state.result = None
    
    if st.session_state.result is None:
        current_q = QUESTIONS[st.session_state.current_question]
        
        st.progress((st.session_state.current_question + 1) / len(QUESTIONS))
        st.write(f'问题 {st.session_state.current_question + 1}/{len(QUESTIONS)}')
        st.write(f'**{current_q["question"]}**')
        
        for option in current_q['options']:
            if st.button(option['text'], key=f'q{st.session_state.current_question}_{option["element"]}'):
                st.session_state.answers.append(option['element'])
                if st.session_state.current_question < len(QUESTIONS) - 1:
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    calculate_result()
                    st.rerun()
    else:
        show_result()

def calculate_result():
    element_counts = {'火': 0, '水': 0, '土': 0, '风': 0}
    for answer in st.session_state.answers:
        element_counts[answer] += 1
    
    max_count = max(element_counts.values())
    dominant_elements = [elem for elem, count in element_counts.items() if count == max_count]
    
    if len(dominant_elements) > 1:
        st.session_state.result = {
            'type': '混合元素',
            'elements': dominant_elements,
            'description': '你是多种元素的混合体，拥有丰富多样的个性特质'
        }
    else:
        dominant_element = dominant_elements[0]
        st.session_state.result = {
            'type': ELEMENTS[dominant_element]['name'],
            'elements': [dominant_element],
            'description': ELEMENTS[dominant_element]['description']
        }

def show_result():
    result = st.session_state.result
    
    st.success(f'🎉 测试完成！')
    st.subheader(f'你的人格类型：{result["type"]}')
    
    for element in result['elements']:
        st.markdown(
            f'<div style="background-color:{ELEMENTS[element]["color"]}20; padding:20px; border-radius:10px; margin:10px 0;">'
            f'<h3 style="color:{ELEMENTS[element]["color"]};">{ELEMENTS[element]["name"]} 🔮</h3>'
            f'<p>{ELEMENTS[element]["description"]}</p>'
            '</div>',
            unsafe_allow_html=True
        )
    
    st.write(result['description'])
    
    st.subheader('元素特性详解：')
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'🔥 **{ELEMENTS["火"]["name"]}**')
        st.write('代表热情、勇气和行动力')
        
        st.markdown(f'💧 **{ELEMENTS["水"]["name"]}**')
        st.write('代表情感、直觉和同理心')
    
    with col2:
        st.markdown(f'🌍 **{ELEMENTS["土"]["name"]}**')
        st.write('代表稳定、务实和责任感')
        
        st.markdown(f'💨 **{ELEMENTS["风"]["name"]}**')
        st.write('代表智慧、沟通和创新思维')
    
    if st.button('重新测试'):
        st.session_state.answers = []
        st.session_state.current_question = 0
        st.session_state.result = None
        st.rerun()

if __name__ == '__main__':
    main()