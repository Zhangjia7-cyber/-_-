import streamlit as st

ELEMENTS = {
    '火': {
        'color': '#FF6B35',
        'name': '火元素',
        'description': '热情、勇敢、充满活力',
        'emoji': '🔥',
        'phrase': '燃烧吧！',
        'weakness': '急躁、冲动、缺乏耐心',
        'advice': '适当放慢节奏，学会倾听和等待，用运动或创意活动释放过剩能量',
        'advice_icon': '⚡'
    },
    '水': {
        'color': '#4ECDC4',
        'name': '水元素',
        'description': '温柔、感性、富有同理心',
        'emoji': '💧',
        'phrase': '放轻松~',
        'weakness': '情绪易波动、过度依赖他人、优柔寡断',
        'advice': '练习情绪管理，培养独立思考能力，尝试写日记或冥想稳定心绪',
        'advice_icon': '💧'
    },
    '土': {
        'color': '#8B4513',
        'name': '土元素',
        'description': '踏实、稳重、注重实际',
        'emoji': '🌍',
        'phrase': '稳如磐石~',
        'weakness': '固执、保守、缺乏灵活性',
        'advice': '主动尝试新事物，接受变化，每周做一件计划外的小冒险',
        'advice_icon': '🌱'
    },
    '风': {
        'color': '#87CEEB',
        'name': '风元素',
        'description': '聪明、好奇、善于思考',
        'emoji': '💨',
        'phrase': '自由飞翔~',
        'weakness': '想法多却执行力弱、容易分心、三分钟热度',
        'advice': '设定小目标并打卡完成，使用番茄工作法，将灵感落地为具体行动',
        'advice_icon': '💡'
    },
    '混合': {
        'color': '#9B59B6',
        'name': '混合元素',
        'description': '丰富多元、适应力强',
        'emoji': '🌟',
        'phrase': '独特魅力~',
        'weakness': '特质矛盾、难以自我定位',
        'advice': '接纳自己的多面性，在不同场合发挥不同特质，定期自我反思整合内在力量',
        'advice_icon': '🔮'
    }
}

QUESTIONS = [
    {
        'question': '当你遇到困难时，你通常会怎么做？',
        'emoji': '🤔',
        'options': [
            {'text': '⚡ 直接面对，积极寻找解决方案', 'element': '火'},
            {'text': '💡 先冷静分析，再制定计划', 'element': '风'},
            {'text': '🤝 寻求他人帮助和支持', 'element': '水'},
            {'text': '🛠️ 按部就班，逐步推进', 'element': '土'}
        ]
    },
    {
        'question': '你更喜欢哪种环境？',
        'emoji': '❓',
        'options': [
            {'text': '🎉 热闹的聚会或活动', 'element': '火'},
            {'text': '📚 安静的图书馆或书房', 'element': '风'},
            {'text': '🏠 温馨的家庭氛围', 'element': '水'},
            {'text': '🏕️ 自然的户外环境', 'element': '土'}
        ]
    },
    {
        'question': '朋友对你的评价最可能是？',
        'emoji': '💭',
        'options': [
            {'text': '🌟 热情开朗，充满活力', 'element': '火'},
            {'text': '🧠 聪明睿智，善于分析', 'element': '风'},
            {'text': '💝 善解人意，体贴周到', 'element': '水'},
            {'text': '🛡️ 可靠踏实，值得信赖', 'element': '土'}
        ]
    },
    {
        'question': '学习新技能时，你倾向于？',
        'emoji': '📖',
        'options': [
            {'text': '🚀 快速上手，边做边学', 'element': '火'},
            {'text': '🔬 先理解原理，再实践', 'element': '风'},
            {'text': '👥 在他人指导下学习', 'element': '水'},
            {'text': '📐 循序渐进，打好基础', 'element': '土'}
        ]
    },
    {
        'question': '做决策时，你更看重？',
        'emoji': '⚖️',
        'options': [
            {'text': '💫 直觉和激情', 'element': '火'},
            {'text': '🎯 逻辑和理性', 'element': '风'},
            {'text': '❤️ 他人的感受', 'element': '水'},
            {'text': '📊 实际的结果', 'element': '土'}
        ]
    }
]

def get_dynamic_avatar_html(element_key, size=150):
    """生成带动画的动态元素形象HTML"""
    elem = ELEMENTS[element_key]
    color = elem['color']
    emoji = elem['emoji']
    phrase = elem['phrase']
    
    return f'''
    <div class="element-avatar-container" id="avatar_{element_key}" 
         onclick="triggerClickFeedback('{element_key}')"
         onmouseenter="showBubble('{element_key}', '{phrase}')"
         onmouseleave="hideBubble('{element_key}')">
        <div class="avatar-wrapper">
            <div class="avatar-glow" style="background: {color};"></div>
            <div class="avatar-emoji" style="font-size: {size}px;">{emoji}</div>
            <div class="avatar-bubble" id="bubble_{element_key}">
                <div class="bubble-content">
                    <span class="bubble-emoji">{emoji}</span>
                    <span class="bubble-text">{phrase}</span>
                </div>
            </div>
        </div>
    </div>
    '''

def get_custom_css():
    """自定义CSS样式"""
    return '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap');
    
    * {
        font-family: 'Noto Sans SC', sans-serif;
    }
    
    /* 全局渐变背景 */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        min-height: 100vh;
    }
    
    /* 毛玻璃卡片 */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 30px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        animation: fadeIn 0.6s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.05); opacity: 0.8; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px currentColor; }
        50% { box-shadow: 0 0 40px currentColor, 0 0 60px currentColor; }
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* 标题样式 */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(120deg, #fff 0%, #f0f0f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: float 3s ease-in-out infinite;
        margin-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 30px;
        animation: fadeIn 1s ease-out;
    }
    
    /* 进度条样式 */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 10px;
    }
    
    /* 问题卡片 */
    .question-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 35px;
        margin: 25px 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    .question-text {
        font-size: 1.4rem;
        color: #fff;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    
    .question-emoji {
        font-size: 2.5rem;
        animation: bounce 2s ease-in-out infinite;
    }
    
    /* 选项按钮样式 */
    .stButton > button {
        width: 100%;
        padding: 18px 25px;
        margin: 12px 0;
        border-radius: 15px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        background: rgba(255, 255, 255, 0.15);
        color: white;
        font-size: 1.1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: scale(1.03);
        background: rgba(255, 255, 255, 0.3);
        border-color: rgba(255, 255, 255, 0.6);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
    }
    
    .stButton > button:active {
        transform: scale(0.98);
    }
    
    /* 结果页面 */
    .result-card {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(25px);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.2);
        animation: resultAppear 0.8s ease-out;
    }
    
    @keyframes resultAppear {
        from { opacity: 0; transform: scale(0.8) translateY(30px); }
        to { opacity: 1; transform: scale(1) translateY(0); }
    }
    
    /* 元素形象容器 */
    .element-avatar-container {
        display: inline-block;
        cursor: pointer;
        transition: transform 0.3s ease;
        position: relative;
    }
    
    .element-avatar-container:hover {
        transform: scale(1.15);
    }
    
    .avatar-wrapper {
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    .avatar-glow {
        position: absolute;
        width: 120px;
        height: 120px;
        border-radius: 50%;
        filter: blur(40px);
        opacity: 0.6;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .avatar-emoji {
        position: relative;
        z-index: 2;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 10px 20px rgba(0,0,0,0.3));
    }
    
    .avatar-bubble {
        position: absolute;
        top: -60px;
        left: 50%;
        transform: translateX(-50%) scale(0);
        background: white;
        padding: 12px 20px;
        border-radius: 20px;
        box-shadow: 0 5px 25px rgba(0,0,0,0.2);
        white-space: nowrap;
        transition: all 0.3s ease;
        z-index: 10;
    }
    
    .avatar-bubble::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        border: 10px solid transparent;
        border-top-color: white;
    }
    
    .bubble-content {
        display: flex;
        align-items: center;
        gap: 8px;
        color: #333;
        font-weight: 500;
    }
    
    .bubble-emoji {
        font-size: 1.3rem;
    }
    
    /* 元素介绍区块 */
    .element-intro {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin: 30px 0;
    }
    
    .element-block {
        flex: 1;
        min-width: 200px;
        max-width: 280px;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        transition: transform 0.3s ease;
        animation: fadeIn 0.8s ease-out;
    }
    
    .element-block:hover {
        transform: translateY(-5px);
    }
    
    .element-icon {
        font-size: 3rem;
        margin-bottom: 10px;
        animation: bounce 2s ease-in-out infinite;
    }
    
    .element-name {
        font-size: 1.3rem;
        font-weight: 700;
        color: #fff;
        margin: 10px 0;
    }
    
    .element-desc {
        font-size: 0.95rem;
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* 重新测试按钮 */
    .restart-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 40px;
        border-radius: 30px;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    
    .restart-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6);
    }
    
    /* Toast 提示样式增强 */
    .stToast {
        animation: slideInRight 0.5s ease-out;
    }
    
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* 气球效果容器 */
    .balloon-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }
    
    /* 发光文字效果 */
    .glow-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin: 30px 0;
        animation: glowPulse 2s ease-in-out infinite;
    }
    
    .glow-fire { color: #FF6B35; text-shadow: 0 0 20px #FF6B35, 0 0 40px #FF6B35, 0 0 60px #FF6B35; }
    .glow-water { color: #4ECDC4; text-shadow: 0 0 20px #4ECDC4, 0 0 40px #4ECDC4, 0 0 60px #4ECDC4; }
    .glow-earth { color: #8B4513; text-shadow: 0 0 20px #8B4513, 0 0 40px #8B4513, 0 0 60px #8B4513; }
    .glow-wind { color: #87CEEB; text-shadow: 0 0 20px #87CEEB, 0 0 40px #87CEEB, 0 0 60px #87CEEB; }
    .glow-mixed { 
        background: linear-gradient(90deg, #FF6B35, #4ECDC4, #8B4513, #87CEEB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(255, 107, 53, 0.5));
    }
    
    @keyframes glowPulse {
        0%, 100% { filter: brightness(1); transform: scale(1); }
        50% { filter: brightness(1.2); transform: scale(1.02); }
    }
    
    /* 居中选项容器 */
    .options-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 15px;
        padding: 20px;
        max-width: 700px;
        margin: 0 auto;
    }
    
    /* 主元素标题 */
    .main-result-title {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        margin: 20px 0;
        animation: resultPopIn 1s ease-out;
    }
    
    @keyframes resultPopIn {
        0% { 
            opacity: 0; 
            transform: scale(0.5) translateY(-50px); 
        }
        60% { 
            transform: scale(1.1); 
        }
        100% { 
            opacity: 1; 
            transform: scale(1) translateY(0); 
        }
    }
    
    .result-subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: rgba(255, 255, 255, 0.95);
        margin-bottom: 20px;
        animation: fadeIn 1s ease-out 0.3s both;
    }
    
    /* 分析卡片样式 */
    .analysis-card {
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 25px;
        margin: 15px 0;
        border: 1px solid rgba(255, 255, 255, 0.3);
        animation: fadeIn 0.8s ease-out;
    }
    
    .analysis-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .analysis-content {
        font-size: 1.1rem;
        line-height: 1.7;
        color: rgba(255, 255, 255, 0.95);
    }
    
    .analysis-icon {
        font-size: 1.5rem;
    }
    
    /* 建议卡片 */
    .advice-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        backdrop-filter: blur(25px);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        border-left: 5px solid;
        animation: slideIn 0.6s ease-out;
        text-align: left;
    }
    
    .advice-icon {
        font-size: 2rem;
        margin-bottom: 10px;
    }
    
    .advice-text {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #fff;
        font-weight: 500;
    }
    </style>
    '''

def get_avatar_html_with_interaction():
    """生成带有交互功能的元素形象HTML"""
    return '''
    <script>
    function showBubble(element, phrase) {
        const bubble = document.getElementById('bubble_' + element);
        if (bubble) {
            bubble.style.transform = 'translateX(-50%) scale(1)';
        }
    }
    
    function hideBubble(element) {
        const bubble = document.getElementById('bubble_' + element);
        if (bubble) {
            bubble.style.transform = 'translateX(-50%) scale(0)';
        }
    }
    
    function triggerClickFeedback(element) {
        const phrases = {
            '火': ['✨ 你和我很合拍！', '🔥 热情之魂！', '💫 一起燃烧吧！'],
            '水': ['🌊 心有灵犀！', '💧 温柔共鸣~', '✨ 你很懂我！'],
            '土': ['🌍 坚实可靠！', '🛡️ 稳如泰山！', '⛰️ 根基深厚！'],
            '风': ['💨 思维同步！', '🧠 智慧相通！', '✨ 灵感迸发！']
        };
        
        const messages = phrases[element] || ['✨ Hi!'];
        const randomMsg = messages[Math.floor(Math.random() * messages.length)];
        
        // 创建气球效果
        createBalloons();
    }
    
    function createBalloons() {
        const container = document.createElement('div');
        container.className = 'balloon-container';
        document.body.appendChild(container);
        
        const colors = ['#FF6B35', '#4ECDC4', '#8B4513', '#87CEEB', '#FFD700', '#FF69B4'];
        
        for (let i = 0; i < 15; i++) {
            setTimeout(() => {
                const balloon = document.createElement('div');
                balloon.innerHTML = ['🎈', '⭐', '✨', '💫', '🎉'][Math.floor(Math.random() * 5)];
                balloon.style.cssText = `
                    position: absolute;
                    left: ${Math.random() * 100}%;
                    bottom: -50px;
                    font-size: ${20 + Math.random() * 20}px;
                    animation: balloonRise ${2 + Math.random() * 2}s ease-out forwards;
                    color: ${colors[Math.floor(Math.random() * colors.length)]};
                `;
                container.appendChild(balloon);
                
                setTimeout(() => balloon.remove(), 4000);
            }, i * 100);
        }
        
        setTimeout(() => container.remove(), 5000);
    }
    
    // 添加气球上升动画
    const style = document.createElement('style');
    style.textContent = `
        @keyframes balloonRise {
            0% { transform: translateY(0) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-100vh) rotate(20deg); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
    </script>
    '''

def render_element_intro():
    """渲染元素介绍区块"""
    st.markdown('<div class="element-intro">', unsafe_allow_html=True)
    
    cols = st.columns(4)
    for idx, (key, elem) in enumerate(ELEMENTS.items()):
        if key == '混合':
            continue
        with cols[idx]:
            st.markdown(f'''
            <div class="element-block" style="background: linear-gradient(135deg, {elem['color']}40, {elem['color']}20);">
                <div class="element-icon">{elem['emoji']}</div>
                <div class="element-name">{elem['name']}</div>
                <div class="element-desc">{elem['description']}</div>
            </div>
            ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_analysis_cards(result_elements):
    """渲染分析卡片（优点、缺点、建议）"""
    # 确定展示哪个元素的分析（混合元素时合并展示）
    if len(result_elements) == 1:
        element_key = result_elements[0]
        elem = ELEMENTS[element_key]
        elements_to_show = [elem]
    else:
        # 混合元素
        elem = ELEMENTS['混合']
        elements_to_show = [elem]
    
    for elem in elements_to_show:
        # 优点卡片
        st.markdown(f'''
        <div class="analysis-card">
            <div class="analysis-title" style="color: #4ECDC4;">
                <span class="analysis-icon">🌟</span>
                <span>你的优点</span>
            </div>
            <div class="analysis-content">
                {elem['description']}
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # 缺点卡片
        st.markdown(f'''
        <div class="analysis-card">
            <div class="analysis-title" style="color: #FF6B35;">
                <span class="analysis-icon">⚠️</span>
                <span>需要注意</span>
            </div>
            <div class="analysis-content">
                {elem['weakness']}
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # 建议卡片
        st.markdown(f'''
        <div class="advice-card" style="border-left-color: {elem['color']};">
            <div style="text-align: center;">
                <span class="advice-icon">{elem['advice_icon']}</span>
                <div style="font-size: 1.2rem; font-weight: 600; color: {elem['color']}; margin-bottom: 10px;">生活建议</div>
            </div>
            <div class="advice-text">
                {elem['advice']}
            </div>
        </div>
        ''', unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title='🔮 元素人格测试仪',
        page_icon='🔮',
        layout='wide',
        initial_sidebar_state="collapsed"
    )
    
    # 注入自定义CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # 初始化session_state
    if 'answers' not in st.session_state:
        st.session_state.answers = []
        st.session_state.current_question = 0
        st.session_state.result = None
    
    # 主界面
    st.markdown('<h1 class="main-title">🔮 元素人格测试仪</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">探索你的内在元素属性，发现独特的自己</p>', unsafe_allow_html=True)
    
    # 渲染元素介绍
    render_element_intro()
    
    if st.session_state.result is None:
        # 测试进行中
        current_q = QUESTIONS[st.session_state.current_question]
        
        # 问题卡片
        st.markdown(f'''
        <div class="question-card">
            <div class="question-text">
                <span class="question-emoji">{current_q['emoji']}</span>
                <span>{current_q['question']}</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # 进度条
        progress = (st.session_state.current_question) / len(QUESTIONS)
        st.progress(progress)
        st.markdown(f'<p style="text-align: center; color: rgba(255,255,255,0.8);">问题 {st.session_state.current_question + 1} / {len(QUESTIONS)}</p>', unsafe_allow_html=True)
        
        # 选项按钮 - 居中布局
        st.markdown('<div class="options-container">', unsafe_allow_html=True)
        
        for i, option in enumerate(current_q['options']):
            if st.button(option['text'], key=f'q{st.session_state.current_question}_{i}'):
                st.session_state.answers.append(option['element'])
                
                # 显示选择提示
                element_emoji = ELEMENTS[option['element']]['emoji']
                st.toast(f'✅ 已选择：{element_emoji} {option["element"]}元素', icon='✨')
                
                if st.session_state.current_question < len(QUESTIONS) - 1:
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    calculate_result()
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        # 结果页面 - 突出显示人格元素
        result = st.session_state.result
        
        st.markdown('''
        <div class="result-card">
        ''', unsafe_allow_html=True)
        
        # 副标题
        st.markdown('<p class="result-subtitle">🎉 测试完成！</p>', unsafe_allow_html=True)
        
        # 获取主导元素的样式类
        if len(result['elements']) == 1:
            element_key = result['elements'][0]
            glow_class = f'glow-{element_key}'
            element_name = ELEMENTS[element_key]['name']
            element_emoji = ELEMENTS[element_key]['emoji']
        else:
            glow_class = 'glow-mixed'
            element_name = '混合元素'
            element_emoji = '🌟'
        
        # 突出显示人格元素 - 大号发光标题
        st.markdown(f'''
        <div class="glow-title {glow_class}">
            <div style="font-size: 1.2rem; margin-bottom: 10px; opacity: 0.9;">您的人格类型是</div>
            <div class="main-result-title">{element_emoji} {element_name}</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # 渲染动态元素形象
        st.markdown('<div style="margin: 40px 0; display: flex; justify-content: center; gap: 60px; flex-wrap: wrap;">', unsafe_allow_html=True)
        
        # 添加交互脚本
        st.markdown(get_avatar_html_with_interaction(), unsafe_allow_html=True)
        
        # 为每个元素创建可点击的形象
        for element in result['elements']:
            st.markdown(get_dynamic_avatar_html(element, size=120), unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 渲染分析卡片（优点、缺点、建议）
        st.markdown('<div style="max-width: 700px; margin: 0 auto;">', unsafe_allow_html=True)
        render_analysis_cards(result['elements'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 详细元素介绍
        st.markdown('<h3 style="color: white; text-align: center; margin: 40px 0 20px;">✨ 元素特性详解 ✨</h3>', unsafe_allow_html=True)
        
        cols = st.columns(2)
        with cols[0]:
            for key in ['火', '水']:
                elem = ELEMENTS[key]
                st.markdown(f'''
                <div class="glass-card" style="margin: 15px 0; text-align: center;">
                    <h3 style="color: {elem['color']}; margin: 10px 0;">{elem['emoji']} {elem['name']}</h3>
                    <p style="color: white;">{elem['description']}</p>
                </div>
                ''', unsafe_allow_html=True)
        
        with cols[1]:
            for key in ['土', '风']:
                elem = ELEMENTS[key]
                st.markdown(f'''
                <div class="glass-card" style="margin: 15px 0; text-align: center;">
                    <h3 style="color: {elem['color']}; margin: 10px 0;">{elem['emoji']} {elem['name']}</h3>
                    <p style="color: white;">{elem['description']}</p>
                </div>
                ''', unsafe_allow_html=True)
        
        # 重新测试按钮
        st.markdown('<div style="text-align: center; margin: 40px 0;">', unsafe_allow_html=True)
        
        if st.button('🔄 重新测试', key='restart_btn', help='点击重新开始测试'):
            st.session_state.answers = []
            st.session_state.current_question = 0
            st.session_state.result = None
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def calculate_result():
    """计算测试结果"""
    element_counts = {'火': 0, '水': 0, '土': 0, '风': 0}
    for answer in st.session_state.answers:
        element_counts[answer] += 1
    
    max_count = max(element_counts.values())
    dominant_elements = [elem for elem, count in element_counts.items() if count == max_count]
    
    if len(dominant_elements) > 1:
        elements_name = ' + '.join([ELEMENTS[e]['name'] for e in dominant_elements])
        st.session_state.result = {
            'type': f'🌟 {elements_name}',
            'elements': dominant_elements,
            'description': '你是多种元素的混合体！拥有丰富多样的个性特质，能够在不同场景中灵活展现不同的魅力。'
        }
    else:
        dominant_element = dominant_elements[0]
        elem = ELEMENTS[dominant_element]
        st.session_state.result = {
            'type': f'{elem["emoji"]} {elem["name"]}',
            'elements': [dominant_element],
            'description': elem['description']
        }

if __name__ == '__main__':
    main()