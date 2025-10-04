import streamlit as st

st.title("SkyShip Game (キー操作版)")

# 初期位置をセッションステートで保存
if "x" not in st.session_state:
    st.session_state.x = 400

# HTML + JS でキー入力を検知して Streamlit に送る
canvas = st.empty()
canvas.markdown(
    f"""
    <div id="game" style="position: relative; width:800px; height:600px; background-color:#87CEEB;">
        <div id="ship" style="position:absolute; left:{st.session_state.x}px; top:500px;
             width:50px; height:30px; background-color:red;"></div>
    </div>
    <script>
    const ship = document.getElementById('ship');
    let x = {st.session_state.x};
    document.addEventListener('keydown', (e) => {{
        if(e.key === 'ArrowLeft') x -= 20;
        if(e.key === 'ArrowRight') x += 20;
        if(x < 0) x = 0;
        if(x > 750) x = 750;
        ship.style.left = x + 'px';
        // Streamlit に値を送る（hidden input 経由）
        const input = document.getElementById('pos_input');
        if(input) input.value = x;
        input.dispatchEvent(new Event('change'));
    }});
    </script>
    <input type="hidden" id="pos_input" value="{st.session_state.x}"/>
    """,
    unsafe_allow_html=True
)

# セッションステート更新用
x_input = st.number_input("位置確認用（更新されます）", value=st.session_state.x, key="x_input")
st.session_state.x = x_input
